import os
import sys
import time
import logging
from typing import Iterable, List, Optional

import psutil


logger = logging.getLogger("flask_video_generator")
if not logger.handlers:
    logging.basicConfig(level=logging.INFO)


class ProcessController:
    """Utilities to control JianYing/CapCut processes on Windows.

    Exposes three static methods used by automation flows:
    - kill_jianying(): terminate CapCut/JianYing related processes
    - restart_jianying(): try to launch the application again
    - kill_jianying_detector(): terminate any detector helper processes
    """

    # Common keywords seen in process names/exe/cmdline for CapCut/JianYing
    _JY_KEYWORDS: List[str] = [
        "capcut",          # International
        "jianying",        # Pinyin
        "剪映",             # Chinese
    ]

    # Helper/child processes to target as part of a full kill
    _JY_AUX_KEYWORDS: List[str] = [
        "cef", "helper", "renderer", "updater", "launcher"
    ]

    @staticmethod
    def _matches_keywords(value: Optional[str], keywords: Iterable[str]) -> bool:
        if not value:
            return False
        lower = value.lower()
        return any(k in lower for k in keywords)

    @staticmethod
    def _proc_matches(proc: psutil.Process, base_keywords: Iterable[str], extra_keywords: Optional[Iterable[str]] = None) -> bool:
        """Return True if process name/exe/cmdline contains the keywords."""
        try:
            name = proc.name()
        except Exception:
            name = None
        try:
            exe = proc.exe()
        except Exception:
            exe = None
        try:
            cmdline = " ".join(proc.cmdline())
        except Exception:
            cmdline = None

        base_ok = (
            ProcessController._matches_keywords(name, base_keywords)
            or ProcessController._matches_keywords(exe, base_keywords)
            or ProcessController._matches_keywords(cmdline, base_keywords)
        )
        if not base_ok:
            return False

        if not extra_keywords:
            return True

        # If extra keywords are provided, require at least one of them too
        return (
            ProcessController._matches_keywords(name, extra_keywords)
            or ProcessController._matches_keywords(exe, extra_keywords)
            or ProcessController._matches_keywords(cmdline, extra_keywords)
        )

    @staticmethod
    def _terminate_processes(filter_fn, grace_seconds: float = 3.0) -> int:
        """Terminate processes matching filter_fn. Returns count of processes killed."""
        targeted: List[psutil.Process] = []
        for proc in psutil.process_iter(["pid", "name", "exe", "cmdline"]):
            try:
                if not filter_fn(proc):
                    continue
                logger.info(f"Terminating PID {proc.pid}: {proc.name()}")
                proc.terminate()
                targeted.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        if targeted:
            gone, alive = psutil.wait_procs(targeted, timeout=grace_seconds)
            # Force kill any that remain and still match filter
            for proc in alive:
                try:
                    if filter_fn(proc):
                        logger.warning(f"Killing stubborn PID {proc.pid}: {proc.name()}")
                        proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        return len(targeted)

    @staticmethod
    def kill_jianying() -> int:
        """Kill CapCut/JianYing processes. Returns number of terminated processes."""
        logger.info("Killing JianYing/CapCut processes...")
        base = ProcessController._JY_KEYWORDS
        aux = ProcessController._JY_AUX_KEYWORDS

        def filter_fn(proc: psutil.Process) -> bool:
            # Match main app or its common helpers
            return ProcessController._proc_matches(proc, base) or ProcessController._proc_matches(proc, base, aux)

        killed = ProcessController._terminate_processes(filter_fn)
        logger.info(f"Killed {killed} JianYing/CapCut related processes")
        return killed

    @staticmethod
    def kill_jianying_detector() -> int:
        """Kill any JianYing/CapCut detector helper processes. Returns number killed."""
        logger.info("Killing JianYing/CapCut detector processes...")

        def filter_fn(proc: psutil.Process) -> bool:
            return ProcessController._proc_matches(proc, ProcessController._JY_KEYWORDS, ["detect", "detector", "watcher", "monitor"])

        killed = ProcessController._terminate_processes(filter_fn)
        logger.info(f"Killed {killed} detector processes")
        return killed

    @staticmethod
    def _candidate_launch_paths() -> List[str]:
        """Return candidate paths (.exe or .lnk) to launch JianYing/CapCut."""
        candidates: List[str] = []

        # Common install locations
        pf = os.environ.get("ProgramFiles", r"C:\\Program Files")
        pf86 = os.environ.get("ProgramFiles(x86)", r"C:\\Program Files (x86)")
        local_appdata = os.environ.get("LOCALAPPDATA", os.path.expanduser(r"~\\AppData\\Local"))
        appdata_roaming = os.environ.get("APPDATA", os.path.expanduser(r"~\\AppData\\Roaming"))

        likely_dirs = [
            os.path.join(pf, "CapCut"),
            os.path.join(pf86, "CapCut"),
            os.path.join(local_appdata, "CapCut"),
            os.path.join(local_appdata, "Programs", "CapCut"),
        ]

        likely_exe_names = ["CapCut.exe", "JianYing.exe", "JianyingPro.exe"]
        for base_dir in likely_dirs:
            for exe_name in likely_exe_names:
                candidates.append(os.path.join(base_dir, exe_name))

        # Start Menu shortcuts (user + all users)
        start_menu_dirs = [
            os.path.join(appdata_roaming, r"Microsoft\\Windows\\Start Menu\\Programs"),
            r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs",
        ]
        lnk_names = ["CapCut.lnk", "剪映.lnk", "JianYing.lnk", "剪映专业版.lnk"]
        for d in start_menu_dirs:
            for root, _dirs, files in os.walk(d):
                for file in files:
                    if file in lnk_names:
                        candidates.append(os.path.join(root, file))

        # Filter existing
        return [p for p in candidates if os.path.exists(p)]

    @staticmethod
    def restart_jianying(wait_seconds: float = 2.0) -> bool:
        """Attempt to start JianYing/CapCut. Returns True if a launch was attempted and a window is expected to appear."""
        # First ensure old processes are gone
        try:
            ProcessController.kill_jianying_detector()
            ProcessController.kill_jianying()
        except Exception:
            # Proceed even if kill has issues
            pass

        candidates = ProcessController._candidate_launch_paths()
        launched = False
        for path in candidates:
            try:
                logger.info(f"Launching JianYing/CapCut via: {path}")
                os.startfile(path)
                launched = True
                break
            except Exception as e:
                logger.debug(f"Failed to start using {path}: {e}")

        if not launched:
            logger.error("Unable to locate CapCut/JianYing executable or shortcut. Please start it manually.")
            return False

        # Give the app a moment to initialize
        time.sleep(wait_seconds)
        return True


