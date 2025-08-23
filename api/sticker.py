from flask import Blueprint, request, jsonify

from add_sticker_impl import add_sticker_impl


bp = Blueprint('sticker', __name__)


@bp.route('/add_sticker', methods=['POST'])
def add_sticker():
    data = request.get_json()

    resource_id = data.get('sticker_id')
    start = data.get('start', 0)
    end = data.get('end', 5.0)
    draft_id = data.get('draft_id')
    transform_y = data.get('transform_y', 0)
    transform_x = data.get('transform_x', 0)
    alpha = data.get('alpha', 1.0)
    flip_horizontal = data.get('flip_horizontal', False)
    flip_vertical = data.get('flip_vertical', False)
    rotation = data.get('rotation', 0.0)
    scale_x = data.get('scale_x', 1.0)
    scale_y = data.get('scale_y', 1.0)
    track_name = data.get('track_name', 'sticker_main')
    relative_index = data.get('relative_index', 0)
    width = data.get('width', 1080)
    height = data.get('height', 1920)

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not resource_id:
        result["error"] = "Hi, the required parameter 'sticker_id' is missing. Please add it and try again. "
        return jsonify(result)

    try:
        draft_result = add_sticker_impl(
            resource_id=resource_id,
            start=start,
            end=end,
            draft_id=draft_id,
            transform_y=transform_y,
            transform_x=transform_x,
            alpha=alpha,
            flip_horizontal=flip_horizontal,
            flip_vertical=flip_vertical,
            rotation=rotation,
            scale_x=scale_x,
            scale_y=scale_y,
            track_name=track_name,
            relative_index=relative_index,
            width=width,
            height=height
        )

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while adding sticker: {str(e)}. "
        return jsonify(result)


