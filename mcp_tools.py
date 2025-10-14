#!/usr/bin/env python3
"""
CapCut API MCP Server (Complete Version)

完整版本的MCP服务器，集成所有CapCut API接口
"""

import sys
import os
import traceback
import io
import contextlib
from typing import Any, Dict

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入CapCut API功能
try:
    from add_audio_track import add_audio_track
    from add_image_impl import add_image_impl
    from add_subtitle_impl import add_subtitle_impl
    from add_sticker_impl import add_sticker_impl
    from add_video_keyframe_impl import add_video_keyframe_impl
    from pyJianYingDraft.text_segment import TextStyleRange, Text_style, Text_border
    from util import hex_to_rgb
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
                "height": {"type": "integer", "default": 1920, "description": "视频高度"},
                "name": {"type": "string", "description": "草稿名称"},
                "framerate": {"type": "string", "description": "帧率（可选值30.0、50.0、60.0）", "enum": ["30.0", "50.0", "60.0"], "default": "30.0"}
            },
            "required": ["width", "height"]
        }
    },
    {
        "name": "add_video",
        "description": "添加视频素材到草稿时间线。支持素材裁剪、转场效果、蒙版遮罩、背景模糊等高级视频编辑功能。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "video_url": {"type": "string", "description": "视频素材文件的URL地址或本地文件路径"},
                "start": {"type": "number", "default": 0, "description": "【素材裁剪-入点】从原始视频素材的第几秒开始截取。例如：2.5表示从素材的2.5秒位置开始裁剪"},
                "end": {"type": "number", "default": 0, "description": "【素材裁剪-出点】到原始视频素材的第几秒结束截取。0表示截取到素材末尾。例如：5.0表示裁剪到素材的5秒位置"},
                "target_start": {"type": "number", "default": 0, "description": "【时间线位置】该视频片段在成片时间线上的起始时间点（秒）。例如：10.0表示这段视频从成片的第10秒开始播放"},
                "width": {"type": "integer", "default": 1080, "description": "画布宽度（像素）。标准竖屏：1080，标准横屏：1920"},
                "height": {"type": "integer", "default": 1920, "description": "画布高度（像素）。标准竖屏：1920，标准横屏：1080"},
                "draft_id": {"type": "string", "description": "目标草稿的唯一标识符"},
                "transform_x": {"type": "number", "default": 0, "description": "【空间定位-X轴】视频素材在画布上的水平位置偏移。单位：半个画布宽度。0为画布中心，-1为向左偏移半个画布宽（画布最左侧），1为向右偏移半个画布宽（画布最右侧），2为向右偏移整个画布宽"},
                "transform_y": {"type": "number", "default": 0, "description": "【空间定位-Y轴】视频素材在画布上的垂直位置偏移。单位：半个画布高度。0为画布中心，-1为向上偏移半个画布高（画布顶部），1为向下偏移半个画布高（画布底部）。参考：字幕常用-0.8"},
                "scale_x": {"type": "number", "default": 1, "description": "【缩放-X轴】水平缩放倍数。1.0为原始大小，0.5为缩小一半，2.0为放大两倍"},
                "scale_y": {"type": "number", "default": 1, "description": "【缩放-Y轴】垂直缩放倍数。1.0为原始大小，0.5为缩小一半，2.0为放大两倍"},
                "speed": {"type": "number", "default": 1.0, "description": "视频播放速率。范围：0.1-100。1.0为正常速度，2.0为2倍速（加速），0.5为0.5倍速（慢动作）"},
                "track_name": {"type": "string", "default": "video_main", "description": "轨道名称标识。建议命名：video_main（主视频轨）、video_pip（画中画轨）、video_overlay（叠加轨）"},
                "relative_index": {"type": "integer", "default": 0, "description": "同轨道内素材的相对排序索引。0为最早，数值越大越靠后。用于精确控制素材在轨道内的前后顺序"},
                "intro_animation": {"type": "string", "description": "入场动画效果名称。素材出现时的动画效果，需与系统支持的动画类型匹配"},
                "intro_animation_duration": {"type": "number", "default": 0.5, "description": "入场动画持续时长（秒）。建议范围：0.3-2.0秒"},
                "outro_animation": {"type": "string", "description": "出场动画效果名称。素材消失时的动画效果，需与系统支持的动画类型匹配"},
                "outro_animation_duration": {"type": "number", "default": 0.5, "description": "出场动画持续时长（秒）。建议范围：0.3-2.0秒"},
                "combo_animation": {"type": "string", "description": "组合动画效果名称。同时包含入场和出场的预设动画组合"},
                "combo_animation_duration": {"type": "number", "default": 0.5, "description": "组合动画总持续时长（秒）。会平均分配给入场和出场"},
                "duration": {"type": ["number", "null"], "default": None, "description": "【性能优化】原始视频素材的总时长（秒）。提前提供可避免重复解析素材，显著提升处理速度。null表示自动检测"},
                "transition": {"type": "string", "description": "转场效果类型名称。应用于当前素材与前一个素材之间的过渡效果，需与系统支持的转场类型匹配"},
                "transition_duration": {"type": "number", "default": 0.5, "description": "转场效果持续时长（秒）。建议范围：0.3-2.0秒。转场会占用前后两个素材各一半的时长"},
                "volume": {"type": "number", "default": 1.0, "description": "视频原声音量增益。范围：0.0-2.0。0.0为静音，1.0为原始音量，2.0为放大两倍"},
                "filter_type": {"type": "string", "description": "滤镜效果类型名称。应用的颜色滤镜或风格化效果，需与系统支持的滤镜类型匹配"},
                "filter_intensity": {"type": "number", "default": 100.0, "description": "滤镜效果强度。范围：0-100。0为无效果，100为最大强度"},
                "fade_in_duration": {"type": "number", "default": 0.0, "description": "音频淡入时长（秒）。视频开始时音量从0逐渐增加到设定值的过渡时间"},
                "fade_out_duration": {"type": "number", "default": 0.0, "description": "音频淡出时长（秒）。视频结束时音量从设定值逐渐减少到0的过渡时间"},
                "mask_type": {"type": "string", "description": "蒙版形状类型。可选：circle（圆形）、rectangle（矩形）、heart（心形）等，需与系统支持的蒙版类型匹配"},
                "mask_center_x": {"type": "number", "default": 0.5, "description": "【歧义警告】蒙版中心点-X坐标。代码逻辑显示应输入像素值(例如1080px宽画布的中心应输入540),但示例代码使用0.5表示居中,与内部转换公式center_x/(画布宽/2)矛盾。建议:按归一化使用(0.0=最左,0.5=中心,1.0=最右),或测试后根据实际效果调整"},
                "mask_center_y": {"type": "number", "default": 0.5, "description": "【歧义警告】蒙版中心点-Y坐标。代码逻辑显示应输入像素值(例如1920px高画布的中心应输入960),但示例代码使用0.5表示居中,与内部转换公式center_y/(画布高/2)矛盾。建议:按归一化使用(0.0=最上,0.5=中心,1.0=最下),或测试后根据实际效果调整"},
                "mask_size": {"type": "number", "default": 1.0, "description": "蒙版主尺寸大小。归一化比例：0.0为不可见，1.0为覆盖整个画布，支持超过1.0"},
                "mask_rotation": {"type": "number", "default": 0.0, "description": "蒙版旋转角度（度）。范围：0-360。顺时针旋转"},
                "mask_feather": {"type": "number", "default": 0.0, "description": "蒙版边缘羽化程度。范围：0.0-1.0。0.0为锐利边缘，1.0为最大柔化"},
                "mask_invert": {"type": "boolean", "default": False, "description": "是否反转蒙版。false：显示蒙版内部区域，true：显示蒙版外部区域"},
                "mask_rect_width": {"type": ["number", "null"], "default": None, "description": "【矩形蒙版专用】矩形宽度。归一化比例：1.0为画布宽度。仅当mask_type为rectangle时有效"},
                "mask_round_corner": {"type": ["number", "null"], "default": None, "description": "【矩形蒙版专用】矩形圆角半径。范围：0-100。0为直角，100为最圆润。仅当mask_type为rectangle时有效"},
                "background_blur": {"type": "integer", "description": "背景模糊强度等级。范围：1-4。1为轻微模糊，4为最强模糊。用于创建素材周围的虚化背景效果"}
            },
            "required": ["video_url", "draft_id"]
        }
    },
    {
        "name": "add_audio",
        "description": "添加音频轨道到草稿时间线。支持音频裁剪、音效处理、音量控制、变速等功能。可用于背景音乐、配音、音效等场景。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "audio_url": {"type": "string", "description": "音频素材文件的URL地址或本地文件路径。支持常见音频格式：mp3、wav、aac、m4a等"},
                "draft_id": {"type": "string", "description": "目标草稿的唯一标识符"},
                "start": {"type": "number", "default": 0, "description": "【素材裁剪-入点】从原始音频素材的第几秒开始截取。对应source_timerange的起始位置。例如：2.5表示从素材的2.5秒位置开始裁剪"},
                "end": {"type": "number", "description": "【素材裁剪-出点】到原始音频素材的第几秒结束截取。不设置则截取到素材末尾。对应source_timerange的结束位置。例如：5.0表示裁剪到素材的5秒位置"},
                "target_start": {"type": "number", "default": 0, "description": "【时间线位置】该音频片段在成片时间线上的起始时间点（秒）。对应target_timerange的起始位置。例如：10.0表示这段音频从成片的第10秒开始播放"},
                "volume": {"type": "number", "default": 1.0, "description": "音量增益倍数。范围：0.0-2.0（实现中为0.0-1.0，但支持>1.0）。0.0为静音，1.0为原始音量，>1.0为放大"},
                "speed": {"type": "number", "default": 1.0, "description": "音频播放速率。范围：0.1-100（理论值）。1.0为正常速度，2.0为2倍速（加速），0.5为0.5倍速（减速）。影响最终片段时长：target_duration = source_duration / speed"},
                "track_name": {"type": "string", "default": "audio_main", "description": "音频轨道名称标识。建议命名：audio_main（主背景音乐）、audio_voice（人声配音）、audio_sfx（音效轨）。会自动创建不存在的轨道"},
                "duration": {"type": ["number", "null"], "default": None, "description": "【性能优化】原始音频素材的总时长（秒）。提前提供可避免重复解析素材，显著提升处理速度。null表示使用默认值0.0，实际时长在下载时获取"},
                "effect_type": {"type": "string", "description": "音效处理类型名称。根据IS_CAPCUT_ENV自动选择：CapCut环境支持CapCutVoiceFiltersEffectType/CapCutVoiceCharactersEffectType/CapCutSpeechToSongEffectType；剪映环境支持AudioSceneEffectType/ToneEffectType/SpeechToSongType"},
                "effect_params": {"type": "array", "description": "音效参数数组。参数的具体含义和数量取决于effect_type。格式：List[Optional[float]]。例如：某些效果可能需要[0.5, 1.0]"},
                "width": {"type": "integer", "default": 1080, "description": "画布宽度（像素）。用于创建或匹配草稿尺寸，通常保持与视频画布一致"},
                "height": {"type": "integer", "default": 1920, "description": "画布高度（像素）。用于创建或匹配草稿尺寸，通常保持与视频画布一致"}
            },
            "required": ["audio_url", "draft_id"]
        }
    },
    {
        "name": "add_image",
        "description": "添加图片素材到草稿时间线。支持图片动画、转场效果、蒙版遮罩、背景模糊等视觉效果。适用于静态图片展示、照片墙、图片过渡等场景。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "image_url": {"type": "string", "description": "图片素材文件的URL地址或本地文件路径。支持常见图片格式：png、jpg、jpeg、webp等"},
                "draft_id": {"type": "string", "description": "目标草稿的唯一标识符"},
                "start": {"type": "number", "default": 0, "description": "【时间线位置-起点】图片在成片时间线上的起始时间点（秒）。对应target_timerange的起始位置。例如：0表示从成片开头开始显示"},
                "end": {"type": "number", "default": 3.0, "description": "【时间线位置-终点】图片在成片时间线上的结束时间点（秒）。对应target_timerange的结束位置。例如：3.0表示显示到成片的第3秒。图片显示时长 = end - start"},
                "width": {"type": "integer", "default": 1080, "description": "画布宽度（像素）。标准竖屏：1080，标准横屏：1920"},
                "height": {"type": "integer", "default": 1920, "description": "画布高度（像素）。标准竖屏：1920，标准横屏：1080"},
                "transform_x": {"type": "number", "default": 0, "description": "【空间定位-X轴】图片素材在画布上的水平位置偏移。单位：半个画布宽度。0为画布中心，-1为向左偏移半个画布宽，1为向右偏移半个画布宽"},
                "transform_y": {"type": "number", "default": 0, "description": "【空间定位-Y轴】图片素材在画布上的垂直位置偏移。单位：半个画布高度。0为画布中心，-1为向上偏移半个画布高，1为向下偏移半个画布高"},
                "scale_x": {"type": "number", "default": 1, "description": "【缩放-X轴】水平缩放倍数。1.0为原始大小，0.5为缩小一半，2.0为放大两倍"},
                "scale_y": {"type": "number", "default": 1, "description": "【缩放-Y轴】垂直缩放倍数。1.0为原始大小，0.5为缩小一半，2.0为放大两倍"},
                "track_name": {"type": "string", "default": "main", "description": "视频轨道名称标识。建议命名：main（主轨道）、overlay（叠加层）、background（背景层）。会自动创建不存在的轨道"},
                "relative_index": {"type": "integer", "default": 0, "description": "同轨道内素材的相对排序索引。0为最早，数值越大越靠后。用于精确控制素材在轨道内的前后顺序和Z轴层级"},
                "intro_animation": {"type": "string", "description": "入场动画效果名称。图片出现时的动画效果，需与系统支持的动画类型匹配。根据IS_CAPCUT_ENV自动选择CapCutIntroType或IntroType"},
                "intro_animation_duration": {"type": "number", "default": 0.5, "description": "入场动画持续时长（秒）。建议范围：0.3-2.0秒。单位会自动转换为微秒（×1e6）"},
                "outro_animation": {"type": "string", "description": "出场动画效果名称。图片消失时的动画效果，需与系统支持的动画类型匹配。根据IS_CAPCUT_ENV自动选择CapCutOutroType或OutroType"},
                "outro_animation_duration": {"type": "number", "default": 0.5, "description": "出场动画持续时长（秒）。建议范围：0.3-2.0秒。单位会自动转换为微秒（×1e6）"},
                "combo_animation": {"type": "string", "description": "组合动画效果名称。同时包含入场和出场的预设动画组合。根据IS_CAPCUT_ENV自动选择CapCutGroupAnimationType或GroupAnimationType"},
                "combo_animation_duration": {"type": "number", "default": 0.5, "description": "组合动画总持续时长（秒）。会平均分配给入场和出场。单位会自动转换为微秒（×1e6）"},
                "transition": {"type": "string", "description": "转场效果类型名称。应用于当前素材与前一个素材之间的过渡效果。根据IS_CAPCUT_ENV自动选择CapCutTransitionType或TransitionType"},
                "transition_duration": {"type": "number", "default": 0.5, "description": "转场效果持续时长（秒）。建议范围：0.3-2.0秒。转场会占用前后两个素材各一半的时长。单位会自动转换为微秒（×1e6）"},
                "mask_type": {"type": "string", "description": "蒙版形状类型。可选：Linear（线性）、Mirror（镜像）、Circle（圆形）、Rectangle（矩形）、Heart（心形）、Star（星形）。根据IS_CAPCUT_ENV自动选择CapCutMaskType或MaskType"},
                "mask_center_x": {"type": "number", "default": 0.0, "description": "【歧义警告】蒙版中心点-X坐标。代码逻辑显示应输入像素值,但转换公式center_x/(画布宽/2)与示例代码0.5=居中矛盾。建议:按归一化使用(0.0=画布最左,0.5=画布中心,1.0=画布最右),或测试后根据实际效果调整"},
                "mask_center_y": {"type": "number", "default": 0.0, "description": "【歧义警告】蒙版中心点-Y坐标。代码逻辑显示应输入像素值,但转换公式center_y/(画布高/2)与示例代码0.5=居中矛盾。建议:按归一化使用(0.0=画布最上,0.5=画布中心,1.0=画布最下),或测试后根据实际效果调整"},
                "mask_size": {"type": "number", "default": 0.5, "description": "蒙版主尺寸大小。表示为素材高度的比例。0.0为不可见，0.5为素材高度的一半，1.0为素材高度。支持超过1.0"},
                "mask_rotation": {"type": "number", "default": 0.0, "description": "蒙版旋转角度（度）。范围：0-360。顺时针旋转"},
                "mask_feather": {"type": "number", "default": 0.0, "description": "蒙版边缘羽化程度。范围：0.0-100.0。0.0为锐利边缘，100.0为最大柔化"},
                "mask_invert": {"type": "boolean", "default": False, "description": "是否反转蒙版。false：显示蒙版内部区域，true：显示蒙版外部区域"},
                "mask_rect_width": {"type": ["number", "null"], "default": None, "description": "【矩形蒙版专用】矩形宽度。表示为素材宽度的比例。例如：1.0为素材全宽。仅当mask_type为Rectangle时有效"},
                "mask_round_corner": {"type": ["number", "null"], "default": None, "description": "【矩形蒙版专用】矩形圆角半径。范围：0-100。0为直角，100为最圆润。仅当mask_type为Rectangle时有效"},
                "background_blur": {"type": "integer", "description": "背景模糊强度等级。范围：1-4。对应模糊值：1=0.0625（轻微），2=0.375（中等），3=0.75（强烈），4=1.0（最大）。用于创建素材周围的虚化背景效果"}
            },
            "required": ["image_url", "draft_id"]
        }
    },
    {
        "name": "add_text",
        "description": "添加文本字幕到草稿时间线。支持丰富的文本样式、描边、背景、阴影、入出场动画等。适用于字幕、标题、艺术字等场景。建议：艺术字可居中放置在显眼位置，常规字幕应选择清晰易读的字体。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "文本内容。支持多行文本"},
                "start": {"type": "number", "description": "【时间线位置-起点】文本在成片时间线上的起始时间点（秒）。对应trange的起始位置"},
                "end": {"type": "number", "description": "【时间线位置-终点】文本在成片时间线上的结束时间点（秒）。对应trange的结束位置。文本显示时长 = end - start"},
                "draft_id": {"type": "string", "description": "目标草稿的唯一标识符"},
                "track_name": {"type": "string", "default": "text_main", "description": "文本轨道名称标识。建议命名：text_main（主字幕轨）、text_title（标题轨）、text_caption（说明轨）。会自动创建不存在的轨道。必需参数"},
                "font": {"type": "string", "description": "字体名称。必须是FontType中支持的字体。不设置则使用null（系统默认字体）。必需参数"},
                "font_size": {"type": "number", "default": 8.0, "description": "字体大小。建议范围：4.0-20.0。数值越大字体越大"},
                "font_color": {"type": "string", "default": "#ffffff", "description": "字体颜色。十六进制格式：#RRGGBB。例如：#ffffff为白色，#000000为黑色。会自动转换为RGB元组"},
                "font_alpha": {"type": "number", "default": 1.0, "description": "字体透明度。范围：0.0-1.0。0.0为完全透明，1.0为完全不透明。有效性会被验证"},
                "transform_x": {"type": "number", "default": 0, "description": "【空间定位-X轴】文本在画布上的水平位置偏移。单位：半个画布宽度。0为画布中心，-1为向左偏移半个画布宽，1为向右偏移半个画布宽"},
                "transform_y": {"type": "number", "default": -0.8, "description": "【空间定位-Y轴】文本在画布上的垂直位置偏移。单位：半个画布高度。0为画布中心，-1为画布顶部，1为画布底部。默认-0.8表示屏幕底部位置（字幕常用，向上偏移0.4倍画布高）"},
                "align": {"type": "integer", "default": 1, "description": "文本对齐方式。0=左对齐，1=居中对齐，2=右对齐"},
                "vertical": {"type": "boolean", "default": False, "description": "是否垂直显示文本。false=水平文本，true=垂直文本"},
                "fixed_width": {"type": "number", "default": 0.7, "description": "文本框固定宽度比例。范围：0.0-1.0（相对画布宽度）。-1表示不固定宽度（自动适应）。默认0.7表示占画布宽度70%"},
                "fixed_height": {"type": "number", "default": -1, "description": "文本框固定高度比例。范围：0.0-1.0（相对画布高度）。-1表示不固定高度（自动适应）。会转换为像素值"},
                "border_alpha": {"type": "number", "default": 1.0, "description": "描边透明度。范围：0.0-1.0。0.0为完全透明，1.0为完全不透明。有效性会被验证"},
                "border_color": {"type": "string", "default": "#000000", "description": "描边颜色。十六进制格式：#RRGGBB。例如：#000000为黑色。会自动转换为RGB元组"},
                "border_width": {"type": "number", "default": 0.0, "description": "描边宽度。0.0表示无描边。大于0时会创建Text_border对象"},
                "background_color": {"type": "string", "default": "#000000", "description": "背景颜色。十六进制格式：#RRGGBB"},
                "background_style": {"type": "integer", "default": 1, "description": "背景样式类型。具体样式需与实现支持的样式匹配"},
                "background_alpha": {"type": "number", "default": 0.0, "description": "背景透明度。范围：0.0-1.0。0.0为无背景（默认），1.0为完全不透明。大于0时会创建Text_background对象。有效性会被验证"},
                "background_round_radius": {"type": "number", "default": 0.0, "description": "背景圆角半径。范围：0.0-1.0。0.0为直角，1.0为最圆"},
                "background_height": {"type": "number", "default": 0.14, "description": "背景高度比例。范围：0.0-1.0（相对画布高度）"},
                "background_width": {"type": "number", "default": 0.14, "description": "背景宽度比例。范围：0.0-1.0（相对画布宽度）"},
                "background_horizontal_offset": {"type": "number", "default": 0.5, "description": "背景水平偏移。范围：0.0-1.0。0.5表示居中"},
                "background_vertical_offset": {"type": "number", "default": 0.5, "description": "背景垂直偏移。范围：0.0-1.0。0.5表示居中"},
                "shadow_enabled": {"type": "boolean", "default": False, "description": "是否启用阴影效果。true时会创建Text_shadow对象"},
                "shadow_alpha": {"type": "number", "default": 0.9, "description": "阴影透明度。范围：0.0-1.0。建议值：0.7-0.9"},
                "shadow_angle": {"type": "number", "default": -45.0, "description": "阴影投射角度。范围：-180.0至180.0（度）。-45表示左上方"},
                "shadow_color": {"type": "string", "default": "#000000", "description": "阴影颜色。十六进制格式：#RRGGBB"},
                "shadow_distance": {"type": "number", "default": 5.0, "description": "阴影距离。数值越大阴影越远"},
                "shadow_smoothing": {"type": "number", "default": 0.15, "description": "阴影平滑度（模糊程度）。范围：0.0-1.0。0.0为锐利，1.0为最柔和"},
                "intro_animation": {"type": "string", "description": "入场动画类型名称。文本出现时的动画效果。根据IS_CAPCUT_ENV自动选择CapCutTextIntro或TextIntro"},
                "intro_duration": {"type": "number", "default": 0.5, "description": "入场动画持续时长（秒）。单位会自动转换为微秒（×1e6）"},
                "outro_animation": {"type": "string", "description": "出场动画类型名称。文本消失时的动画效果。根据IS_CAPCUT_ENV自动选择CapCutTextOutro或TextOutro"},
                "outro_duration": {"type": "number", "default": 0.5, "description": "出场动画持续时长（秒）。单位会自动转换为微秒（×1e6）"},
                "width": {"type": "integer", "default": 1080, "description": "画布宽度（像素）。标准竖屏：1080，标准横屏：1920"},
                "height": {"type": "integer", "default": 1920, "description": "画布高度（像素）。标准竖屏：1920，标准横屏：1080"},
                "italic": {"type": "boolean", "default": False, "description": "是否斜体。应用于Text_style。注意：与bold/underline可能存在互斥关系（取决于字体）"},
                "bold": {"type": "boolean", "default": False, "description": "是否加粗。应用于Text_style"},
                "underline": {"type": "boolean", "default": False, "description": "是否下划线。应用于Text_style"}
            },
            "required": ["text", "font", "start", "end", "track_name"]
        }
    },
    # {
    #     "name": "add_subtitle",
    #     "description": "添加字幕到草稿，支持SRT文件和样式设置",
    #     "inputSchema": {
    #         "type": "object",
    #         "properties": {
    #             "srt": {"type": "string", "description": "字幕内容或SRT文件URL（支持直接传字幕文本或文件路径/URL）"},
    #             "draft_id": {"type": "string", "description": "草稿ID（用于指定要添加字幕的草稿）"},
    #             "time_offset": {"type": "number", "default": 0.0, "description": "字幕时间偏移量（秒，可整体调整字幕显示时间）"},
    #             "font_size": {"type": "number", "default": 8.0, "description": "字体大小"},
    #             "font": {"type": "string", "description": "字体"},
    #             "bold": {"type": "boolean", "default": False, "description": "是否加粗"},
    #             "italic": {"type": "boolean", "default": False, "description": "是否斜体"},
    #             "underline": {"type": "boolean", "default": False, "description": "是否下划线"},
    #             "font_color": {"type": "string", "default": "#FFFFFF", "description": "字体颜色（支持十六进制色值）"},
    #             "align": {"type": "integer", "default": 1, "description": "对齐方式：0左 1中 2右"},
    #             "vertical": {"type": "boolean", "default": False, "description": "是否垂直显示"},
    #             "alpha": {"type": "number", "default": 1.0, "description": "字体透明度（范围0-1）"},
    #             "border_alpha": {"type": "number", "default": 1.0, "description": "边框透明度"},
    #             "border_color": {"type": "string", "default": "#000000", "description": "边框颜色"},
    #             "border_width": {"type": "number", "default": 0.0, "description": "边框宽度"},
    #             "background_color": {"type": "string", "default": "#000000", "description": "背景颜色"},
    #             "background_style": {"type": "integer", "default": 1, "description": "背景样式（需与实现支持的样式匹配）"},
    #             "background_alpha": {"type": "number", "default": 0.0, "description": "背景透明度"},
    #             "transform_x": {"type": "number", "default": 0.0, "description": "X轴位置偏移"},
    #             "transform_y": {"type": "number", "default": -0.8, "description": "Y轴位置偏移"},
    #             "scale_x": {"type": "number", "default": 1.0, "description": "X轴缩放比例"},
    #             "scale_y": {"type": "number", "default": 1.0, "description": "Y轴缩放比例"},
    #             "rotation": {"type": "number", "default": 0.0, "description": "旋转角度（度）"},
    #             "track_name": {"type": "string", "default": "subtitle", "description": "轨道名称"},
    #             "width": {"type": "integer", "default": 1080, "description": "画布宽度"},
    #             "height": {"type": "integer", "default": 1920, "description": "画布高度"}
    #         },
    #         "required": ["srt"]
    #     }
    # },
    {
        "name": "add_effect",
        "description": "添加视频特效到草稿时间线。支持场景特效和人物特效两大类。推荐开头使用的5种特效：冲刺、放大镜、逐渐放大、聚光灯、夸夸弹幕。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "effect_type": {"type": "string", "description": "特效类型名称。根据effect_category和IS_CAPCUT_ENV自动选择：scene分类使用VideoSceneEffectType或CapCutVideoSceneEffectType；character分类使用VideoCharacterEffectType或CapCutVideoCharacterEffectType"},
                "effect_category": {"type": "string", "default": "scene", "enum": ["scene", "character"], "description": "特效分类。scene=场景特效（如光效、粒子），character=人物特效（如美颜、变形）"},
                "start": {"type": "number", "default": 0, "description": "【时间线位置-起点】特效在成片时间线上的起始时间点（秒）。对应trange的起始位置"},
                "end": {"type": "number", "default": 3.0, "description": "【时间线位置-终点】特效在成片时间线上的结束时间点（秒）。对应trange的结束位置。特效显示时长 = end - start"},
                "draft_id": {"type": "string", "description": "目标草稿的唯一标识符。未传或不存在时自动创建新草稿"},
                "track_name": {"type": "string", "default": "effect_01", "description": "特效轨道名称标识。建议命名：effect_01、effect_scene、effect_character。会自动创建不存在的轨道"},
                "params": {"type": "array", "description": "特效参数数组。格式：List[Optional[float]]。参数的具体含义取决于effect_type。未提供或为None的参数项将使用默认值"},
                "width": {"type": "integer", "default": 1080, "description": "画布宽度（像素）。标准竖屏：1080，标准横屏：1920"},
                "height": {"type": "integer", "default": 1920, "description": "画布高度（像素）。标准竖屏：1920，标准横屏：1080"}
            },
            "required": ["effect_type"]
        }
    },
    {
        "name": "add_sticker",
        "description": "添加贴纸到草稿时间线。支持位置、缩放、旋转、透明度、翻转等变换。适用于装饰、表情、图标等场景。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "resource_id": {"type": "string", "description": "贴纸资源的唯一标识符。需要从系统资源库获取有效的resource_id"},
                "draft_id": {"type": "string", "description": "目标草稿的唯一标识符"},
                "start": {"type": "number", "description": "【时间线位置-起点】贴纸在成片时间线上的起始时间点（秒）。对应trange的起始位置"},
                "end": {"type": "number", "description": "【时间线位置-终点】贴纸在成片时间线上的结束时间点（秒）。对应trange的结束位置。贴纸显示时长 = end - start"},
                "transform_x": {"type": "number", "default": 0, "description": "【空间定位-X轴】贴纸在画布上的水平位置偏移。单位：半个画布宽度。0为画布中心，-1为向左偏移半个画布宽，1为向右偏移半个画布宽"},
                "transform_y": {"type": "number", "default": 0, "description": "【空间定位-Y轴】贴纸在画布上的垂直位置偏移。单位：半个画布高度。0为画布中心，-1为向上偏移半个画布高，1为向下偏移半个画布高"},
                "scale_x": {"type": "number", "default": 1.0, "description": "【缩放-X轴】水平缩放倍数。1.0为原始大小，0.5为缩小一半，2.0为放大两倍"},
                "scale_y": {"type": "number", "default": 1.0, "description": "【缩放-Y轴】垂直缩放倍数。1.0为原始大小，0.5为缩小一半，2.0为放大两倍"},
                "alpha": {"type": "number", "default": 1.0, "description": "贴纸透明度。范围：0.0-1.0。0.0为完全透明，1.0为完全不透明"},
                "rotation": {"type": "number", "default": 0.0, "description": "贴纸旋转角度（度）。顺时针旋转，可以是正值或负值"},
                "track_name": {"type": "string", "default": "sticker_main", "description": "贴纸轨道名称标识。建议命名：sticker_main、sticker_emoji、sticker_decoration。会自动创建不存在的轨道"},
                "width": {"type": "integer", "default": 1080, "description": "画布宽度（像素）。标准竖屏：1080，标准横屏：1920"},
                "height": {"type": "integer", "default": 1920, "description": "画布高度（像素）。标准竖屏：1920，标准横屏：1080"}
            },
            "required": ["resource_id", "start", "end", "draft_id"]
        }
    },
    {
        "name": "add_video_keyframe",
        "description": "添加视频关键帧动画。支持位置、缩放、旋转、透明度、饱和度、对比度、亮度、音量等属性的关键帧动画。可实现平滑的属性变化效果。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "draft_id": {"type": "string", "description": "目标草稿的唯一标识符"},
                "track_name": {"type": "string", "default": "main", "description": "视频轨道名称。指定要添加关键帧的轨道"},
                "property_type": {"type": "string", "description": "【单个模式】关键帧属性类型。可选值：position_x（X位置）、position_y（Y位置）、rotation（旋转）、scale_x（X缩放）、scale_y（Y缩放）、uniform_scale（统一缩放）、alpha（透明度）、saturation（饱和度）、contrast（对比度）、brightness（亮度）、volume（音量）"},
                "time": {"type": "number", "default": 0.0, "description": "【单个模式】关键帧时间点（秒）。在时间线上的绝对时间位置"},
                "value": {"type": "string", "description": "【单个模式】关键帧值。具体格式取决于property_type。例如：位置可能是数值，颜色可能是#RRGGBB"},
                "property_types": {"type": "array", "description": "【批量模式】关键帧属性类型列表。与times和values一一对应，用于批量添加多个关键帧"},
                "times": {"type": "array", "description": "【批量模式】关键帧时间点列表（秒）。与property_types和values一一对应"},
                "values": {"type": "array", "description": "【批量模式】关键帧值列表。与property_types和times一一对应"}
            },
            "required": ["draft_id", "track_name"]
        }
    },
    {
        "name": "generate_video",
        "description": "导出草稿为视频文件。将编辑好的草稿渲染成最终的视频文件，支持多种分辨率和帧率配置。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "draft_id": {"type": "string", "description": "要导出的草稿的唯一标识符"},
                "resolution": {"type": "string", "enum": ["1080P", "2K", "4K"], "description": "导出视频分辨率。1080P=1920×1080，2K=2560×1440，4K=3840×2160", "default": "1080P"},
                "framerate": {"type": "string", "enum": ["30fps", "50fps", "60fps"], "description": "导出视频帧率。30fps适合常规视频，50/60fps适合高动态画面", "default": "30fps"},
                "name": {"type": "string", "description": "导出视频的文件名称（不含扩展名）"}
            },
            "required": ["draft_id"]
        }
    },
    {
        "name": "get_font_types",
        "description": "获取系统支持的字体类型列表。返回FontType枚举中所有可用的字体名称，用于add_text的font参数。",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "get_audio_effect_types",
        "description": "获取系统支持的音频特效类型列表。返回AudioSceneEffectType、ToneEffectType、SpeechToSongType等枚举中的音效名称，用于add_audio的effect_type参数。",
        "inputSchema": {
            "type": "object",
            "properties": {}
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
            start_idx = style_dict.get("start", 0)
            end_idx = style_dict.get("end", 0)

            style_obj = style_dict.get("style", {})
            border_obj = style_dict.get("border")
            font_str = style_dict.get("font")

            # 构建 Text_style
            text_style = Text_style(
                size=style_obj.get("size", 8.0),
                bold=style_obj.get("bold", False),
                italic=style_obj.get("italic", False),
                underline=style_obj.get("underline", False),
                color=hex_to_rgb(style_obj.get("color", "#FFFFFF")),
                alpha=1.0,
                align=1,
                vertical=False,
                letter_spacing=0,
                line_spacing=0,
            )

            # 构建 Text_border（可选）
            text_border = None
            if border_obj:
                text_border = Text_border(
                    alpha=border_obj.get("alpha", 1.0),
                    color=hex_to_rgb(border_obj.get("color", "#000000")),
                    width=border_obj.get("width", 0.0)
                )

            style_range = TextStyleRange(
                start=start_idx,
                end=end_idx,
                style=text_style,
                border=text_border,
                font_str=font_str
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
        with capture_stdout():                          
            if tool_name == "add_audio":
                # 将 effect_type/effect_params 映射为实现所需的 sound_effects
                effect_type = arguments.pop("effect_type", None)
                effect_params = arguments.pop("effect_params", None)
                if effect_type:
                    if effect_params is None:
                        effect_params = []
                    # 如果已存在 sound_effects，追加；否则创建
                    existing_effects = arguments.get("sound_effects")
                    if existing_effects:
                        existing_effects.append((effect_type, effect_params))
                    else:
                        arguments["sound_effects"] = [(effect_type, effect_params)]
                result = add_audio_track(**arguments)
                
            elif tool_name == "add_image":
                result = add_image_impl(**arguments)

            elif tool_name == "add_subtitle":
                # 兼容字段：将 srt 映射为实现参数 srt_path
                if "srt" in arguments and "srt_path" not in arguments:
                    arguments["srt_path"] = arguments.pop("srt")
                result = add_subtitle_impl(**arguments)
                
            elif tool_name == "add_sticker":
                result = add_sticker_impl(**arguments)
                
            elif tool_name == "add_video_keyframe":
                result = add_video_keyframe_impl(**arguments)

            else:
                return {"success": False, "error": f"Unknown tool: {tool_name}"}
        
        return {
            "success": True,
            "result": result
        }
        
    except Exception as e:
        print(f"[ERROR] Tool execution error: {e}", file=sys.stderr)
        print(f"[ERROR] Traceback: {traceback.format_exc()}", file=sys.stderr)
        return {"success": False, "error": str(e)}
