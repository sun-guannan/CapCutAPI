from flask import Blueprint, request, jsonify

from add_effect_impl import add_effect_impl


bp = Blueprint('effects', __name__)


@bp.route('/add_effect', methods=['POST'])
def add_effect():
    data = request.get_json()

    effect_type = data.get('effect_type')
    start = data.get('start', 0)
    effect_category = data.get('effect_category', "scene")
    end = data.get('end', 3.0)
    draft_id = data.get('draft_id')
    track_name = data.get('track_name', "effect_01")
    params = data.get('params')
    width = data.get('width', 1080)
    height = data.get('height', 1920)

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not effect_type:
        result["error"] = "Hi, the required parameters 'effect_type' are missing. Please add them and try again."
        return jsonify(result)

    try:
        draft_result = add_effect_impl(
            effect_type=effect_type,
            effect_category=effect_category,
            start=start,
            end=end,
            draft_id=draft_id,
            track_name=track_name,
            params=params,
            width=width,
            height=height
        )

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while adding effect: {str(e)}. "
        return jsonify(result)


