from flask import Blueprint, request, jsonify

from add_text_impl import add_text_impl
from util import hex_to_rgb
from pyJianYingDraft.text_segment import TextStyleRange, Text_style, Text_border


bp = Blueprint('text', __name__)


@bp.route('/add_text', methods=['POST'])
def add_text():
    data = request.get_json()

    text = data.get('text')
    start = data.get('start', 0)
    end = data.get('end', 5)
    draft_id = data.get('draft_id')
    transform_y = data.get('transform_y', 0)
    transform_x = data.get('transform_x', 0)
    font = data.get('font', "文轩体")
    font_color = data.get('color', data.get('font_color', "#FF0000"))
    font_size = data.get('size', data.get('font_size', 8.0))
    track_name = data.get('track_name', "text_main")
    align = data.get('align', 1)
    vertical = data.get('vertical', False)
    font_alpha = data.get('alpha', data.get('font_alpha', 1.0))
    outro_animation = data.get('outro_animation', None)
    outro_duration = data.get('outro_duration', 0.5)
    width = data.get('width', 1080)
    height = data.get('height', 1920)

    fixed_width = data.get('fixed_width', -1)
    fixed_height = data.get('fixed_height', -1)

    border_alpha = data.get('border_alpha', 1.0)
    border_color = data.get('border_color', "#000000")
    border_width = data.get('border_width', 0.0)

    background_color = data.get('background_color', "#000000")
    background_style = data.get('background_style', 0)
    background_alpha = data.get('background_alpha', 0.0)
    background_round_radius = data.get('background_round_radius', 0.0)
    background_height = data.get('background_height', 0.14)
    background_width = data.get('background_width', 0.14)
    background_horizontal_offset = data.get('background_horizontal_offset', 0.5)
    background_vertical_offset = data.get('background_vertical_offset', 0.5)

    shadow_enabled = data.get('shadow_enabled', False)
    shadow_alpha = data.get('shadow_alpha', 0.9)
    shadow_angle = data.get('shadow_angle', -45.0)
    shadow_color = data.get('shadow_color', "#000000")
    shadow_distance = data.get('shadow_distance', 5.0)
    shadow_smoothing = data.get('shadow_smoothing', 0.15)

    bubble_effect_id = data.get('bubble_effect_id')
    bubble_resource_id = data.get('bubble_resource_id')
    effect_effect_id = data.get('effect_effect_id')

    intro_animation = data.get('intro_animation')
    intro_duration = data.get('intro_duration', 0.5)

    outro_animation = data.get('outro_animation')
    outro_duration = data.get('outro_duration', 0.5)

    text_styles_data = data.get('text_styles', [])
    text_styles = None
    if text_styles_data:
        text_styles = []
        for style_data in text_styles_data:
            start_pos = style_data.get('start', 0)
            end_pos = style_data.get('end', 0)

            style = Text_style(
                size=style_data.get('style', {}).get('size', font_size),
                bold=style_data.get('style', {}).get('bold', False),
                italic=style_data.get('style', {}).get('italic', False),
                underline=style_data.get('style', {}).get('underline', False),
                color=hex_to_rgb(style_data.get('style', {}).get('color', font_color)),
                alpha=style_data.get('style', {}).get('alpha', font_alpha),
                align=style_data.get('style', {}).get('align', 1),
                vertical=style_data.get('style', {}).get('vertical', vertical),
                letter_spacing=style_data.get('style', {}).get('letter_spacing', 0),
                line_spacing=style_data.get('style', {}).get('line_spacing', 0)
            )

            border = None
            if style_data.get('border', {}).get('width', 0) > 0:
                border = Text_border(
                    alpha=style_data.get('border', {}).get('alpha', border_alpha),
                    color=hex_to_rgb(style_data.get('border', {}).get('color', border_color)),
                    width=style_data.get('border', {}).get('width', border_width)
                )

            style_range = TextStyleRange(
                start=start_pos,
                end=end_pos,
                style=style,
                border=border,
                font_str=style_data.get('font', font)
            )

            text_styles.append(style_range)

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not text or start is None or end is None:
        result["error"] = "Hi, the required parameters 'text', 'start' or 'end' are missing. "
        return jsonify(result)

    try:
        draft_result = add_text_impl(
            text=text,
            start=start,
            end=end,
            draft_id=draft_id,
            transform_y=transform_y,
            transform_x=transform_x,
            font=font,
            font_color=font_color,
            font_size=font_size,
            track_name=track_name,
            align=align,
            vertical=vertical,
            font_alpha=font_alpha,
            border_alpha=border_alpha,
            border_color=border_color,
            border_width=border_width,
            background_color=background_color,
            background_style=background_style,
            background_alpha=background_alpha,
            background_round_radius=background_round_radius,
            background_height=background_height,
            background_width=background_width,
            background_horizontal_offset=background_horizontal_offset,
            background_vertical_offset=background_vertical_offset,
            shadow_enabled=shadow_enabled,
            shadow_alpha=shadow_alpha,
            shadow_angle=shadow_angle,
            shadow_color=shadow_color,
            shadow_distance=shadow_distance,
            shadow_smoothing=shadow_smoothing,
            bubble_effect_id=bubble_effect_id,
            bubble_resource_id=bubble_resource_id,
            effect_effect_id=effect_effect_id,
            intro_animation=intro_animation,
            intro_duration=intro_duration,
            outro_animation=outro_animation,
            outro_duration=outro_duration,
            width=width,
            height=height,
            fixed_width=fixed_width,
            fixed_height=fixed_height,
            text_styles=text_styles
        )

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while processing text: {str(e)}. You can click the link below for help: "
        return jsonify(result)


