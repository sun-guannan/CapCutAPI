#!/usr/bin/env python3
"""
Streaming-capable MCP server for CapCut API tools.

This server reuses the tool registry and execution logic defined in
`mcp_server.py` but exposes them through the `mcp` FastMCP server,
which supports stdio and SSE (HTTP) transports.
"""

import argparse
import sys
from typing import Any, Dict, Optional, List
from dotenv import load_dotenv
from pathlib import Path
import logging
from mcp.server.fastmcp import FastMCP
import mcp.types as types
# pydantic is intentionally not required here for flat handlers

# Reuse tool schemas and executor from the existing implementation
from mcp_tools import execute_tool, TOOLS

# Load environment variables from .env file
env_file = Path(__file__).parent / ".env"
logger = logging.getLogger(__name__)
if not logging.getLogger().hasHandlers():
    logging.basicConfig(level=logging.INFO)
if env_file.exists():
    load_dotenv(env_file)
    logger.info(f"Loaded environment from: {env_file}")
else:
    logger.warning(f"Environment file not found: {env_file}")
    logger.info("Using default environment variables")


def _json_type_to_py(type_name: str) -> Any:
    mapping: Dict[str, Any] = {
        "string": str,
        "number": float,
        "integer": int,
        "boolean": bool,
        "array": list[Any],
        "object": dict[str, Any],
    }
    return mapping.get(type_name, Any)


def _args_dict() -> Dict[str, Any]:
    _locals = locals()
    return {k: v for k, v in _locals.items() if (k not in {"_locals"} and v is not None)}


# Manual tool handlers with flattened parameters (required first)
def tool_create_draft(width: int = 1080, height: int = 1920) -> Dict[str, Any]:
    arguments = {"width": width, "height": height}
    return execute_tool("create_draft", arguments)


def tool_add_video(
    video_url: str,
    draft_id: str,
    start: float = 0,
    end: Optional[float] = None,
    target_start: float = 0,
    width: int = 1080,
    height: int = 1920,
    transform_x: float = 0,
    transform_y: float = 0,
    scale_x: float = 1,
    scale_y: float = 1,
    speed: float = 1.0,
    track_name: str = "main",
    volume: float = 1.0,
    transition: Optional[str] = None,
    transition_duration: float = 0.5,
    mask_type: Optional[str] = None,
    background_blur: Optional[int] = None,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "video_url": video_url,
        "draft_id": draft_id,
        "start": start,
        "end": end,
        "target_start": target_start,
        "width": width,
        "height": height,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "speed": speed,
        "track_name": track_name,
        "volume": volume,
        "transition": transition,
        "transition_duration": transition_duration,
        "mask_type": mask_type,
        "background_blur": background_blur,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_video", arguments)


def tool_add_audio(
    audio_url: str,
    draft_id: str,
    start: float = 0,
    end: Optional[float] = None,
    target_start: float = 0,
    volume: float = 1.0,
    speed: float = 1.0,
    track_name: str = "audio_main",
    width: int = 1080,
    height: int = 1920,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "audio_url": audio_url,
        "draft_id": draft_id,
        "start": start,
        "end": end,
        "target_start": target_start,
        "volume": volume,
        "speed": speed,
        "track_name": track_name,
        "width": width,
        "height": height,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_audio", arguments)


def tool_add_image(
    image_url: str,
    draft_id: str,
    start: float = 0,
    end: float = 3.0,
    width: int = 1080,
    height: int = 1920,
    transform_x: float = 0,
    transform_y: float = 0,
    scale_x: float = 1,
    scale_y: float = 1,
    track_name: str = "main",
    intro_animation: Optional[str] = None,
    outro_animation: Optional[str] = None,
    transition: Optional[str] = None,
    mask_type: Optional[str] = None,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "image_url": image_url,
        "draft_id": draft_id,
        "start": start,
        "end": end,
        "width": width,
        "height": height,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "track_name": track_name,
        "intro_animation": intro_animation,
        "outro_animation": outro_animation,
        "transition": transition,
        "mask_type": mask_type,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_image", arguments)


def tool_add_text(
    text: str,
    start: float,
    end: float,
    draft_id: str,
    font_color: str = "#ffffff",
    font_size: int = 24,
    shadow_enabled: bool = False,
    shadow_color: str = "#000000",
    shadow_alpha: float = 0.8,
    shadow_angle: float = 315.0,
    shadow_distance: float = 5.0,
    shadow_smoothing: float = 0.0,
    background_color: Optional[str] = None,
    background_alpha: float = 1.0,
    background_style: int = 0,
    background_round_radius: float = 0.0,
    text_styles: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "text": text,
        "start": start,
        "end": end,
        "draft_id": draft_id,
        "font_color": font_color,
        "font_size": font_size,
        "shadow_enabled": shadow_enabled,
        "shadow_color": shadow_color,
        "shadow_alpha": shadow_alpha,
        "shadow_angle": shadow_angle,
        "shadow_distance": shadow_distance,
        "shadow_smoothing": shadow_smoothing,
        "background_color": background_color,
        "background_alpha": background_alpha,
        "background_style": background_style,
        "background_round_radius": background_round_radius,
        "text_styles": text_styles,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_text", arguments)


def tool_add_subtitle(
    srt_path: str,
    draft_id: str,
    track_name: str = "subtitle",
    time_offset: float = 0,
    font: Optional[str] = None,
    font_size: float = 8.0,
    font_color: str = "#FFFFFF",
    bold: bool = False,
    italic: bool = False,
    underline: bool = False,
    border_width: float = 0.0,
    border_color: str = "#000000",
    background_color: str = "#000000",
    background_alpha: float = 0.0,
    transform_x: float = 0.0,
    transform_y: float = -0.8,
    width: int = 1080,
    height: int = 1920,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "srt_path": srt_path,
        "draft_id": draft_id,
        "track_name": track_name,
        "time_offset": time_offset,
        "font": font,
        "font_size": font_size,
        "font_color": font_color,
        "bold": bold,
        "italic": italic,
        "underline": underline,
        "border_width": border_width,
        "border_color": border_color,
        "background_color": background_color,
        "background_alpha": background_alpha,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "width": width,
        "height": height,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_subtitle", arguments)


def tool_add_effect(
    effect_type: str,
    draft_id: str,
    start: float = 0,
    end: float = 3.0,
    track_name: str = "effect_01",
    params: Optional[List[Any]] = None,
    width: int = 1080,
    height: int = 1920,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "effect_type": effect_type,
        "draft_id": draft_id,
        "start": start,
        "end": end,
        "track_name": track_name,
        "params": params,
        "width": width,
        "height": height,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_effect", arguments)


def tool_add_sticker(
    resource_id: str,
    start: float,
    end: float,
    draft_id: str,
    transform_x: float = 0,
    transform_y: float = 0,
    scale_x: float = 1.0,
    scale_y: float = 1.0,
    alpha: float = 1.0,
    rotation: float = 0.0,
    track_name: str = "sticker_main",
    width: int = 1080,
    height: int = 1920,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "resource_id": resource_id,
        "draft_id": draft_id,
        "start": start,
        "end": end,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "alpha": alpha,
        "rotation": rotation,
        "track_name": track_name,
        "width": width,
        "height": height,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_sticker", arguments)


def tool_add_video_keyframe(
    draft_id: str,
    track_name: str = "main",
    property_type: Optional[str] = None,
    time: float = 0.0,
    value: Optional[str] = None,
    property_types: Optional[List[str]] = None,
    times: Optional[List[float]] = None,
    values: Optional[List[Any]] = None,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "draft_id": draft_id,
        "track_name": track_name,
        "property_type": property_type,
        "time": time,
        "value": value,
        "property_types": property_types,
        "times": times,
        "values": values,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("add_video_keyframe", arguments)


def tool_generate_video(
    draft_id: str,
    resolution: str = "1080p",
    framerate: str = "30fps",
    name: Optional[str] = None,
) -> Dict[str, Any]:
    arguments: Dict[str, Any] = {
        "draft_id": draft_id,
        "resolution": resolution,
        "framerate": framerate,
        "name": name,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return execute_tool("generate_video", arguments)


def _register_tools(app: FastMCP) -> None:
    """Register tools with explicit flat-parameter handlers."""
    app.add_tool(tool_create_draft, name="create_draft", description="创建新的CapCut草稿")
    app.add_tool(tool_add_video, name="add_video", description="添加视频到草稿，支持转场、蒙版、背景模糊等效果")
    app.add_tool(tool_add_audio, name="add_audio", description="添加音频到草稿，支持音效处理")
    app.add_tool(tool_add_image, name="add_image", description="添加图片到草稿，支持动画、转场、蒙版等效果")
    app.add_tool(tool_add_text, name="add_text", description="添加文本到草稿，支持文本多样式、文字阴影和文字背景")
    app.add_tool(tool_add_subtitle, name="add_subtitle", description="添加字幕到草稿，支持SRT文件和样式设置")
    app.add_tool(tool_add_effect, name="add_effect", description="添加特效到草稿")
    app.add_tool(tool_add_sticker, name="add_sticker", description="添加贴纸到草稿")
    app.add_tool(tool_add_video_keyframe, name="add_video_keyframe", description="添加视频关键帧，支持属性动画")
    app.add_tool(tool_generate_video, name="generate_video", description="生成渲染视频")

def _override_list_tools(app: FastMCP) -> None:
    """Override list_tools to include inputSchema from TOOLS (and optional outputSchema)."""
    tool_map: Dict[str, Dict[str, Any]] = {t.get("name", ""): t for t in TOOLS if t.get("name")}

    @app._mcp_server.list_tools()  # type: ignore[attr-defined]
    async def list_tools() -> list[types.Tool]:
        result: list[types.Tool] = []
        for name, spec in tool_map.items():
            result.append(
                types.Tool(
                    name=name,
                    description=spec.get("description", ""),
                    inputSchema=spec.get("inputSchema", {"type": "object"}),
                    outputSchema=spec.get("outputSchema"),
                )
            )
        return result

def create_fastmcp_app(host: str = "127.0.0.1", port: int = 3333, path: str = "/mcp") -> FastMCP:
    """Factory to create a FastMCP app with tools registered and list_tools overridden."""
    app = FastMCP("capcut-api", host=host, port=port, streamable_http_path=path)
    _register_tools(app)
    _override_list_tools(app)
    return app


def main() -> None:
    parser = argparse.ArgumentParser(description="Streaming-capable MCP server for CapCut API")
    parser.add_argument("--host", default="127.0.0.1", help="streamable host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=3333, help="streamable port (default: 3333)")
    args = parser.parse_args()

    app = FastMCP("capcut-api", host=args.host, port=args.port)
    _register_tools(app)
    _override_list_tools(app)

    print(f"Starting CapCut FastMCP SSE server on http://{args.host}:{args.port}", file=sys.stderr)
    app.run(transport="streamable-http", mount_path="/streamable")


if __name__ == "__main__":
    main()


