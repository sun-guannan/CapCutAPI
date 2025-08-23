from flask import Blueprint, request, jsonify

from add_image_impl import add_image_impl


bp = Blueprint('image', __name__)


@bp.route('/add_image', methods=['POST'])
def add_image():
    data = request.get_json()

    draft_folder = data.get('draft_folder')
    image_url = data.get('image_url')
    width = data.get('width', 1080)
    height = data.get('height', 1920)
    start = data.get('start', 0)
    end = data.get('end', 3.0)
    draft_id = data.get('draft_id')
    transform_y = data.get('transform_y', 0)
    scale_x = data.get('scale_x', 1)
    scale_y = data.get('scale_y', 1)
    transform_x = data.get('transform_x', 0)
    track_name = data.get('track_name', "image_main")
    relative_index = data.get('relative_index', 0)
    animation = data.get('animation')
    animation_duration = data.get('animation_duration', 0.5)
    intro_animation = data.get('intro_animation')
    intro_animation_duration = data.get('intro_animation_duration', 0.5)
    outro_animation = data.get('outro_animation')
    outro_animation_duration = data.get('outro_animation_duration', 0.5)
    combo_animation = data.get('combo_animation')
    combo_animation_duration = data.get('combo_animation_duration', 0.5)
    transition = data.get('transition')
    transition_duration = data.get('transition_duration', 0.5)

    mask_type = data.get('mask_type')
    mask_center_x = data.get('mask_center_x', 0.0)
    mask_center_y = data.get('mask_center_y', 0.0)
    mask_size = data.get('mask_size', 0.5)
    mask_rotation = data.get('mask_rotation', 0.0)
    mask_feather = data.get('mask_feather', 0.0)
    mask_invert = data.get('mask_invert', False)
    mask_rect_width = data.get('mask_rect_width')
    mask_round_corner = data.get('mask_round_corner')

    background_blur = data.get('background_blur')

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not image_url:
        result["error"] = "Hi, the required parameters 'image_url' are missing."
        return jsonify(result)

    try:
        draft_result = add_image_impl(
            draft_folder=draft_folder,
            image_url=image_url,
            width=width,
            height=height,
            start=start,
            end=end,
            draft_id=draft_id,
            transform_y=transform_y,
            scale_x=scale_x,
            scale_y=scale_y,
            transform_x=transform_x,
            track_name=track_name,
            relative_index=relative_index,
            animation=animation,
            animation_duration=animation_duration,
            intro_animation=intro_animation,
            intro_animation_duration=intro_animation_duration,
            outro_animation=outro_animation,
            outro_animation_duration=outro_animation_duration,
            combo_animation=combo_animation,
            combo_animation_duration=combo_animation_duration,
            transition=transition,
            transition_duration=transition_duration,
            mask_type=mask_type,
            mask_center_x=mask_center_x,
            mask_center_y=mask_center_y,
            mask_size=mask_size,
            mask_rotation=mask_rotation,
            mask_feather=mask_feather,
            mask_invert=mask_invert,
            mask_rect_width=mask_rect_width,
            mask_round_corner=mask_round_corner,
            background_blur=background_blur
        )

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while processing image: {str(e)}."
        return jsonify(result)


