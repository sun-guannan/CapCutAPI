from flask import Blueprint, request, jsonify

from add_audio_track import add_audio_track


bp = Blueprint('audio', __name__)


@bp.route('/add_audio', methods=['POST'])
def add_audio():
    data = request.get_json()

    draft_folder = data.get('draft_folder')
    audio_url = data.get('audio_url')
    start = data.get('start', 0)
    end = data.get('end', None)
    draft_id = data.get('draft_id')
    volume = data.get('volume', 1.0)
    target_start = data.get('target_start', 0)
    speed = data.get('speed', 1.0)
    track_name = data.get('track_name', 'audio_main')
    duration = data.get('duration', None)
    effect_type = data.get('effect_type', None)
    effect_params = data.get('effect_params', None)
    width = data.get('width', 1080)
    height = data.get('height', 1920)

    sound_effects = None
    if effect_type is not None:
        sound_effects = [(effect_type, effect_params)]

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not audio_url:
        result["error"] = "Hi, the required parameters 'audio_url' are missing."
        return jsonify(result)

    try:
        draft_result = add_audio_track(
            draft_folder=draft_folder,
            audio_url=audio_url,
            start=start,
            end=end,
            target_start=target_start,
            draft_id=draft_id,
            volume=volume,
            track_name=track_name,
            speed=speed,
            sound_effects=sound_effects,
            width=width,
            height=height,
            duration=duration
        )

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while processing audio: {str(e)}."
        return jsonify(result)


