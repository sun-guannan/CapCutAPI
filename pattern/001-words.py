import requests
import json
from flask import Flask, request, jsonify, Response
import sys
import time
import json

sys.path.append('/Users/sunguannan/capcutapi')
from example import add_image_impl

PORT=9001       #端口
BASE_URL = f"http://localhost:{PORT}"
draft_folder = "/Users/sunguannan/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"




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

def save_draft_impl(draft_id, draft_folder):
    """API wrapper for save_draft service"""
    data = {
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


def group_sentences(corrected_srt, threshold=1.0):
    """按时间间隔分句"""
    if not corrected_srt:
        return []
    sentences = []
    current_sentence = [corrected_srt[0]]
    for i in range(1, len(corrected_srt)):
        prev_end = corrected_srt[i-1]["end"]
        curr_start = corrected_srt[i]["start"]
        if curr_start - prev_end > threshold:
            sentences.append(current_sentence)
            current_sentence = [corrected_srt[i]]
        else:
            current_sentence.append(corrected_srt[i])
    sentences.append(current_sentence)
    return sentences


def adjust_sentence_timing(sentences, gap_adjust=1, time_precision=3):
    """调整句子间的时间间隔，并保留原始时间"""
    def round_time(t):
        return round(t, time_precision) if time_precision is not None else t

    adjusted_sentences = []
    total_offset = 0.0
    prev_end = sentences[0][-1]["end"]

    # 第一句保持原时间
    first_sentence = [
        {
            "word": w["word"],
            "start": w["start"],
            "end": w["end"],
            "original_start": w["start"],
            "original_end": w["end"]
        }
        for w in sentences[0]
    ]
    adjusted_sentences.append(first_sentence)

    for i in range(1, len(sentences)):
        sentence = sentences[i]
        curr_start = sentence[0]["start"]
        natural_gap = curr_start - prev_end
        adjusted_gap = natural_gap if gap_adjust == 0 else (1.0 if natural_gap > 1.0 else natural_gap)
        move_amount = natural_gap - adjusted_gap
        total_offset += move_amount

        adjusted_sentence = []
        for w in sentence:
            adjusted_sentence.append({
                "word": w["word"],
                "start": round_time(w["start"] - total_offset),
                "end": round_time(w["end"] - total_offset),
                "original_start": w["start"],
                "original_end": w["end"]
            })
        adjusted_sentences.append(adjusted_sentence)
        prev_end = sentence[-1]["end"]
    return adjusted_sentences


def split_into_paragraphs(sentence, max_words=5, max_chunk_duration=1.5):
    """把句子按词数和时长分段"""
    paragraphs = []
    i = 0
    n = len(sentence)
    while i < n:
        paragraph = [sentence[i]]
        current_start = sentence[i]["start"]
        current_end = sentence[i]["end"]
        i += 1
        while i < n:
            current_word = sentence[i]
            is_continuous = abs(current_word["start"] - current_end) < 0.001
            if (len(paragraph) >= max_words or
                (current_word["end"] - current_start) >= max_chunk_duration or
                not is_continuous):
                break
            paragraph.append(current_word)
            current_end = current_word["end"]
            i += 1
        paragraphs.append(paragraph)
    
    return paragraphs


def build_segments_by_mode(
    mode, 
    paragraph, 
    track_name, 
    font, 
    font_size,
    highlight_color, 
    normal_color, 
    transform_x, 
    transform_y, 
    fixed_width, 
    shadow_enabled, 
    shadow_color, 
    border_color, 
    border_width, 
    border_alpha, 
    background_color,
    ):

    """根据模式生成字幕片段"""
    segments = []
    #print("二级代码返回调试fx", fixed_width)

    if mode == "word_pop":
        # 单词跳出
        for w in paragraph:
            text_styles = []
            word_count = len(w["word"].replace(" ", "")) #统计有多少个字
            text_styles.append({
                        "start": 0,
                        "end": word_count,
                        "border": {
                            "alpha": border_alpha,
                            "color": border_color,
                            "width": border_width
                        }
                    })
            segments.append({
                "text": w["word"],
                "start": w["start"],
                "end": w["end"],
                "font": font,
                "track_name": track_name,
                "font_color": normal_color,
                "font_size": font_size,
                "transform_x": transform_x,
                "transform_y": transform_y,
                "shadow_enabled": shadow_enabled,
                "fixed_width": fixed_width,
                "text_styles": text_styles,

                "shadow_color": shadow_color,
                "border_color": border_color,
                "border_width": border_width,
                "border_alpha": border_alpha,

                "background_color": background_color,
            })

    elif mode == "word_highlight":
        # 单词高亮：当前词亮，其他灰
        paragraph_text = " ".join(w["word"] for w in paragraph)
        offsets = []
        ci = 0
        for w in paragraph:
            offsets.append((ci, ci + len(w["word"])))
            ci += len(w["word"]) + 1
        for idx, w in enumerate(paragraph):
            text_styles = []
            for k, (s, e) in enumerate(offsets):
                color = highlight_color if k == idx else normal_color
                text_styles.append({
                    "start": s,
                    "end": e,
                    "style": {
                        "color": color, 
                        "size": font_size, 
                        },
                    "border": {
                        "alpha": border_alpha,
                        "color": border_color,
                        "width": border_width
                    }
                })
            print("text_styles", text_styles)

            segments.append({
                "text": paragraph_text,
                "start": w["start"],
                "end": w["end"],
                "font": font,
                "track_name": track_name,
                "font_color": normal_color,
                "font_size": font_size,
                "text_styles": text_styles,
                "transform_x": transform_x,
                "transform_y": transform_y,
                "shadow_enabled": shadow_enabled,
                "fixed_width": fixed_width,


                "shadow_color": shadow_color,
                "border_color": border_color,
                "border_width": border_width,
                "border_alpha": border_alpha,

                "background_color": background_color,
            })

    elif mode == "sentence_fade":
        # 句子渐显：已亮过的词继续保持亮
        paragraph_text = " ".join(w["word"] for w in paragraph)
        offsets = []
        ci = 0
        for w in paragraph:
            offsets.append((ci, ci + len(w["word"])))
            ci += len(w["word"]) + 1
        for idx, w in enumerate(paragraph):
            text_styles = []
            for k, (s, e) in enumerate(offsets):
                color = highlight_color if k <= idx else normal_color
                text_styles.append({
                    "start": s,
                    "end": e,
                    "style": {"color": color, "size": font_size},
                    "border": {
                        "alpha": border_alpha,
                        "color": border_color,
                        "width": border_width
                    }
                })
            segments.append({
                "text": paragraph_text,
                "start": w["start"],
                "end": w["end"],
                "font": font,
                "track_name": track_name,
                "font_color": normal_color,
                "font_size": font_size,
                "text_styles": text_styles,
                "transform_x": transform_x,
                "transform_y": transform_y,
                "shadow_enabled": shadow_enabled,
                "fixed_width": fixed_width,


                "shadow_color": shadow_color,
                "border_color": border_color,
                "border_width": border_width,
                "border_alpha": border_alpha,

                "background_color": background_color,
            })

    elif mode == "sentence_pop":
        # 句子跳出
        text = " ".join(w["word"] for w in paragraph)
        start_time = paragraph[0]["start"]
        end_time = paragraph[-1]["end"]
        text_styles = []
        word_count = len(text.replace(" ", "")) #统计有多少个字
        text_styles.append({
                    "start": 0,
                    "end": word_count,
                    "border": {
                        "alpha": border_alpha,
                        "color": border_color,
                        "width": border_width
                    }
                })
        segments.append({
            "text": text,
            "start": start_time,
            "end": end_time,
            "font": font,
            "track_name": track_name,
            "font_color": normal_color,
            "font_size": font_size,
            "transform_x": transform_x,
            "transform_y": transform_y,
            "shadow_enabled": shadow_enabled,
            "fixed_width": fixed_width,
            "text_styles": text_styles,


            "shadow_color": shadow_color,
            "border_color": border_color,
            "border_width": border_width,
            "border_alpha": border_alpha,

            "background_color": background_color,
        })

    else:
        raise ValueError(f"未知模式: {mode}")
    """segments.append({
        "file_name": file_name,
    })"""

    return segments

corrected_srt = [{
                                "word": "Hello",
                                "start": 0.0,
                                "end": 0.64,
                                "confidence": 0.93917525
                            },
                            {
                                "word": "I'm",
                                "start": 0.64,
                                "end": 0.79999995,
                                "confidence": 0.9976464
                            },
                            {
                                "word": "PAWA",
                                "start": 0.79999995,
                                "end": 1.36,
                                "confidence": 0.6848311
                            },
                            {
                                "word": "Nice",
                                "start": 1.36,
                                "end": 1.52,
                                "confidence": 0.9850389
                            },
                            {
                                "word": "To",
                                "start": 1.52,
                                "end": 1.68,
                                "confidence": 0.9926886
                            },
                            {
                                "word": "Meet",
                                "start": 1.68,
                                "end": 2.08,
                                "confidence": 0.9972697
                            },
                            {
                                "word": "You",
                                "start": 2.08,
                                "end": 2.72,
                                "confidence": 0.9845563
                            },
                            {
                                "word": "Enjoy",
                                "start": 2.72,
                                "end": 3.04,
                                "confidence": 0.99794894
                            },
                            {
                                "word": "My",
                                "start": 3.04,
                                "end": 3.1999998,
                                "confidence": 0.9970203
                            },
                            {
                                "word": "Parttern",
                                "start": 3.1999998,
                                "end": 3.36,
                                "confidence": 0.9970235
                            },
                            {
                                "word": "Thank",
                                "start": 3.36,
                                "end": 3.6799998,
                                "confidence": 0.98627764
                            },
                            {
                                "word": "You",
                                "start": 3.6799998,
                                "end": 4.0,
                                "confidence": 0.9939551
                            },
                            ]


def add_koubo_from_srt(
    corrected_srt, 
    track_name, 
    mode="word_pop",
    font="ZY_Modern", 
    font_size=32, 
    highlight_color="#FFD700",
    normal_color="#AAAAAA", max_chunk_duration=1.5, max_words=5,
    gap_adjust=1, 
    time_precision=3, 
    transform_x=0.5, 
    transform_y=0.3,
    fixed_width=-1, 
    shadow_enabled=True, 
    shadow_color="#000000", 
    border_color="#000000", 
    border_width=0.5, 
    border_alpha=1.0, 
    background_color="#000000",

    ):
    """统一入口：根据 mode 选择字幕效果"""
    sentences = group_sentences(corrected_srt)
    adjusted_sentences = adjust_sentence_timing(sentences, gap_adjust, time_precision)
    all_paragraphs = [split_into_paragraphs(s, max_words, max_chunk_duration) for s in adjusted_sentences]

    draft_id_ret = None
    for sentence_paragraphs in all_paragraphs:
        for paragraph in sentence_paragraphs:
            segments = build_segments_by_mode(
                mode, 
                paragraph, 
                track_name, 
                font, 
                font_size,
                highlight_color, 
                normal_color, 
                transform_x, 
                transform_y,
                fixed_width,
                shadow_enabled, 
                shadow_color, 
                border_color, 
                border_width, 
                border_alpha,  
                background_color,

                )
            #print("segments", segments)

            for seg in segments:
                #print("二级代码返回调试fx", seg)
                if draft_id_ret:
                    seg["draft_id"] = draft_id_ret
                    print("seg", seg)

                res = add_text_impl(**seg)
                if draft_id_ret is None and isinstance(res, dict):
                    try:
                        draft_id_ret = res["output"]["draft_id"]
                    except:
                        pass
    return draft_id_ret

colors = {
        "shadow_color": "#000000",
        "border_color": "#FFD700",
        "background_color": "#000000",
        "normal_color": "#FFFFFF",
        "highlight_color": "#DA70D6"  # 紫色
    }

draft_id = add_koubo_from_srt(
    corrected_srt, 
    track_name="main_text", 
    font_size=15,
    gap_adjust=0,
    transform_x=0,
    transform_y=-0.45,# 0=保持原间隔，1=调整>1s的间隔
    fixed_width = 0.6,
    mode="word_highlight",
    shadow_enabled=True,
    border_width=10,
    border_alpha=1.0,

    **colors,

    font="ZY_Modern", #设置自己的字体，需要在字体库中添加


)

add_image_impl(image_url="https://pic1.imgdb.cn/item/689aff2758cb8da5c81e64a2.png", start = 0, end = 4, draft_id=draft_id)

save_result = save_draft_impl(draft_id, draft_folder)

print(save_result)
"""
# 单词高亮
mode="word_highlight"
# 单词跳出
mode="word_pop"
# 句子渐显
mode="sentence_fade"
# 句子跳出
mode="sentence_pop"
"""
