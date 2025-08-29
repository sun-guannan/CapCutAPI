import os
import logging
from typing import Any, Dict, Optional

from save_draft_impl import query_script_impl
from db import get_session
from models import VideoTask
from sqlalchemy import select


logger = logging.getLogger(__name__)


def generate_video_impl(
    draft_id: str,
    resolution: Optional[str] = None,
    framerate: Optional[float] = None,
    name: Optional[str] = None,
) -> Dict[str, Any]:
    """Kick off Celery pipeline to generate a video for a given draft.

    Args:
        draft_id: The draft identifier to render.
        resolution: Target resolution label (e.g., "1080p", "720p"). If omitted, worker default is used.
        framerate: Target framerate (e.g., 30.0, 60.0). If omitted, worker default is used.
        name: Optional override for the draft/video name embedded in content.

    Returns:
        A dict with keys:
        - success: Whether the dispatch was successful.
        - output: {"final_task_id": str, "unique_dir_name": Optional[str]} when successful.
        - error: Error message string when unsuccessful.
    """
    result: Dict[str, Any] = {"success": False, "output": "", "error": ""}

    if not draft_id:
        result["error"] = "Hi, the required parameter 'draft_id' is missing. Please add it and try again."
        return result

    try:
        from celery import Celery
        import json

        script = query_script_impl(draft_id, force_update=False)
        if script is None:
            result["error"] = f"Draft {draft_id} not found in cache. Please create or save the draft first."
            return result

        draft_content = json.loads(script.dumps())
        if name:
            draft_content["name"] = name

        broker_url = os.getenv("CELERY_BROKER_URL") or os.getenv("REDIS_URL")
        backend_url = os.getenv("CELERY_RESULT_BACKEND") or os.getenv("REDIS_URL")

        if not broker_url or not backend_url:
            result["error"] = "CELERY_BROKER_URL and CELERY_RESULT_BACKEND environment variables are required"
            return result

        celery_client = Celery(broker=broker_url, backend=backend_url)
        try:
            insp = celery_client.control.inspect(timeout=1)
            ping_result = insp.ping() if insp else None
        except Exception:
            ping_result = None
        if not ping_result:
            logger.warning(
                "No Celery workers responded to ping. Verify worker is running and connected to the same broker/result backend."
            )

        process_sig = celery_client.signature(
            "s3_asset_downloader.tasks.process_draft_content",
            kwargs={"draft_content": draft_content},
            queue="default",
        )

        generate_sig = celery_client.signature(
            "s3_asset_downloader.tasks.generate_video",
            kwargs={"output_path": None, "resolution": resolution, "framerate": framerate},
            queue="default",
        )

        chain_result = (process_sig | generate_sig).apply_async()
        logger.info(f"Dispatched Celery chain. Final task id: {chain_result.id}")

        first_result = chain_result
        while getattr(first_result, "parent", None) is not None:
            first_result = first_result.parent

        unique_dir_name = None
        try:
            process_task_id = getattr(first_result, "id", None)
            if process_task_id:
                process_async = celery_client.AsyncResult(process_task_id)
                if process_async.ready() and isinstance(process_async.result, dict):
                    unique_dir_name = process_async.result.get("unique_dir_name")
        except Exception:
            unique_dir_name = None

        final_task_id = chain_result.id
        try:
            with get_session() as session:
                existing = session.execute(select(VideoTask).where(VideoTask.task_id == final_task_id)).scalar_one_or_none()
                if not existing:
                    session.add(
                        VideoTask(
                            task_id=final_task_id,
                            draft_id=draft_id,
                            status="initialized",
                            extra={"unique_dir_name": unique_dir_name},
                        )
                    )
        except Exception as e:
            logger.error(f"Failed to insert video task {final_task_id}: {e}")

        result["success"] = True
        result["output"] = {"final_task_id": final_task_id, "unique_dir_name": unique_dir_name}
        return result

    except Exception as e:
        result["error"] = f"Error occurred while generating video: {str(e)}"
        return result


