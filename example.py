import requests
import json
import sys
import time
from settings.local import PORT
from util import timing_decorator
import functools
import threading
from pyJianYingDraft.text_segment import TextStyleRange, Text_style, Text_border
from util import hex_to_rgb

import shutil
import os

# Base URL of the service, please modify according to actual situation
BASE_URL = f"http://localhost:{PORT}"
LICENSE_KEY = "trial"  # Trial license key

CAPCUT_DRAFT_FOLDER = "/Users/sunguannan/Movies/CapCut/User Data/Projects/com.lveditor.draft"
JIANYINGPRO_DRAFT_FOLDER = "/Users/sunguannan/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"

def make_request(endpoint, data, method='POST'):
    """Send HTTP request to the server and handle the response"""
    url = f"{BASE_URL}/{endpoint}"
    headers = {'Content-Type': 'application/json'}
    
    try:
        if method == 'POST':
            response = requests.post(url, data=json.dumps(data), headers=headers)
        elif method == 'GET':
            response = requests.get(url, params=data, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
            
        response.raise_for_status()  # Raise an exception if the request fails
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Unable to parse server response")
        sys.exit(1)

def add_audio_track(audio_url, start, end, target_start, volume=1.0, 
                    speed=1.0, track_name="main_audio", effect_type=None, effect_params=None, draft_id=None):
    """API call to add audio track"""
    data = {
        "audio_url": audio_url,
        "start": start,
        "end": end,
        "target_start": target_start,
        "volume": volume,
        "speed": speed,
        "track_name": track_name,
        "effect_type": effect_type,
        "effect_params": effect_params
    }
    
    if draft_id:
        data["draft_id"] = draft_id
        
    return make_request("add_audio", data)

def add_text_impl(text, start, end, font, font_color, font_size, track_name, draft_folder="123", draft_id=None,
                  vertical=False, transform_x=0, transform_y=0, font_alpha=1.0,
                  border_color=None, border_width=0.0, border_alpha=1.0,
                  background_color=None, background_alpha=1.0, background_style=None,
                  background_round_radius=0.0, background_height=0.14, background_width=0.14,
                  background_horizontal_offset=0.5, background_vertical_offset=0.5,
                  shadow_enabled=False, shadow_alpha=0.9, shadow_angle=-45.0,
                  shadow_color="#000000", shadow_distance=5.0, shadow_smoothing=0.15,
                  bubble_effect_id=None, bubble_resource_id=None,
                  effect_effect_id=None, 
                  intro_animation=None, intro_duration=0.5,
                  outro_animation=None, outro_duration=0.5,
                  width=1080, height=1920,
                  fixed_width=-1, fixed_height=-1,
                  text_styles=None):
    """Add text with support for multiple styles, shadows, and backgrounds"""
    data = {
        "draft_folder": draft_folder,
        "text": text,
        "start": start,
        "end": end,
        "font": font,
        "font_color": font_color,
        "font_size": font_size,
        "alpha": font_alpha,
        "track_name": track_name,
        "vertical": vertical,
        "transform_x": transform_x,
        "transform_y": transform_y
    }
    
    # Add border parameters
    if border_color:
        data["border_color"] = border_color
        data["border_width"] = border_width
        data["border_alpha"] = border_alpha
    
    # Add background parameters
    if background_color:
        data["background_color"] = background_color
        data["background_alpha"] = background_alpha
        if background_style:
            data["background_style"] = background_style
        data["background_round_radius"] = background_round_radius
        data["background_height"] = background_height
        data["background_width"] = background_width
        data["background_horizontal_offset"] = background_horizontal_offset
        data["background_vertical_offset"] = background_vertical_offset
    
    # Add shadow parameters
    if shadow_enabled:
        data["shadow_enabled"] = shadow_enabled
        data["shadow_alpha"] = shadow_alpha
        data["shadow_angle"] = shadow_angle
        data["shadow_color"] = shadow_color
        data["shadow_distance"] = shadow_distance
        data["shadow_smoothing"] = shadow_smoothing
    
    
    # Add bubble effect parameters
    if bubble_effect_id:
        data["bubble_effect_id"] = bubble_effect_id
        if bubble_resource_id:
            data["bubble_resource_id"] = bubble_resource_id
    
    # Add text effect parameters
    if effect_effect_id:
        data["effect_effect_id"] = effect_effect_id
    
    # Add intro animation parameters
    if intro_animation:
        data["intro_animation"] = intro_animation
        data["intro_duration"] = intro_duration
    
    # Add outro animation parameters
    if outro_animation:
        data["outro_animation"] = outro_animation
        data["outro_duration"] = outro_duration
    
    # Add size parameters
    data["width"] = width
    data["height"] = height
    
    # Add fixed size parameters
    if fixed_width > 0:
        data["fixed_width"] = fixed_width
    if fixed_height > 0:
        data["fixed_height"] = fixed_height
    
    if draft_id:
        data["draft_id"] = draft_id
    
    # Add text styles parameters
    if text_styles:
        data["text_styles"] = text_styles

    if draft_id:
        data["draft_id"] = draft_id
        
    return make_request("add_text", data)

def add_image_impl(image_url, start, end, width=None, height=None, track_name="image_main", draft_id=None,
                  transform_x=0, transform_y=0, scale_x=1.0, scale_y=1.0, transition=None, transition_duration=None,
                  mask_type=None, mask_center_x=0.0, mask_center_y=0.0, mask_size=0.5,
                  mask_rotation=0.0, mask_feather=0.0, mask_invert=False,
                  mask_rect_width=None, mask_round_corner=None, background_blur=None):
    """API call to add image"""
    data = {
        "image_url": image_url,
        "width": width,
        "height": height,
        "start": start,
        "end": end,
        "track_name": track_name,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "transition": transition,
        "transition_duration": transition_duration or 0.5,  # Default transition duration is 0.5 seconds
        # Add mask-related parameters
        "mask_type": mask_type,
        "mask_center_x": mask_center_x,
        "mask_center_y": mask_center_y,
        "mask_size": mask_size,
        "mask_rotation": mask_rotation,
        "mask_feather": mask_feather,
        "mask_invert": mask_invert,
        "mask_rect_width": mask_rect_width,
        "mask_round_corner": mask_round_corner
    }
    
    if draft_id:
        data["draft_id"] = draft_id
    if background_blur:
        data["background_blur"] = background_blur
        
    return make_request("add_image", data)

def generate_image_impl(prompt, width, height, start, end, track_name, draft_id=None,
                  transform_x=0, transform_y=0, scale_x=1.0, scale_y=1.0, transition=None, transition_duration=None):
    """API call to add image"""
    data = {
        "prompt": prompt,
        "width": width,
        "height": height,
        "start": start,
        "end": end,
        "track_name": track_name,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "transition": transition,
        "transition_duration": transition_duration or 0.5  # Default transition duration is 0.5 seconds
    }
    
    if draft_id:
        data["draft_id"] = draft_id
        
    return make_request("generate_image", data)

def add_sticker_impl(resource_id, start, end, draft_id=None, transform_x=0, transform_y=0,
                    alpha=1.0, flip_horizontal=False, flip_vertical=False, rotation=0.0,
                    scale_x=1.0, scale_y=1.0, track_name="sticker_main", relative_index=0,
                    width=1080, height=1920):
    """API call to add sticker"""
    data = {
        "sticker_id": resource_id,
        "start": start,
        "end": end,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "alpha": alpha,
        "flip_horizontal": flip_horizontal,
        "flip_vertical": flip_vertical,
        "rotation": rotation,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "track_name": track_name,
        "relative_index": relative_index,
        "width": width,
        "height": height
    }
    
    if draft_id:
        data["draft_id"] = draft_id
        
    return make_request("add_sticker", data)

def add_video_keyframe_impl(draft_id, track_name, property_type=None, time=None, value=None, 
                           property_types=None, times=None, values=None):
    """API call to add video keyframe
    
    Supports two modes:
    1. Single keyframe: using property_type, time, value parameters
    2. Batch keyframes: using property_types, times, values parameters (in list form)
    """
    data = {
        "draft_id": draft_id,
        "track_name": track_name
    }
    
    # Add single keyframe parameters (if provided)
    if property_type is not None:
        data["property_type"] = property_type
    if time is not None:
        data["time"] = time
    if value is not None:
        data["value"] = value
    
    # Add batch keyframe parameters (if provided)
    if property_types is not None:
        data["property_types"] = property_types
    if times is not None:
        data["times"] = times
    if values is not None:
        data["values"] = values
    
    return make_request("add_video_keyframe", data)

def add_video_impl(video_url, start=None, end=None, width=None, height=None, track_name="main",
                   draft_id=None, transform_y=0, scale_x=1, scale_y=1, transform_x=0,
                   speed=1.0, target_start=0, relative_index=0, transition=None, transition_duration=None,
                   # Mask-related parameters
                   mask_type=None, mask_center_x=0.5, mask_center_y=0.5, mask_size=1.0,
                   mask_rotation=0.0, mask_feather=0.0, mask_invert=False,
                   mask_rect_width=None, mask_round_corner=None, background_blur=None):
    """API call to add video track"""
    data = {
        "video_url": video_url,
        "height": height,
        "draft_id": draft_id,
        "track_name": track_name,
        "transform_y": transform_y,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "transform_x": transform_x,
        "speed": speed,
        "target_start": target_start,
        "relative_index": relative_index,
        "transition": transition,
        "transition_duration": transition_duration or 0.5,  # Default transition duration is 0.5 seconds
        # Mask-related parameters
        "mask_type": mask_type,
        "mask_center_x": mask_center_x,
        "mask_center_y": mask_center_y,
        "mask_size": mask_size,
        "mask_rotation": mask_rotation,
        "mask_feather": mask_feather,
        "mask_invert": mask_invert,
        "mask_rect_width": mask_rect_width,
        "mask_round_corner": mask_round_corner
    }
    if start:
        data["start"] = start
    if end:
        data["end"] = end
    if width:
        data["width"] = width
    if height:
        data["height"] = height
    if background_blur:
        data["background_blur"] = background_blur
    return make_request("add_video", data)

def add_effect(effect_type, start, end, draft_id=None, track_name="effect_01",
              params=None, width=1080, height=1920, effect_category=None):
    """API call to add effect"""
    data = {
        "effect_type": effect_type,
        "start": start,
        "end": end,
        "track_name": track_name,
        "params": params or [],
        "width": width,
        "height": height
    }
    
    if effect_category:
        data["effect_category"] = effect_category
    
    if draft_id:
        data["draft_id"] = draft_id
        
    return make_request("add_effect", data)

def test_effect_01():
    """Test adding effect service"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    
    print("\nTest: Adding effect")
    effect_result = add_effect(
        start=0,
        end=5,
        track_name="effect_01",
        # effect_type="金粉闪闪",  # Example using glow effect
        effect_type="Gold_Sparkles",
        params=[100, 50, 34]  # Example parameters, depending on the specific effect type
    )
    print(f"Effect adding result: {effect_result}")
    print(save_draft_impl(effect_result['output']['draft_id'], draft_folder))
    
    # If needed, you can add other test cases here
    
    # Return the first test result for subsequent operations (if any)
    return effect_result


def test_effect_02():
    """Test service for adding effects"""
    # draft_folder = "/Users/sunguannan/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"
    draft_folder = "/Users/sunguannan/Movies/CapCut/User Data/Projects/com.lveditor.draft"
    
    print("\nTest: Adding effects")
    # First add video track
    image_result = add_video_impl(
        video_url="https://pan.superbed.cn/share/1nbrg1fl/jimeng_daweidai.mp4",
        start=0,
        end=3.0,
        target_start=0,
        width=1080,
        height=1920
    )
    print(f"Video added successfully! {image_result['output']['draft_id']}")
    image_result = add_video_impl(
        video_url="https://pan.superbed.cn/share/1nbrg1fl/jimeng_daweidai.mp4",
        draft_id=image_result['output']['draft_id'],
        start=0,
        end=3.0,
        target_start=3,
    )
    print(f"Video added successfully! {image_result['output']['draft_id']}")
    
    # Then add effect
    effect_result = add_effect(
        effect_type="Like",
        effect_category="character",  # Explicitly specify as character effect
        start=3,
        end=6,
        draft_id=image_result['output']['draft_id'],
        track_name="effect_01"
    )
    print(f"Effect adding result: {effect_result}")
    print(save_draft_impl(effect_result['output']['draft_id'], draft_folder))
    
    source_folder = os.path.join(os.getcwd(), effect_result['output']['draft_id'])
    destination_folder = os.path.join(draft_folder, effect_result['output']['draft_id'])
    
    if os.path.exists(source_folder):
        print(f"Moving {effect_result['output']['draft_id']} to {draft_folder}")
        shutil.move(source_folder, destination_folder)
        print("Folder moved successfully!")
    else:
        print(f"Source folder {source_folder} does not exist")
    
    # Add log to prompt user to find the draft in CapCut
    print(f"\n===== IMPORTANT =====\nPlease open CapCut and find the draft named '{effect_result['output']['draft_id']}'\n======================")
    
    # Return the first test result for subsequent operations (if any)
    return effect_result

def test_text():
    """Test adding text with various features"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    # Test case 1: Basic text addition
    print("\nTest: Adding basic text")
    text_result = add_text_impl(
        text="Hello, I am CapCut Assistant",
        start=0,
        end=3,
        font="思源中宋",
        font_color="#FF0000",  # Red
        track_name="main_text",
        transform_y=0.8,
        transform_x=0.5,
        font_size=30.0
    )
    print("Test case 1 (Basic text) successful:", text_result)

    # Test case 2: Vertical text
    result2 = add_text_impl(
        draft_id=text_result['output']['draft_id'],
        text="Vertical text demo",
        start=3,
        end=6,
        font="云书法三行魏碑体",
        font_color="#00FF00",  # Green
        font_size=8.0,
        track_name="main_text",
        vertical=True,  # Enable vertical text
        transform_y=-0.5,
        outro_animation='Blur'
    )
    print("Test case 2 (Vertical text) successful:", result2)

    # Test case 3: Text with border and background
    result3 = add_text_impl(
        draft_id=result2['output']['draft_id'],
        text="Border and background test",
        start=6,
        end=9,
        font="思源中宋",
        font_color="#FFFFFF",  # White text
        font_size=24.0,
        track_name="main_text",
        transform_y=0.0,
        transform_x=0.5,
        border_color="#FF0000",  # Red border
        border_width=20.0,
        border_alpha=1.0,
        background_color="#0000FF",  # Blue background
        background_alpha=0.5,  # Semi-transparent background
        background_style=0  # Bubble style background
    )
    print("Test case 3 (Border and background) successful:", result3)
    
    # Test case 4: Text with shadow effect
    result4 = add_text_impl(
        draft_id=result3['output']['draft_id'],
        text="Shadow effect test",
        start=9,
        end=12,
        font="思源中宋",
        font_color="#FFFFFF",  # White text
        font_size=28.0,
        track_name="main_text",
        transform_y=-0.3,
        transform_x=0.5,
        shadow_enabled=True,  # Enable shadow
        shadow_alpha=0.8,
        shadow_angle=-30.0,
        shadow_color="#000000",  # Black shadow
        shadow_distance=8.0,
        shadow_smoothing=0.2
    )
    print("Test case 4 (Shadow effect) successful:", result4)
    
    # Test case 5: Multi-style text using TextStyleRange
    # Create different text styles
    style1 = {
        "start": 0,
        "end": 5,
        "style": {
            "color": "#FF0000",  # Red
            "size": 30,
            "bold": True
        },
        "border": {
            "color": "#FFFFFF",  # White border
            "width": 40,
            "alpha": 1.0
        },
        "font": "思源中宋"
    }
    
    style2 = {
        "start": 5,
        "end": 10,
        "style": {
            "color": "#00FF00",  # Green
            "size": 25,
            "italic": True
        },
        "font": "挥墨体"
    }
    
    style3 = {
        "start": 10,
        "end": 15,
        "style": {
            "color": "#0000FF",  # Blue
            "size": 20,
            "underline": True
        },
        "font": "金陵体"
    }
    
    # Add multi-style text
    result5 = add_text_impl(
        draft_id=result4['output']['draft_id'],
        text="Multi-style text test",
        start=12,
        end=15,
        font="思源粗宋",
        track_name="main_text",
        transform_y=0.3,
        transform_x=0.5,
        font_color="#000000",  # Default black
        font_size=20.0,
        # Use dictionary list instead of TextStyleRange object list
        text_styles=[style1, style2, style3]
    )
    print("Test case 5 (Multi-style text) successful:", result5)
    
    # Test case 6: Combined effects - shadow + background + multi-style
    combined_style1 = {
        "start": 0,
        "end": 8,
        "style": {
            "color": "#FFD700",  # Gold
            "size": 32,
            "bold": True
        },
        "border": {
            "color": "#8B4513",  # Brown border
            "width": 30,
            "alpha": 0.8
        },
        "font": "思源中宋"
    }
    
    combined_style2 = {
        "start": 8,
        "end": 16,
        "style": {
            "color": "#FF69B4",  # Hot pink
            "size": 28,
            "italic": True
        },
        "font": "挥墨体"
    }
    
    result6 = add_text_impl(
        draft_id=result5['output']['draft_id'],
        text="Combined effects demo",
        start=15,
        end=18,
        font="思源粗宋",
        track_name="main_text",
        transform_y=-0.6,
        transform_x=0.5,
        font_color="#FFFFFF",  # Default white
        font_size=24.0,
        # Background settings
        background_color="#4169E1",  # Royal blue background
        background_alpha=0.6,
        background_style=1,
        background_round_radius=0.3,
        background_height=0.18,
        background_width=0.8,
        # Shadow settings
        shadow_enabled=True,
        shadow_alpha=0.7,
        shadow_angle=-60.0,
        shadow_color="#2F4F4F",  # Dark slate gray shadow
        shadow_distance=6.0,
        shadow_smoothing=0.25,
        # Multi-style text
        text_styles=[combined_style1, combined_style2]
    )
    print("Test case 6 (Combined effects) successful:", result6)
    
    # Finally save and upload the draft
    if result6.get('success') and result6.get('output'):
        save_result = save_draft_impl(result6['output']['draft_id'], draft_folder)
        print(f"Draft save result: {save_result}")
    
    # Return the last test result for subsequent operations (if any)
    return result6


def test_text_02():
    """测试添加文本"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    # 测试用例1：基本文本添加
    print("\n测试：添加基本文本")
    text_result = add_text_impl(
        text="你好，我是剪映助手",
        start=0,
        end=3,
        font="思源中宋",
        font_color="#FF0000",  # 红色
        track_name="main_text",
        transform_y=0.8,
        transform_x=0.5,
        font_size=30.0
    )
    print("测试用例1（基本文本）成功:", text_result)

    # 测试用例2：竖排文本
    result2 = add_text_impl(
        draft_id=text_result['output']['draft_id'],
        text="竖排文本演示",
        start=3,
        end=6,
        font="云书法三行魏碑体",
        font_color="#00FF00",  # 绿色
        font_size=8.0,
        track_name="main_text",
        vertical=True,  # 启用竖排
        transform_y=-0.5,
        outro_animation='晕开'
    )
    print("测试用例2（竖排文本）成功:", result2)

    # 测试用例3：带描边和背景的文本
    result3 = add_text_impl(
        draft_id=result2['output']['draft_id'],
        text="描边和背景测试",
        start=6,
        end=9,
        font="思源中宋",
        font_color="#FFFFFF",  # 白色文字
        font_size=24.0,
        track_name="main_text",
        transform_y=0.0,
        transform_x=0.5,
        border_color="#FF0000",  # 红色描边
        border_width=20.0,
        border_alpha=1.0,
        background_color="#0000FF",  # 蓝色背景
        background_alpha=0.5,  # 半透明背景
        background_style=0  # 气泡样式背景
    )
    print("测试用例3（描边和背景）成功:", result3)
    
    # 测试用例4：使用 TextStyleRange 的多样式文本
    # 创建不同的文本样式
    style1 = {
        "start": 0,
        "end": 2,
        "style": {
            "color": "#FF0000",  # 红色
            "size": 30,
            "bold": True
        },
        "border": {
            "color": "#FFFFFF",  # 白色描边
            "width": 40,
            "alpha": 1.0
        },
        "font": "思源中宋"
    }
    
    style2 = {
        "start": 2,
        "end": 4,
        "style": {
            "color": "#00FF00",  # 绿色
            "size": 25,
            "italic": True
        },
        "font": "挥墨体"
    }
    
    style3 = {
        "start": 4,
        "end": 6,
        "style": {
            "color": "#0000FF",  # 蓝色
            "size": 20,
            "underline": True
        },
        "font": "金陵体"
    }
    
    # 添加多样式文本
    result4 = add_text_impl(
        draft_id=result3['output']['draft_id'],
        text="多样式\n文本测试",
        start=9,
        end=12,
        font="思源粗宋",
        track_name="main_text",
        transform_y=0.5,
        transform_x=0.5,
        font_color="#000000",  # 默认黑色
        font_size=20.0,
        # 使用字典列表而不是 TextStyleRange 对象列表
        text_styles=[style1, style2, style3]
    )
    print("测试用例4（多样式文本）成功:", result4)
    
    # 最后保存并上传草稿
    if result4.get('success') and result4.get('output'):
        save_result = save_draft_impl(result4['output']['draft_id'],draft_folder)
        print(f"草稿保存结果: {save_result}")
    
    # 返回最后一个测试结果用于后续操作（如果有的话）
    return result4


def test_text_03():
    """测试添加文本"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    # 测试用例1：基本文本添加
    print("\n测试：添加基本文本")
    text_result = add_text_impl(
        text="现在支持",
        start=0,
        end=6,
        font="挥墨体",
        font_color="#FFFFFF",  # 红色
        track_name="text_01",
        transform_y=0.58,
        transform_x=0,
        font_size=24.0,
        intro_animation="弹入",
        intro_duration=0.5
    )
    print("测试用例1（基本文本）成功:", text_result)

    # 测试用例2：带背景参数的文本
    result2 = add_text_impl(
        draft_id=text_result['output']['draft_id'],
        text="文字背景",
        start=1.5,
        end=6,
        font="思源中宋",
        font_color="#FFFFFF", 
        font_size=20.0,
        track_name="text_2",
        transform_y=0.15,
        transform_x=0,
        background_color="#0000FF",  # 蓝色背景
        background_alpha=0.7,  # 70%透明度
        background_style=1,  
        background_round_radius=0.5,  # 圆角半径
        background_height=0.2,  # 背景高度
        background_width=0.8,  # 背景宽度
        background_horizontal_offset=0.5,  # 水平居中
        background_vertical_offset=0.5,  # 垂直居中
        intro_animation="弹入",
        intro_duration=0.5
    )
    print("测试用例2（背景参数）成功:", result2)

    # 测试用例3：带阴影参数的文本
    result3 = add_text_impl(
        draft_id=result2['output']['draft_id'],
        text="文字阴影",
        start=3,
        end=6,
        font="金陵体",
        font_color="#FFFF00",  # 黄色文字
        font_size=25.0,
        track_name="text3",
        transform_y=-0.16,
        transform_x=0,
        shadow_enabled=True,  # 启用阴影
        shadow_alpha=0.8,  # 阴影透明度
        shadow_angle=-45.0,  # 阴影角度
        shadow_color="#0000FF",  # 蓝色阴影
        shadow_distance=10.0,  # 阴影距离
        shadow_smoothing=0.3,  # 阴影平滑度
        intro_animation="弹入",
        intro_duration=0.5
    )
    print("测试用例3（阴影参数）成功:", result3)
    
    # 测试用例4：带描边和背景的文本
    result4 = add_text_impl(
        draft_id=result3['output']['draft_id'],
        text="文字描边",
        start=4.5,
        end=6,
        font="思源中宋",
        font_color="#FFFFFF",  # 白色文字
        font_size=24.0,
        track_name="text_4",
        transform_y=-0.58,
        border_color="#FF0000",  # 红色描边
        border_width=20.0,
        border_alpha=1.0,
        intro_animation="弹入",
        intro_duration=0.5
    )
    print("测试用例4（综合参数）成功:", result4)
    
    # 最后保存并上传草稿
    if text_result.get('success') and text_result.get('output'):
        save_result = save_draft_impl(text_result['output']['draft_id'],draft_folder)
        print(f"草稿保存结果: {save_result}")
    
    # 返回最后一个测试结果用于后续操作（如果有的话）
    return text_result


def test_image01():
    """Test adding image"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding image 1")
    image_result = add_image_impl(
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=0,
        end=5.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image added successfully! {image_result['output']['draft_id']}")
    print(save_draft_impl(image_result['output']['draft_id'], draft_folder))


def test_image02():
    """Test adding multiple images"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding image 1")
    image_result = add_image_impl(
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=0,
        end=5.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image 1 added successfully! {image_result['output']['draft_id']}")
    
    print("\nTest: Adding image 2")
    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=5,
        end=10.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image 2 added successfully! {image_result['output']['draft_id']}")
    print(save_draft_impl(image_result['output']['draft_id'], draft_folder))


def test_image03():
    """Test adding images to different tracks"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding image 1")
    image_result = add_image_impl(
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=0,
        end=5.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image 1 added successfully! {image_result['output']['draft_id']}")
    
    print("\nTest: Adding image 2")
    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=5,
        end=10.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image 2 added successfully! {image_result['output']['draft_id']}")

    print("\nTest: Adding image 3")
    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=10,
        end=15.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main_2"  # Use different track name
    )
    print(f"Image 3 added successfully! {image_result['output']['draft_id']}")
    query_draft_status_impl_polling(image_result['output']['draft_id'])
    save_draft_impl(image_result['output']['draft_id'], draft_folder)

def test_image04():
    """Test adding image"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding image 1")
    image_result = add_image_impl(
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=5.0,
        end=10.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="image_main"
    )
    print(f"Image added successfully! {image_result['output']['draft_id']}")
    print(save_draft_impl(image_result['output']['draft_id'], draft_folder))

def test_image05():
    """测试添加图片"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\n测试：添加图片1")
    image_result = add_image_impl(
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=1920,
        height=1080,
        start=5.0,
        end=10.0,
        track_name="image_main",
        background_blur=3
    )
    print(f"添加图片成功！{image_result['output']['draft_id']}")
    print(save_draft_impl(image_result['output']['draft_id'], draft_folder))

def test_mask_01():
    """Test adding images to different tracks"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding image 1")
    image_result = add_image_impl(
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=0,
        end=5.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image 1 added successfully! {image_result['output']['draft_id']}")
    
    print("\nTest: Adding image 2")
    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=5,
        end=10.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image 2 added successfully! {image_result['output']['draft_id']}")

    print("\nTest: Adding image 3")
    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=10,
        end=15.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main_2",  # Use different track name
        mask_type="Circle",  # Add circular mask
        mask_center_x=0.5,  # Mask center X coordinate (0.5 means centered)
        mask_center_y=0.5,  # Mask center Y coordinate (0.5 means centered)
        mask_size=0.8,  # Mask size (0.8 means 80%)
        mask_feather=0.1  # Mask feathering (0.1 means 10%)
    )
    print(f"Image 3 added successfully! {image_result['output']['draft_id']}")
    print(save_draft_impl(image_result['output']['draft_id'], draft_folder))

def test_mask_02():
    """Test adding videos to different tracks"""
    # Set draft folder path for saving  
    draft_folder = CAPCUT_DRAFT_FOLDER
    # Define video URL for testing
    video_url = "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4"
    draft_id = None  # Initialize draft_id
    
    # Add video to first track
    video_result = add_video_impl(
        draft_id=draft_id,  # Pass in draft_id
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Use first 5 seconds of video
        target_start=0,
        track_name="main_video_track"
    )
    draft_id = video_result['output']['draft_id']  # Update draft_id
    print(f"First video addition result: {video_result}")
    
    # Add video to second track
    video_result = add_video_impl(
        draft_id=draft_id,  # Use previous draft_id
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Use first 5 seconds of video
        target_start=0,
        track_name="main_video_track_2",  # Use different track name
        speed=1.0,  # Change playback speed
        scale_x=0.5,  # Reduce video width
        transform_y=0.5  # Place video at bottom of screen
    )
    draft_id = video_result['output']['draft_id']  # Update draft_id
    print(f"Second video addition result: {video_result}")
    
    # Third time add video to another track with circular mask
    video_result = add_video_impl(
        draft_id=draft_id,  # Use previous draft_id
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Use first 5 seconds of video
        target_start=0,
        track_name="main_video_track_3",  # Use third track
        speed=1.5,  # Faster playback speed
        scale_x=0.3,  # Smaller video width
        transform_y=-0.5,  # Place video at top of screen
        mask_type="Circle",  # Add circular mask
        mask_center_x=0.5,  # Mask center X coordinate
        mask_center_y=0.5,  # Mask center Y coordinate
        mask_size=0.8,  # Mask size
        mask_feather=0.1  # Mask feathering
    )
    draft_id = video_result['output']['draft_id']  # Update draft_id
    print(f"Third video addition result: {video_result}")
    
    # Finally save and upload draft
    save_result = save_draft_impl(draft_id, draft_folder)
    print(f"Draft save result: {save_result}")


def test_audio01():
    """Test adding audio"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding audio")
    audio_result = add_audio_track(
        audio_url="https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=15,
        volume=0.8,
        speed=1.0,
        track_name="main_audio101",
        # effect_type="麦霸",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result: {audio_result}")
    print(save_draft_impl(audio_result['output']['draft_id'], draft_folder))


def test_audio02():
    """Test adding multiple audio segments"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding audio 1")
    audio_result = add_audio_track(
        audio_url="https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=0,
        volume=0.8,
        speed=1.0,
        track_name="main_audio101",
        # effect_type="麦霸",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result 1: {audio_result}")

    print("\nTest: Adding audio 2")
    audio_result = add_audio_track(
        draft_id=audio_result['output']['draft_id'],
        audio_url="https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=1.5,
        volume=0.8,
        speed=1.0,
        track_name="main_audio101",
        # effect_type="麦霸",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result 2: {audio_result}")
    print(save_draft_impl(audio_result['output']['draft_id'], draft_folder))


def test_audio03():
    """Test adding audio in a loop"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    draft_id = None  # Initialize draft_id
    
    for i in range(10):
        target_start = i * 1.5  # Increment by 1.5 seconds each time
        
        audio_result = add_audio_track(
            audio_url="https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
            start=4,
            end=5,
            target_start=target_start,
            volume=0.8,
            speed=1.0,
            track_name="main_audio101",
            # effect_type="麦霸",
            effect_type="Tremble",
            effect_params=[90.0, 50.0],
            draft_id=draft_id  # Pass the previous draft_id (None for the first time)
        )
        
        draft_id = audio_result['output']['draft_id']  # Update draft_id
        print(f"Audio addition result {i+1}: {audio_result}")
    
    # Finally save and upload draft
    save_result = save_draft_impl(draft_id, draft_folder)
    print(f"Draft save result: {save_result}")


def test_audio04():
    """Test adding audio to different tracks"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding audio 1")
    audio_result = add_audio_track(
        audio_url="https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=0,
        volume=0.8,
        speed=1.0,
        track_name="main_audio101",
        # effect_type="麦霸",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result 1: {audio_result}")

    print("\nTest: Adding audio 2")
    audio_result = add_audio_track(
        draft_id=audio_result['output']['draft_id'],
        audio_url="https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=1.5,
        volume=0.8,
        speed=1.0,
        track_name="main_audio102",  # Use different track name
        # effect_type="麦霸",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result 2: {audio_result}")
    query_draft_status_impl_polling(audio_result['output']['draft_id'])
    save_draft_impl(audio_result['output']['draft_id'], draft_folder)

def add_subtitle_impl(srt, draft_id=None, time_offset=0.0, font_size=5.0, font = "思源粗宋",
                    bold=False, italic=False, underline=False, font_color="#ffffff",
                    transform_x=0.0, transform_y=0.0, scale_x=1.0, scale_y=1.0,
                    vertical=False, track_name="subtitle", alpha=1,
                    border_alpha=1.0, border_color="#000000", border_width=0.0,
                    background_color="#000000", background_style=1, background_alpha=0.0,
                    rotation=0.0, width=1080, height=1920):
    """API wrapper for add_subtitle service"""
    data = {
        "license_key": LICENSE_KEY,  # Using trial version license key
        "srt": srt,  # Modified parameter name to match server side
        "draft_id": draft_id,
        "time_offset": time_offset,
        "font": font,
        "font_size": font_size,
        "bold": bold,
        "italic": italic,
        "underline": underline,
        "font_color": font_color,
        "transform_x": transform_x,
        "transform_y": transform_y,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "vertical": vertical,
        "track_name": track_name,
        "alpha": alpha,
        "border_alpha": border_alpha,
        "border_color": border_color,
        "border_width": border_width,
        "background_color": background_color,
        "background_style": background_style,
        "background_alpha": background_alpha,
        "rotation": rotation,
        "width": width,
        "height": height
    }
    return make_request("add_subtitle", data)

def save_draft_impl(draft_id, draft_folder):
    """API wrapper for save_draft service"""
    data = {
        "license_key": LICENSE_KEY,  # Using trial version license key
        "draft_id": draft_id,
        "draft_folder": draft_folder
    }
    return make_request("save_draft", data)

def query_script_impl(draft_id):
    """API wrapper for query_script service"""
    data = {
        "draft_id": draft_id
    }
    return make_request("query_script", data)

def query_draft_status_impl(task_id):
    """API wrapper for query_draft_status service"""
    data = {
        "license_key": LICENSE_KEY,  # Using trial version license key
        "task_id": task_id
    }
    return make_request("query_draft_status", data)
    
def query_draft_status_impl_polling(task_id, timeout=300, callback=None):
    """
    Poll for draft download status, implemented with async thread to avoid blocking the main thread
    
    :param task_id: task ID returned by save_draft_impl
    :param timeout: timeout in seconds, default 5 minutes
    :param callback: optional callback function called when task completes, fails or times out, with final status as parameter
    :return: tuple of thread object and result container, can be used to get results later
    """
    # Create result container to store final result
    result_container = {"result": None}
    
    def _polling_thread():
        start_time = time.time()
        print(f"Starting to query status for task {task_id}...")
        
        while True:
            try:
                # Get current task status
                task_status = query_draft_status_impl(task_id).get("output", {})
                
                # Print current status
                status = task_status.get("status", "unknown")
                message = task_status.get("message", "")
                progress = task_status.get("progress", 0)
                print(f"Current status: {status}, progress: {progress}%, message: {message}")
                
                # Check if completed or failed
                if status == "completed":
                    print(f"Task completed! Draft URL: {task_status.get('draft_url', 'Not provided')}")
                    result_container["result"] = task_status.get('draft_url', 'Not provided')
                    if callback:
                        callback(task_status.get('draft_url', 'Not provided'))
                    break
                elif status == "failed":
                    print(f"Task failed: {message}")
                    result_container["result"] = task_status
                    if callback:
                        callback(task_status)
                    break
                elif status == "not_found":
                    print(f"Task does not exist: {task_id}")
                    result_container["result"] = task_status
                    if callback:
                        callback(task_status)
                    break
                
                # Check if timed out
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print(f"Query timed out, waited {timeout} seconds")
                    result_container["result"] = task_status
                    if callback:
                        callback(task_status)
                    break
            except Exception as e:
                # Catch all exceptions to prevent thread crash
                print(f"Exception occurred during query: {e}")
                time.sleep(1)  # Wait 1 second before retrying after error
                continue
            
            # Wait 1 second before querying again
            time.sleep(1)
    
    # Create and start thread
    thread = threading.Thread(target=_polling_thread)
    # thread.daemon = True  # Set as daemon thread, automatically terminates when main thread ends
    thread.start()
    
    # Return thread object and result container for external code to get results
    return thread, result_container

def test_subtitle():
    draft_folder = CAPCUT_DRAFT_FOLDER

    # Test case: Add text subtitles
    print("\nTest: Adding text subtitles")
    text_result = add_subtitle_impl(
        srt="1\n00:00:00,000 --> 00:00:04,433\nHello, I am the CapCut draft assistant developed by Sun Guannan.\n\n2\n00:00:04,433 --> 00:00:11,360\nI specialize in combining audio, video, and image materials to create CapCut drafts.\n",
        font_size=8.0,
        bold=True,
        italic=True,
        underline=True,
        font_color="#FF0000",
        transform_y=0,
        transform_x=0.4,
        time_offset=42,
        scale_x=1.0,
        scale_y=2.0,
        vertical=True,
        # Add background color parameters
        background_color="#FFFF00",  # Yellow background
        background_style=1,  # Style 1 means rectangular background
        background_alpha=0.7,  # 70% opacity
        # Add border parameters
        border_color="#0000FF",  # Blue border
        border_width=20.0,  # Border width 2
        border_alpha=1.0  # Fully opaque
    )
    print(f"Text addition result: {text_result}")
    
    # Save draft
    if text_result.get('success') and text_result.get('output'):
        save_result = save_draft_impl(text_result['output']['draft_id'], draft_folder)
        print(f"Draft save result: {save_result}")

def test01():
    draft_folder = CAPCUT_DRAFT_FOLDER

    # Combined test
    print("\nTest 2: Add audio")
    audio_result = add_audio_track(
        audio_url = "https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=2,
        volume=0.8,
        speed=1.0,
        track_name="main_audio100",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result 1: {audio_result}")

    audio_result = add_audio_track(
        draft_id=audio_result['output']['draft_id'],
        audio_url = "https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=4,
        volume=0.8,
        speed=1.0,
        track_name="main_audio100",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result 2: {audio_result}")

    audio_result = add_audio_track(
        draft_id=audio_result['output']['draft_id'],
        audio_url = "https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=6,
        volume=0.8,
        speed=1.0,
        track_name="main_audio101",
        effect_type="Tremble",
        effect_params=[90.0, 50.0]
    )
    print(f"Audio addition result 3: {audio_result}")

    # Test case 1: Basic text addition
    text_result = add_text_impl(
        draft_folder=draft_folder,
        text="Test Text 1",
        draft_id=audio_result['output']['draft_id'],
        start=0,
        end=3,
        font="思源中宋",  # Use Source Han Serif font
        font_color="#FF0000",  # Red
        track_name="main_text",
        transform_y=0.8,
        transform_x=0.5,
        font_size=30.0
    )
    print("Test case 1 (Basic text) successful:", text_result)

    # Test case 2: Vertical text
    result2 = add_text_impl(
        draft_id=text_result['output']['draft_id'],
        text="Vertical Text Test",
        start=3,
        end=6,
        font="云书法三行魏碑体",
        font_color="#00FF00",  # Green
        font_size=8.0,
        track_name="main_text",
        vertical=True,  # Enable vertical text
        transform_y=-0.5,
        outro_animation='Fade_Out'
    )
    print("Test case 2 (Vertical text) successful:", result2)

    print("Test completed")
    # Test adding image
    image_result = add_image_impl(
        draft_id=result2['output']['draft_id'],  # Replace with actual draft ID
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",  # Replace with actual image URL
        width=480,
        height=480,
        start = 0,
        end=5.0,  # Display for 5 seconds
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print("Image added successfully!")


    # Test adding image
    image_result = add_image_impl(
        draft_id=result2['output']['draft_id'],  # Replace with actual draft ID
        image_url="http://gips0.baidu.com/it/u=3602773692,1512483864&fm=3028&app=3028&f=JPEG&fmt=auto?w=960&h=1280",  # Replace with actual image URL
        width=480,
        height=480,
        start = 0,
        end=5.0,  # Display for 5 seconds
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main_2"
    )
    print("Image added successfully!")

    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],  # Replace with actual draft ID
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",  # Replace with actual image URL
        width=480,
        height=480,
        start = 5,
        end=10.0,  # Display for 5 seconds
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print("Image 2 added successfully!")

    # Test adding video keyframe
    print("\nTest: Add video keyframe")
    keyframe_result = add_video_keyframe_impl(
        draft_id=image_result['output']['draft_id'],  # Use existing draft ID
        track_name="main",
        property_type="position_y",  # Test opacity
        time=1.5,  # Add keyframe at 3.5 seconds
        value="0.2"  # Move 300px
    )
    print(f"Keyframe addition result: {keyframe_result}")

    print("\nTest: Add video keyframe")
    keyframe_result = add_video_keyframe_impl(
        draft_id=image_result['output']['draft_id'],  # Use existing draft ID
        track_name="main",
        property_type="position_y",  # Test opacity
        time=3.5,  # Add keyframe at 3.5 seconds
        value="0.4"  # Move 300px
    )
    print(f"Keyframe addition result: {keyframe_result}")
    
    query_draft_status_impl_polling(keyframe_result['output']['draft_id'])
    save_draft_impl(keyframe_result['output']['draft_id'], draft_folder)

def test02():
    draft_folder = CAPCUT_DRAFT_FOLDER

    # Combined test
    print("\nTest 2: Add audio")
    audio_result = add_audio_track(
        audio_url = "https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=2,
        volume=0.8,
        speed=1.0,
        track_name="main_audio100",
        effect_type = "Big_House",
        effect_params = [50.0]
    )
    print(f"Audio addition result 1: {audio_result}")

    audio_result = add_audio_track(
        draft_id=audio_result['output']['draft_id'],
        audio_url = "https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=4,
        volume=0.8,
        speed=1.0,
        track_name="main_audio100",
        effect_type = "Big_House",
        effect_params = [50.0]
    )
    print(f"Audio addition result 2: {audio_result}")

    audio_result = add_audio_track(
        draft_id=audio_result['output']['draft_id'],
        audio_url = "https://lf3-lv-music-tos.faceu.com/obj/tos-cn-ve-2774/oYACBQRCMlWBIrZipvQZhI5LAlUFYii0RwEPh",
        start=4,
        end=5,
        target_start=6,
        volume=0.8,
        speed=1.0,
        track_name="main_audio101",
        effect_type = "Big_House",
        effect_params = [50.0]
    )
    print(f"Audio addition result 3: {audio_result}")

    # Test case 1: Basic text addition
    text_result = add_text_impl(
        draft_folder=draft_folder,
        text="Test Text 1",
        draft_id=audio_result['output']['draft_id'],
        start=0,
        end=3,
        font="思源中宋",  # Use Source Han Serif font
        font_color="#FF0000",  # Red
        track_name="main_text",
        transform_y=0.8,
        transform_x=0.5,
        font_size=30.0
    )
    print("Test case 1 (Basic text) successful:", text_result)

    # Test case 2: Vertical text
    result2 = add_text_impl(
        draft_id=text_result['output']['draft_id'],
        text="Vertical Text Test",
        start=3,
        end=6,
        font="云书法三行魏碑体",
        font_color="#00FF00",  # Green
        font_size=8.0,
        track_name="main_text",
        vertical=True,  # Enable vertical text
        transform_y=-0.5,
        outro_animation='Throw_Back'
    )
    print("Test case 2 (Vertical text) successful:", result2)

    print("Test completed")
    # Test adding image
    image_result = add_image_impl(
        draft_id=result2['output']['draft_id'],  # Replace with actual draft ID
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",  # Replace with actual image URL
        width=480,
        height=480,
        start = 0,
        end=5.0,  # Display for 5 seconds
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print("Image added successfully!")


    # Test adding image
    image_result = add_image_impl(
        draft_id=result2['output']['draft_id'],  # Replace with actual draft ID
        image_url="http://gips0.baidu.com/it/u=3602773692,1512483864&fm=3028&app=3028&f=JPEG&fmt=auto?w=960&h=1280",  # Replace with actual image URL
        width=480,
        height=480,
        start = 0,
        end=5.0,  # Display for 5 seconds
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main_2"
    )
    print("Image added successfully!")

    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],  # Replace with actual draft ID
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",  # Replace with actual image URL
        width=480,
        height=480,
        start = 5,
        end=10.0,  # Display for 5 seconds
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print("Image 2 added successfully!")

    # Test adding video keyframe
    print("\nTest: Add video keyframe")
    keyframe_result = add_video_keyframe_impl(
        draft_id=image_result['output']['draft_id'],  # Use existing draft ID
        track_name="main",
        property_type="position_y",  # Test opacity
        time=1.5,  # Add keyframe at 3.5 seconds
        value="0.2"  # Move 300px
    )
    print(f"Keyframe addition result: {keyframe_result}")

    print("\nTest: Add video keyframe")
    keyframe_result = add_video_keyframe_impl(
        draft_id=image_result['output']['draft_id'],  # Use existing draft ID
        track_name="main",
        property_type="position_y",  # Test opacity
        time=3.5,  # Add keyframe at 3.5 seconds
        value="0.4"  # Move 300px
    )
    print(f"Keyframe addition result: {keyframe_result}")
    
    query_draft_status_impl_polling(keyframe_result['output']['draft_id'])
    save_draft_impl(keyframe_result['output']['draft_id'], draft_folder)

def test_video_track01():
    """Test adding video track"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    video_url = "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4" # Replace with actual video URL

    print("\nTest: Add video track")
    video_result = add_video_impl(
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Cut the first 5 seconds of the video
        target_start=0,
        track_name="main_video_track"
    )
    print(f"Video track addition result: {video_result}")

    if video_result and 'output' in video_result and 'draft_id' in video_result['output']:
        draft_id = video_result['output']['draft_id']
        print(f"Save draft: {save_draft_impl(draft_id, draft_folder)}")
    else:
        print("Unable to get draft ID, skipping save operation.")


def test_video_track02():
    """Test adding video tracks in a loop"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    video_url = "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4" # Replace with actual video URL
    draft_id = None  # Initialize draft_id
    
    for i in range(5):
        target_start = i * 5  # Increment by 5 seconds each time
        
        video_result = add_video_impl(
            draft_id=draft_id,  # Pass in draft_id
            video_url=video_url,
            width=1920,
            height=1080,
            start=0,
            end=5.0, # Cut the first 5 seconds of the video
            target_start=target_start,
            track_name="main_video_track"
        )
        draft_id = video_result['output']['draft_id']  # Update draft_id
        print(f"Video addition result {i+1}: {video_result}")
    
    # Finally save and upload the draft
    save_result = save_draft_impl(draft_id, draft_folder)
    print(f"Draft save result: {save_result}")


def test_video_track03():
    """Test adding videos to different tracks"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    video_url = "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4" # Replace with actual video URL
    draft_id = None  # Initialize draft_id
    
    # Add video to the first track
    video_result = add_video_impl(
        draft_id=draft_id,  # Pass in draft_id
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Cut the first 5 seconds of the video
        target_start=0,
        track_name="main_video_track"
    )
    draft_id = video_result['output']['draft_id']  # Update draft_id
    print(f"First video addition result: {video_result}")
    
    # Add video to the second track
    video_result = add_video_impl(
        draft_id=draft_id,  # Use previous draft_id
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Cut the first 5 seconds of the video
        target_start=0,
        track_name="main_video_track_2",  # Use different track name
        speed=1.0,  # Change playback speed
        scale_x=0.5,  # Reduce video width
        transform_y=0.5  # Position video at bottom of screen
    )
    draft_id = video_result['output']['draft_id']  # Update draft_id
    print(f"Second video addition result: {video_result}")
    
    # Third time add video to another track
    video_result = add_video_impl(
        draft_id=draft_id,  # Use previous draft_id
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Cut the first 5 seconds of the video
        target_start=0,
        track_name="main_video_track_3",  # Use third track
        speed=1.5,  # Faster playback speed
        scale_x=0.3,  # Smaller video width
        transform_y=-0.5  # Position video at top of screen
    )
    draft_id = video_result['output']['draft_id']  # Update draft_id
    print(f"Third video addition result: {video_result}")
    
    # Finally save and upload the draft
    save_result = save_draft_impl(draft_id, draft_folder)
    print(f"Draft save result: {save_result}")

def test_video_track04():
    """Test adding video track"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    video_url = "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4" # Replace with actual video URL

    print("\nTest: Add video track")
    video_result = add_video_impl(
        video_url='https://p26-bot-workflow-sign.byteimg.com/tos-cn-i-mdko3gqilj/07bf6797a1834d75beb05c63293af204.mp4~tplv-mdko3gqilj-image.image?rk3s=81d4c505&x-expires=1782141919&x-signature=2ETX83Swh%2FwKzHeWB%2F9oGq9vqt4%3D&x-wf-file_name=output-997160b5.mp4'
    )
    print(f"Video track addition result: {video_result}")

    print("\nTest: Add video track")
    video_result = add_video_impl(
        video_url='https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4',
        draft_id=video_result['output']['draft_id'],  # Use existing draft ID
        target_start=19.84
    )
    print(f"Video track addition result: {video_result}")
    if video_result and 'output' in video_result and 'draft_id' in video_result['output']:
        draft_id = video_result['output']['draft_id']
        print(f"Save draft: {save_draft_impl(draft_id, draft_folder)}")
    else:
        print("Unable to get draft ID, skipping save operation.")

def test_video_track05():
    """测试添加视频轨道"""
    draft_folder = CAPCUT_DRAFT_FOLDER

    video_url = "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4" # 替换为实际视频URL

    print("\n测试：添加视频轨道")
    video_result = add_video_impl(
        video_url='https://p26-bot-workflow-sign.byteimg.com/tos-cn-i-mdko3gqilj/07bf6797a1834d75beb05c63293af204.mp4~tplv-mdko3gqilj-image.image?rk3s=81d4c505&x-expires=1782141919&x-signature=2ETX83Swh%2FwKzHeWB%2F9oGq9vqt4%3D&x-wf-file_name=output-997160b5.mp4',
        background_blur=2,
        width=1920,
        height=1080
    )

    print(f"视频轨道添加结果: {video_result}")
    if video_result and 'output' in video_result and 'draft_id' in video_result['output']:
        draft_id = video_result['output']['draft_id']
        print(f"保存草稿: {save_draft_impl(draft_id, draft_folder)}")
    else:
        print("无法获取草稿ID，跳过保存操作。")

def test_keyframe():
    """Test adding keyframes"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    draft_id = None  # Initialize draft_id
    
    print("\nTest: Add basic video track")
    video_result = add_video_impl(
        video_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4",
        width=1920,
        height=1080,
        start=0,
        end=10.0,
        target_start=0,
        track_name="main_video_track"
    )
    print("Video addition result:", video_result)
    
    if video_result.get('success') and video_result.get('output'):
        draft_id = video_result['output']['draft_id']
        print("Using existing draft_id:", draft_id)
    else:
        print("Unable to get draft ID, terminating test.")
        return

    print("\nTest: Add opacity keyframe")
    keyframe_result = add_video_keyframe_impl(
        draft_id=draft_id,
        track_name="main_video_track",
        property_type="alpha",
        time=2.0,
        value="1.0"
    )
    print("Opacity keyframe addition result:", keyframe_result)

    print("\nTest: Add position Y keyframe")
    keyframe_result = add_video_keyframe_impl(
        draft_id=draft_id,
        track_name="main_video_track",
        property_type="position_y",
        time=2.0,
        value="0.5"
    )
    print("Position Y keyframe addition result:", keyframe_result)

    print("\nTest: Add scale X keyframe")
    keyframe_result = add_video_keyframe_impl(
        draft_id=draft_id,
        track_name="main_video_track",
        property_type="position_y",
        time=4.0,
        value="-0.5"
    )
    print("Scale X keyframe addition result:", keyframe_result)

    print("\nFinal draft save")
    save_result = save_draft_impl(draft_id, draft_folder)
    print(f"Draft save result: {save_result}")

def test_keyframe_02():
    """Test adding keyframes - Batch adding to implement fade-in and zoom bounce effects"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    draft_id = None  # Initialize draft_id
    
    print("\nTest: Adding basic video track")
    video_result = add_video_impl(
        video_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4",
        width=1920,
        height=1080,
        start=0,
        end=10.0,
        target_start=0,
        track_name="main_video_track"
    )
    print("Video adding result:", video_result)
    
    if video_result.get('success') and video_result.get('output'):
        draft_id = video_result['output']['draft_id']
        print("Using existing draft_id:", draft_id)
    else:
        print("Unable to get draft ID, terminating test.")
        return

    print("\nTest: Batch adding opacity keyframes - Implementing fade-in effect")
    # Add opacity keyframes to implement fade-in effect from invisible to visible
    alpha_keyframe_result = add_video_keyframe_impl(
        draft_id=draft_id,
        track_name="main_video_track",
        property_types=["alpha", "alpha", "alpha", "alpha"],
        times=[0.0, 1.0, 2.0, 3.0],
        values=["0.0", "0.3", "0.7", "1.0"]
    )
    print("Opacity keyframe batch adding result:", alpha_keyframe_result)

    print("\nTest: Batch adding scale keyframes - Implementing zoom bounce effect")
    # Add uniform scale keyframes to implement zoom bounce effect
    scale_keyframe_result = add_video_keyframe_impl(
        draft_id=draft_id,
        track_name="main_video_track",
        property_types=["uniform_scale", "uniform_scale", "uniform_scale", "uniform_scale", "uniform_scale"],
        times=[0.0, 1.5, 3.0, 4.5, 6.0],
        values=["0.8", "1.3", "1.0", "1.2", "1.0"]
    )
    print("Scale keyframe batch adding result:", scale_keyframe_result)

    print("\nTest: Batch adding position Y keyframes - Implementing up and down floating effect")
    # Add position Y keyframes to implement up and down floating effect
    position_y_keyframe_result = add_video_keyframe_impl(
        draft_id=draft_id,
        track_name="main_video_track",
        property_types=["position_y", "position_y", "position_y", "position_y"],
        times=[2.0, 3.5, 5.0, 6.5],
        values=["0.0", "0.2", "-0.2", "0.0"]
    )
    print("Position Y keyframe batch adding result:", position_y_keyframe_result)

    print("\nFinal draft saving")
    save_result = save_draft_impl(draft_id, draft_folder)
    print(f"Draft saving result: {save_result}")

def test_subtitle_01():
    """Test adding text subtitles"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    
    print("\nTest 3: Adding text subtitles")
    text_result = add_subtitle_impl(
        srt="1\n00:00:00,000 --> 00:00:04,433\n你333好，我是孙关南开发的剪映草稿助手。\n\n2\n00:00:04,433 --> 00:00:11,360\n我擅长将音频、视频、图片素材拼接在一起剪辑输出剪映草稿。\n",
        font_size=8.0,
        bold=True,
        italic=True,
        underline=True,
        font_color="#FF0000",
        transform_y=0,
        transform_x=0.4,
        time_offset=42,
        scale_x=1.0,
        scale_y=2.0,
        vertical=True
    )
    print(f"Text adding result: {text_result}")
    
    if text_result.get('success') and text_result.get('output'):
        save_result = save_draft_impl(text_result['output']['draft_id'], draft_folder)
        print(f"Draft saving result: {save_result}")
    
    return text_result


def test_subtitle_02():
    """Test adding text subtitles via SRT URL"""
    draft_folder = CAPCUT_DRAFT_FOLDER
    
    print("\nTest 3: Adding text subtitles (from URL)")
    text_result = add_subtitle_impl(
        srt="https://oss-oversea-bucket.oss-cn-hongkong.aliyuncs.com/dfd_srt_1748575460_kmtu56iu.srt?Expires=1748707452&OSSAccessKeyId=TMP.3Km5TL5giRLgDkc3CamKPcWZTmSrLVeRxPWxEisNB2CTymvUxrpX8VXzy5r99F6bJkwjwFM5d1RsiV3cF18iaMriAPtA1y&Signature=4JzB4YGiChsxcTFuvUyZ0v3MjMI%3D",
        font_size=8.0,
        bold=True,
        italic=True,
        underline=True,
        font_color="#FF0000",
        transform_y=0,
        transform_x=0.4,
        time_offset=42,
        scale_x=1.0,
        scale_y=2.0,
        vertical=True
    )
    print(f"Text adding result: {text_result}")
    
    if text_result.get('success') and text_result.get('output'):
        save_result = save_draft_impl(text_result['output']['draft_id'], draft_folder)
        print(f"Draft saving result: {save_result}")
    
    return text_result


def test_video_01():
    """Test adding single video with transform and speed parameters"""
    # Set draft folder path for saving
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding video")
    video_result = add_video_impl(
        video_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4", # Replace with actual video URL
        start=0,
        end=5,
        width=1920,
        height=1080,
        track_name="main_video",
        transform_y=0.1,
        scale_x=0.8,
        scale_y=0.8,
        transform_x=0.1,
        speed=1.2,
        target_start=0,
        relative_index=0
    )
    print(f"Video adding result: {video_result}")

    # Save draft
    if video_result.get('success') and video_result.get('output'):
        query_draft_status_impl_polling(video_result['output']['draft_id'])
        save_draft_impl(video_result['output']['draft_id'], draft_folder)
        
def test_video_02():
    """Test adding multiple videos with different resolutions to the same draft"""
    # Set draft folder path for saving
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding video")
    video_result = add_video_impl(
        video_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4", # Replace with actual video URL
        start=0,
        end=5,
        width=1920,
        height=1080,
        track_name="main_video",
        transform_y=0.1,
        scale_x=0.8,
        scale_y=0.8,
        transform_x=0.1,
        speed=1.2,
        target_start=0,
        relative_index=0
    )
    print(f"Video adding result: {video_result}")

    video_result = add_video_impl(
        video_url="https://videos.pexels.com/video-files/3129769/3129769-hd_1280_720_30fps.mp4", # Replace with actual video URL
        draft_id=video_result['output']['draft_id'],
        start=0,
        end=5,
        width=1920,
        height=1080,
        track_name="main_video_2",
        transform_y=0.1,
        scale_x=0.8,
        scale_y=0.8,
        transform_x=0.1,
        speed=1.2,
        target_start=0,
        relative_index=0
    )
    video_result = add_video_impl(
        video_url="https://videos.pexels.com/video-files/3129769/3129769-uhd_3840_2160_30fps.mp4", # Replace with actual video URL
        draft_id=video_result['output']['draft_id'],
        start=0,
        end=5,
        width=1920,
        height=1080,
        track_name="main_video_3",
        transform_y=0.1,
        scale_x=0.8,
        scale_y=0.8,
        transform_x=0.1,
        speed=1.2,
        target_start=0,
        relative_index=0
    )
    video_result = add_video_impl(
        video_url="https://videos.pexels.com/video-files/3129769/3129769-sd_426_240_30fps.mp4", # Replace with actual video URL
        draft_id=video_result['output']['draft_id'],
        start=0,
        end=5,
        width=1920,
        height=1080,
        track_name="main_video_4",
        transform_y=0.1,
        scale_x=0.8,
        scale_y=0.8,
        transform_x=0.1,
        speed=1.2,
        target_start=0,
        relative_index=0
    )
    video_result = add_video_impl(
        video_url="https://videos.pexels.com/video-files/3129769/3129769-sd_640_360_30fps.mp4", # Replace with actual video URL
        draft_id=video_result['output']['draft_id'],
        start=0,
        end=5,
        width=1920,
        height=1080,
        track_name="main_video_5",
        transform_y=0.1,
        scale_x=0.8,
        scale_y=0.8,
        transform_x=0.1,
        speed=1.2,
        target_start=0,
        relative_index=0
    )
    video_result = add_video_impl(
        video_url="https://videos.pexels.com/video-files/3129769/3129769-uhd_2560_1440_30fps.mp4", # Replace with actual video URL
        draft_id=video_result['output']['draft_id'],
        start=0,
        end=5,
        width=1920,
        height=1080,
        track_name="main_video_6",
        transform_y=0.1,
        scale_x=0.8,
        scale_y=0.8,
        transform_x=0.1,
        speed=1.2,
        target_start=0,
        relative_index=0
    )

    if video_result.get('success') and video_result.get('output'):
        print(json.loads(query_script_impl(video_result['output']['draft_id'])['output']))
        # query_draft_status_impl_polling(video_result['output']['draft_id'])
        # save_draft_impl(video_result['output']['draft_id'], draft_folder)
   
def test_stiker_01():
    """Test adding stickers"""
    # Add stickers, test various parameters, only for jianyingpro
    draft_folder = JIANYINGPRO_DRAFT_FOLDER
    result = add_sticker_impl(
        resource_id="7107529669750066445",
        start=1.0,
        end=4.0,
        transform_y=0.3,      # Move up
        transform_x=-0.2,     # Move left
        alpha=0.8,            # Set transparency
        rotation=45.0,        # Rotate 45 degrees
        scale_x=1.5,          # Horizontal scale 1.5x
        scale_y=1.5,          # Vertical scale 1.5x
        flip_horizontal=True  # Horizontal flip
    )
    print(f"Sticker adding result: {save_draft_impl(result['output']['draft_id'], draft_folder)}")

def test_stiker_02():
    """Test adding stickers"""
    # Add stickers, test various parameters, only for jianyingpro
    draft_folder = JIANYINGPRO_DRAFT_FOLDER
    result = add_sticker_impl(
        resource_id="7107529669750066445",
        start=1.0,
        end=4.0,
        transform_y=0.3,      # Move up
        transform_x=-0.2,     # Move left
        alpha=0.8,            # Set transparency
        rotation=45.0,        # Rotate 45 degrees
        scale_x=1.5,          # Horizontal scale 1.5x
        scale_y=1.5,          # Vertical scale 1.5x
        flip_horizontal=True  # Horizontal flip
    )
    result = add_sticker_impl(
        resource_id="7107529669750066445",
        draft_id=result['output']['draft_id'],
        start=5.0,
        end=10.0,
        transform_y=-0.3,     # Move up
        transform_x=0.5,      # Move left
        alpha=0.1,            # Set transparency
        rotation=30.0,        # Rotate 30 degrees
        scale_x=1.5,          # Horizontal scale 1.5x
        scale_y=1.2,          # Vertical scale 1.2x
    )
    print(f"Sticker adding result: {save_draft_impl(result['output']['draft_id'], draft_folder)}")

def test_stiker_03():
    """Test adding stickers"""
    # Add stickers, test various parameters, only for jianyingpro
    draft_folder = JIANYINGPRO_DRAFT_FOLDER
    result = add_sticker_impl(
        resource_id="7107529669750066445",
        start=1.0,
        end=4.0,
        transform_y=0.3,      # Move up
        transform_x=-0.2,     # Move left
        alpha=0.8,            # Set transparency
        rotation=45.0,        # Rotate 45 degrees
        scale_x=1.5,          # Horizontal scale 1.5x
        scale_y=1.5,          # Vertical scale 1.5x
        flip_horizontal=True, # Horizontal flip
        track_name="stiker_main",
        relative_index=999
    )
    result = add_sticker_impl(
        resource_id="7107529669750066445",
        draft_id=result['output']['draft_id'],
        start=5.0,
        end=10.0,
        transform_y=-0.3,     # Move up
        transform_x=0.5,      # Move left
        alpha=0.1,            # Set transparency
        rotation=30.0,        # Rotate 30 degrees
        scale_x=1.5,          # Horizontal scale 1.5x
        scale_y=1.2,          # Vertical scale 1.2x
        track_name="stiker_main_2",
        relative_index=0
    )
    print(f"Sticker adding result: {save_draft_impl(result['output']['draft_id'], draft_folder)}")


def test_transition_01():
    """Test adding multiple images with dissolve transition effects"""
    # Set draft folder path for saving
    draft_folder = CAPCUT_DRAFT_FOLDER

    print("\nTest: Adding image 1")
    image_result = add_image_impl(
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=0,
        end=5.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main",
        transition="Dissolve",
        transition_duration=1.0
    )
    print(f"Image 1 added successfully! {image_result['output']['draft_id']}")
    
    print("\nTest: Adding image 2")
    image_result = add_image_impl(
        draft_id=image_result['output']['draft_id'],
        image_url="https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_image_v2/d6e33c84d7554146a25b1093b012838b_0.png?x-oss-process=image/resize,w_500/watermark,image_aW1nL3dhdGVyMjAyNDExMjkwLnBuZz94LW9zcy1wcm9jZXNzPWltYWdlL3Jlc2l6ZSxtX2ZpeGVkLHdfMTQ1LGhfMjU=,t_80,g_se,x_10,y_10/format,webp",
        width=480,
        height=480,
        start=5,
        end=10.0,
        transform_y=0.7,
        scale_x=2.0,
        scale_y=1.0,
        transform_x=0,
        track_name="main"
    )
    print(f"Image 2 added successfully! {image_result['output']['draft_id']}")
    print(save_draft_impl(image_result['output']['draft_id'], draft_folder))


def test_transition_02():
    """Test adding video tracks with transition effects"""
    # Set draft folder path for saving  
    draft_folder = CAPCUT_DRAFT_FOLDER
    # Define video URL for testing
    video_url = "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4?spm=5176.29623064.0.0.41ed26d6cBOhV3&file=092faf3c94244973ab752ee1280ba76f.mp4"

    print("\nTest: Adding video track")
    video_result = add_video_impl(
        video_url=video_url,
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Trim first 5 seconds of video
        target_start=0,
        track_name="main_video_track",
        transition="Dissolve",
        transition_duration=1.0
    )
    print(f"Video track adding result: {video_result}")

    print("\nTest: Adding video track")
    video_result = add_video_impl(
        video_url=video_url,
        draft_id=video_result['output']['draft_id'],
        width=1920,
        height=1080,
        start=0,
        end=5.0, # Trim first 5 seconds of video
        target_start=5.0,
        track_name="main_video_track"
    )
    print(f"Video track adding result: {video_result}")

    if video_result and 'output' in video_result and 'draft_id' in video_result['output']:
        draft_id = video_result['output']['draft_id']
        print(f"Saving draft: {save_draft_impl(draft_id, draft_folder)}")
    else:
        print("Unable to get draft ID, skipping save operation.")

if __name__ == "__main__":
    # test01()
    # test02()
    # test_effect_01()  # Run effect test
    # test_effect_02()
    # test_audio01()
    # test_audio02()
    # test_audio03()
    # test_audio04()
    # test_image01()
    # test_image02()
    # test_image03()
    # test_image04()
    # # test_video()
    # test_video_02()
    # test_text()
    # test_video_track01()
    # test_video_track02()
    # test_video_track03()
    # test_video_track04()
    # test_keyframe()
    # test_keyframe_02()
    test_subtitle_01()
    # test_subtitle_02()
    # test_subtitle()
    # test_stiker_01()
    # test_stiker_02()
    # test_stiker_03()
    # test_transition_01()
    # test_transition_02()
    # # test_generate_image01()
    # # test_generate_image02()
    # # test_speech_01()
    # test_mask_01()
    # test_mask_02()
