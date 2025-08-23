from flask import Blueprint, request, jsonify

from add_subtitle_impl import add_subtitle_impl


bp = Blueprint('subtitle', __name__)


@bp.route('/add_subtitle', methods=['POST'])
def add_subtitle():
    data = request.get_json()

    srt = data.get('srt')
    draft_id = data.get('draft_id')
    time_offset = data.get('time_offset', 0.0)

    font = data.get('font', "思源粗宋")
    font_size = data.get('font_size', 5.0)
    bold = data.get('bold', False)
    italic = data.get('italic', False)
    underline = data.get('underline', False)
    font_color = data.get('font_color', '#FFFFFF')
    vertical = data.get('vertical', False)
    alpha = data.get('alpha', 1)

    border_alpha = data.get('border_alpha', 1.0)
    border_color = data.get('border_color', '#000000')
    border_width = data.get('border_width', 0.0)

    background_color = data.get('background_color', '#000000')
    background_style = data.get('background_style', 0)
    background_alpha = data.get('background_alpha', 0.0)

    transform_x = data.get('transform_x', 0.0)
    transform_y = data.get('transform_y', -0.8)
    scale_x = data.get('scale_x', 1.0)
    scale_y = data.get('scale_y', 1.0)
    rotation = data.get('rotation', 0.0)
    track_name = data.get('track_name', 'subtitle')
    width = data.get('width', 1080)
    height = data.get('height', 1920)

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not srt:
        result["error"] = "Hi, the required parameters 'srt' are missing."
        return jsonify(result)

    try:
        draft_result = add_subtitle_impl(
            srt_path=srt,
            draft_id=draft_id,
            track_name=track_name,
            time_offset=time_offset,
            font=font,
            font_size=font_size,
            bold=bold,
            italic=italic,
            underline=underline,
            font_color=font_color,
            vertical=vertical,
            alpha=alpha,
            border_alpha=border_alpha,
            border_color=border_color,
            border_width=border_width,
            background_color=background_color,
            background_style=background_style,
            background_alpha=background_alpha,
            transform_x=transform_x,
            transform_y=transform_y,
            scale_x=scale_x,
            scale_y=scale_y,
            rotation=rotation,
            width=width,
            height=height
        )

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while processing subtitle: {str(e)}."
        return jsonify(result)


