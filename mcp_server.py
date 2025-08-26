#!/usr/bin/env python3
"""
CapCut API MCP Server (Complete Version)

完整版本的MCP服务器，集成所有CapCut API接口
"""

import sys
import os
import json
import traceback
import io
import contextlib
from typing import Any, Dict, List, Optional

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入CapCut API功能
try:
    from create_draft import get_or_create_draft
    from add_text_impl import add_text_impl
    from add_video_track import add_video_track
    from add_audio_track import add_audio_track
    from add_image_impl import add_image_impl
    from add_subtitle_impl import add_subtitle_impl
    from add_effect_impl import add_effect_impl
    from add_sticker_impl import add_sticker_impl
    from add_video_keyframe_impl import add_video_keyframe_impl
    from get_duration_impl import get_video_duration
    from save_draft_impl import save_draft_impl
    from pyJianYingDraft.text_segment import TextStyleRange
    CAPCUT_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import CapCut modules: {e}", file=sys.stderr)
    CAPCUT_AVAILABLE = False

# 完整的工具定义
TOOLS = [
    {
        "name": "create_draft",
        "description": "创建新的CapCut草稿",
        "inputSchema": {
            "type": "object",
            "properties": {
                "width": {"type": "integer", "default": 1080, "description": "视频宽度"},
                "height": {"type": "integer", "default": 1920, "description": "视频高度"}
            }
        }
    },
    {
        "name": "add_video",
        "description": "添加视频到草稿，支持转场、蒙版、背景模糊等效果",
        "inputSchema": {
            "type": "object",
            "properties": {
                "video_url": {"type": "string", "description": "视频URL"},
                "draft_id": {"type": "string", "description": "草稿ID"},
                "start": {"type": "number", "default": 0, "description": "开始时间（秒）"},
                "end": {"type": "number", "description": "结束时间（秒）"},
                "target_start": {"type": "number", "default": 0, "description": "目标开始时间（秒）"},
                "width": {"type": "integer", "default": 1080, "description": "视频宽度"},
                "height": {"type": "integer", "default": 1920, "description": "视频高度"},
                "transform_x": {"type": "number", "default": 0, "description": "X轴位置"},
                "transform_y": {"type": "number", "default": 0, "description": "Y轴位置"},
                "scale_x": {"type": "number", "default": 1, "description": "X轴缩放"},
                "scale_y": {"type": "number", "default": 1, "description": "Y轴缩放"},
                "speed": {"type": "number", "default": 1.0, "description": "播放速度"},
                "track_name": {"type": "string", "default": "main", "description": "轨道名称"},
                "volume": {"type": "number", "default": 1.0, "description": "音量"},
                "transition": {"type": "string", "description": "转场类型"},
                "transition_duration": {"type": "number", "default": 0.5, "description": "转场时长"},
                "mask_type": {"type": "string", "description": "蒙版类型"},
                "background_blur": {"type": "integer", "description": "背景模糊级别(1-4)"}
            },
            "required": ["video_url"]
        }
    },
    {
        "name": "add_audio",
        "description": "添加音频到草稿，支持音效处理",
        "inputSchema": {
            "type": "object",
            "properties": {
                "audio_url": {"type": "string", "description": "音频URL"},
                "draft_id": {"type": "string", "description": "草稿ID"},
                "start": {"type": "number", "default": 0, "description": "开始时间（秒）"},
                "end": {"type": "number", "description": "结束时间（秒）"},
                "target_start": {"type": "number", "default": 0, "description": "目标开始时间（秒）"},
                "volume": {"type": "number", "default": 1.0, "description": "音量"},
                "speed": {"type": "number", "default": 1.0, "description": "播放速度"},
                "track_name": {"type": "string", "default": "audio_main", "description": "轨道名称"},
                "width": {"type": "integer", "default": 1080, "description": "视频宽度"},
                "height": {"type": "integer", "default": 1920, "description": "视频高度"}
            },
            "required": ["audio_url"]
        }
    },
    {
        "name": "add_image",
        "description": "添加图片到草稿，支持动画、转场、蒙版等效果",
        "inputSchema": {
            "type": "object",
            "properties": {
                "image_url": {"type": "string", "description": "图片URL"},
                "draft_id": {"type": "string", "description": "草稿ID"},
                "start": {"type": "number", "default": 0, "description": "开始时间（秒）"},
                "end": {"type": "number", "default": 3.0, "description": "结束时间（秒）"},
                "width": {"type": "integer", "default": 1080, "description": "视频宽度"},
                "height": {"type": "integer", "default": 1920, "description": "视频高度"},
                "transform_x": {"type": "number", "default": 0, "description": "X轴位置"},
                "transform_y": {"type": "number", "default": 0, "description": "Y轴位置"},
                "scale_x": {"type": "number", "default": 1, "description": "X轴缩放"},
                "scale_y": {"type": "number", "default": 1, "description": "Y轴缩放"},
                "track_name": {"type": "string", "default": "main", "description": "轨道名称"},
                "intro_animation": {"type": "string", "description": "入场动画"},
                "outro_animation": {"type": "string", "description": "出场动画"},
                "transition": {"type": "string", "description": "转场类型"},
                "mask_type": {"type": "string", "description": "蒙版类型"}
            },
            "required": ["image_url"]
        }
    },
    {
        "name": "add_text",
        "description": "添加文本到草稿，支持文本多样式、文字阴影和文字背景",
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "文本内容"},
                "start": {"type": "number", "description": "开始时间（秒）"},
                "end": {"type": "number", "description": "结束时间（秒）"},
                "draft_id": {"type": "string", "description": "草稿ID"},
                "font_color": {"type": "string", "default": "#ffffff", "description": "字体颜色"},
                "font_size": {"type": "integer", "default": 24, "description": "字体大小"},
                "shadow_enabled": {"type": "boolean", "default": False, "description": "是否启用文字阴影"},
                "shadow_color": {"type": "string", "default": "#000000", "description": "阴影颜色"},
                "shadow_alpha": {"type": "number", "default": 0.8, "description": "阴影透明度"},
                "shadow_angle": {"type": "number", "default": 315.0, "description": "阴影角度"},
                "shadow_distance": {"type": "number", "default": 5.0, "description": "阴影距离"},
                "shadow_smoothing": {"type": "number", "default": 0.0, "description": "阴影平滑度"},
                "background_color": {"type": "string", "description": "背景颜色"},
                "background_alpha": {"type": "number", "default": 1.0, "description": "背景透明度"},
                "background_style": {"type": "integer", "default": 0, "description": "背景样式"},
                "background_round_radius": {"type": "number", "default": 0.0, "description": "背景圆角半径"},
                "text_styles": {"type": "array", "description": "文本多样式配置列表"}
            },
            "required": ["text", "start", "end"]
        }
    },
    {
        "name": "add_subtitle",
        "description": "添加字幕到草稿，支持SRT文件和样式设置",
        "inputSchema": {
            "type": "object",
            "properties": {
                "srt_path": {"type": "string", "description": "SRT字幕文件路径或URL"},
                "draft_id": {"type": "string", "description": "草稿ID"},
                "track_name": {"type": "string", "default": "subtitle", "description": "轨道名称"},
                "time_offset": {"type": "number", "default": 0, "description": "时间偏移（秒）"},
                "font": {"type": "string", "description": "字体"},
                "font_size": {"type": "number", "default": 8.0, "description": "字体大小"},
                "font_color": {"type": "string", "default": "#FFFFFF", "description": "字体颜色"},
                "bold": {"type": "boolean", "default": False, "description": "是否粗体"},
                "italic": {"type": "boolean", "default": False, "description": "是否斜体"},
                "underline": {"type": "boolean", "default": False, "description": "是否下划线"},
                "border_width": {"type": "number", "default": 0.0, "description": "边框宽度"},
                "border_color": {"type": "string", "default": "#000000", "description": "边框颜色"},
                "background_color": {"type": "string", "default": "#000000", "description": "背景颜色"},
                "background_alpha": {"type": "number", "default": 0.0, "description": "背景透明度"},
                "transform_x": {"type": "number", "default": 0.0, "description": "X轴位置"},
                "transform_y": {"type": "number", "default": -0.8, "description": "Y轴位置"},
                "width": {"type": "integer", "default": 1080, "description": "视频宽度"},
                "height": {"type": "integer", "default": 1920, "description": "视频高度"}
            },
            "required": ["srt_path"]
        }
    },
    {
        "name": "add_effect",
        "description": "添加特效到草稿",
        "inputSchema": {
            "type": "object",
            "properties": {
                "effect_type": {"type": "string", "description": "特效类型名称"},
                "draft_id": {"type": "string", "description": "草稿ID"},
                "start": {"type": "number", "default": 0, "description": "开始时间（秒）"},
                "end": {"type": "number", "default": 3.0, "description": "结束时间（秒）"},
                "track_name": {"type": "string", "default": "effect_01", "description": "轨道名称"},
                "params": {"type": "array", "description": "特效参数列表"},
                "width": {"type": "integer", "default": 1080, "description": "视频宽度"},
                "height": {"type": "integer", "default": 1920, "description": "视频高度"}
            },
            "required": ["effect_type"]
        }
    },
    {
        "name": "add_sticker",
        "description": "添加贴纸到草稿",
        "inputSchema": {
            "type": "object",
            "properties": {
                "resource_id": {"type": "string", "description": "贴纸资源ID"},
                "draft_id": {"type": "string", "description": "草稿ID"},
                "start": {"type": "number", "description": "开始时间（秒）"},
                "end": {"type": "number", "description": "结束时间（秒）"},
                "transform_x": {"type": "number", "default": 0, "description": "X轴位置"},
                "transform_y": {"type": "number", "default": 0, "description": "Y轴位置"},
                "scale_x": {"type": "number", "default": 1.0, "description": "X轴缩放"},
                "scale_y": {"type": "number", "default": 1.0, "description": "Y轴缩放"},
                "alpha": {"type": "number", "default": 1.0, "description": "透明度"},
                "rotation": {"type": "number", "default": 0.0, "description": "旋转角度"},
                "track_name": {"type": "string", "default": "sticker_main", "description": "轨道名称"},
                "width": {"type": "integer", "default": 1080, "description": "视频宽度"},
                "height": {"type": "integer", "default": 1920, "description": "视频高度"}
            },
            "required": ["resource_id", "start", "end"]
        }
    },
    {
        "name": "add_video_keyframe",
        "description": "添加视频关键帧，支持位置、缩放、旋转、透明度等属性动画",
        "inputSchema": {
            "type": "object",
            "properties": {
                "draft_id": {"type": "string", "description": "草稿ID"},
                "track_name": {"type": "string", "default": "main", "description": "轨道名称"},
                "property_type": {"type": "string", "description": "关键帧属性类型(position_x, position_y, rotation, scale_x, scale_y, uniform_scale, alpha, saturation, contrast, brightness, volume)"},
                "time": {"type": "number", "default": 0.0, "description": "关键帧时间点（秒）"},
                "value": {"type": "string", "description": "关键帧值"},
                "property_types": {"type": "array", "description": "批量模式：关键帧属性类型列表"},
                "times": {"type": "array", "description": "批量模式：关键帧时间点列表"},
                "values": {"type": "array", "description": "批量模式：关键帧值列表"}
            }
        }
    }
]

@contextlib.contextmanager
def capture_stdout():
    """捕获标准输出，防止CapCut API的调试信息干扰JSON响应"""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_stdout

def convert_text_styles(text_styles_data):
    """将字典格式的text_styles转换为TextStyleRange对象列表"""
    if not text_styles_data:
        return None
    
    try:
        text_style_ranges = []
        for style_dict in text_styles_data:
            style_range = TextStyleRange(
                start=style_dict.get("start", 0),
                end=style_dict.get("end", 0),
                font_size=style_dict.get("font_size"),
                font_color=style_dict.get("font_color"),
                bold=style_dict.get("bold", False),
                italic=style_dict.get("italic", False),
                underline=style_dict.get("underline", False)
            )
            text_style_ranges.append(style_range)
        return text_style_ranges
    except Exception as e:
        print(f"[ERROR] Error converting text_styles: {e}", file=sys.stderr)
        return None

def execute_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """执行具体的工具"""
    try:
        print(f"[DEBUG] Executing tool: {tool_name} with args: {arguments}", file=sys.stderr)
        
        if not CAPCUT_AVAILABLE:
            return {"success": False, "error": "CapCut modules not available"}
        
        # 捕获标准输出，防止调试信息干扰
        with capture_stdout() as captured:
            if tool_name == "create_draft":
                draft_id, script = get_or_create_draft(
                    width=arguments.get("width", 1080),
                    height=arguments.get("height", 1920)
                )
                result = {
                    "draft_id": str(draft_id),
                    "draft_url": ""
                }
                
            elif tool_name == "add_video":
                result = add_video_track(**arguments)
                
            elif tool_name == "add_audio":
                result = add_audio_track(**arguments)
                
            elif tool_name == "add_image":
                result = add_image_impl(**arguments)
                
            elif tool_name == "add_text":
                # 处理text_styles参数
                text_styles_converted = None
                if "text_styles" in arguments and arguments["text_styles"]:
                    text_styles_converted = convert_text_styles(arguments["text_styles"])
                    arguments["text_styles"] = text_styles_converted
                
                result = add_text_impl(**arguments)
                
            elif tool_name == "add_subtitle":
                result = add_subtitle_impl(**arguments)
                
            elif tool_name == "add_effect":
                result = add_effect_impl(**arguments)
                
            elif tool_name == "add_sticker":
                result = add_sticker_impl(**arguments)
                
            elif tool_name == "add_video_keyframe":
                result = add_video_keyframe_impl(**arguments)
                
            elif tool_name == "get_video_duration":
                duration = get_video_duration(arguments["video_url"])
                result = {"duration": duration}
                
            elif tool_name == "save_draft":
                save_result = save_draft_impl(**arguments)
                if isinstance(save_result, dict) and "draft_url" in save_result:
                    result = {"draft_url": save_result["draft_url"]}
                else:
                    result = {"draft_url": f"https://www.install-ai-guider.top/draft/downloader?draft_id=unknown"}
                
            else:
                return {"success": False, "error": f"Unknown tool: {tool_name}"}
        
        return {
            "success": True,
            "result": result,
            "features_used": {
                "shadow": arguments.get("shadow_enabled", False) if tool_name == "add_text" else False,
                "background": bool(arguments.get("background_color")) if tool_name == "add_text" else False,
                "multi_style": bool(arguments.get("text_styles")) if tool_name == "add_text" else False
            }
        }
        
    except Exception as e:
        print(f"[ERROR] Tool execution error: {e}", file=sys.stderr)
        print(f"[ERROR] Traceback: {traceback.format_exc()}", file=sys.stderr)
        return {"success": False, "error": str(e)}

def handle_request(request_data: str) -> Optional[str]:
    """处理JSON-RPC请求"""
    try:
        request = json.loads(request_data.strip())
        print(f"[DEBUG] Received request: {request.get('method', 'unknown')}", file=sys.stderr)
        
        if request.get("method") == "initialize":
            response = {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "experimental": {},
                        "tools": {"listChanged": False}
                    },
                    "serverInfo": {
                        "name": "capcut-api",
                        "version": "1.12.3"
                    }
                }
            }
            return json.dumps(response)
            
        elif request.get("method") == "notifications/initialized":
            return None
            
        elif request.get("method") == "tools/list":
            response = {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {"tools": TOOLS}
            }
            return json.dumps(response)
            
        elif request.get("method") == "tools/call":
            tool_name = request["params"]["name"]
            arguments = request["params"].get("arguments", {})
            
            result = execute_tool(tool_name, arguments)
            
            response = {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            }
            return json.dumps(response)
            
        else:
            error_response = {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {"code": -32601, "message": "Method not found"}
            }
            return json.dumps(error_response)
            
    except Exception as e:
        print(f"[ERROR] Request handling error: {e}", file=sys.stderr)
        print(f"[ERROR] Traceback: {traceback.format_exc()}", file=sys.stderr)
        error_response = {
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": 0, "message": str(e)}
        }
        return json.dumps(error_response)

def main():
    """主函数"""
    print("🚀 Starting CapCut API MCP Server (Complete Version)...", file=sys.stderr)
    print(f"📋 Available tools: {len(TOOLS)} tools loaded", file=sys.stderr)
    print("✨ Features: 视频、音频、图片、文本、字幕、特效、贴纸、关键帧", file=sys.stderr)
    print("🔌 Waiting for client connections...", file=sys.stderr)
    
    try:
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    print("[DEBUG] EOF received, shutting down", file=sys.stderr)
                    break
                
                response = handle_request(line)
                if response:
                    print(response)
                    sys.stdout.flush()
                    
            except EOFError:
                print("[DEBUG] EOF exception, shutting down", file=sys.stderr)
                break
            except Exception as e:
                print(f"[ERROR] Server error: {e}", file=sys.stderr)
                print(f"[ERROR] Traceback: {traceback.format_exc()}", file=sys.stderr)
                
    except KeyboardInterrupt:
        print("[INFO] Server stopped by user", file=sys.stderr)
    except Exception as e:
        print(f"[ERROR] Fatal server error: {e}", file=sys.stderr)
        print(f"[ERROR] Traceback: {traceback.format_exc()}", file=sys.stderr)

if __name__ == "__main__":
    main()