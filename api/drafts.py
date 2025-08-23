from flask import Blueprint, request, jsonify

from create_draft import create_draft, DraftFramerate
from save_draft_impl import save_draft_impl, query_task_status, query_script_impl
from util import generate_draft_url as utilgenerate_draft_url


bp = Blueprint('drafts', __name__)


@bp.route('/create_draft', methods=['POST'])
def create_draft_service():
    data = request.get_json()

    width = data.get('width', 1080)
    height = data.get('height', 1920)
    framerate = data.get('framerate', DraftFramerate.FR_30.value)
    name = data.get('name', "draft")

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    try:
        script, draft_id = create_draft(width=width, height=height, framerate=framerate, name=name)

        result["success"] = True
        result["output"] = {"draft_id": draft_id}
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while creating draft: {str(e)}."
        return jsonify(result)


@bp.route('/query_script', methods=['POST'])
def query_script():
    data = request.get_json()

    draft_id = data.get('draft_id')
    force_update = data.get('force_update', True)

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not draft_id:
        result["error"] = "Hi, the required parameter 'draft_id' is missing. Please add it and try again."
        return jsonify(result)

    try:
        script = query_script_impl(draft_id=draft_id, force_update=force_update)

        if script is None:
            result["error"] = f"Draft {draft_id} does not exist in cache."
            return jsonify(result)

        script_str = script.dumps()

        result["success"] = True
        result["output"] = script_str
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while querying script: {str(e)}. "
        return jsonify(result)


@bp.route('/save_draft', methods=['POST'])
def save_draft():
    data = request.get_json()

    draft_id = data.get('draft_id')
    draft_folder = data.get('draft_folder')

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not draft_id:
        result["error"] = "Hi, the required parameter 'draft_id' is missing. Please add it and try again."
        return jsonify(result)

    try:
        draft_result = save_draft_impl(draft_id, draft_folder)

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while saving draft: {str(e)}. "
        return jsonify(result)


@bp.route('/query_draft_status', methods=['POST'])
def query_draft_status_api():
    data = request.get_json()

    task_id = data.get('task_id')

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not task_id:
        result["error"] = "Hi, the required parameter 'task_id' is missing. Please add it and try again."
        return jsonify(result)

    try:
        task_status = query_task_status(task_id)

        if task_status["status"] == "not_found":
            result["error"] = f"Task with ID {task_id} not found. Please check if the task ID is correct."
            return jsonify(result)

        result["success"] = True
        result["output"] = task_status
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while querying task status: {str(e)}."
        return jsonify(result)


@bp.route('/generate_draft_url', methods=['POST'])
def generate_draft_url():
    from settings.local import DRAFT_DOMAIN, PREVIEW_ROUTER

    data = request.get_json()

    draft_id = data.get('draft_id')
    draft_folder = data.get('draft_folder')

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not draft_id:
        result["error"] = "Hi, the required parameter 'draft_id' is missing. Please add it and try again."
        return jsonify(result)

    try:
        draft_result = {"draft_url": f"{DRAFT_DOMAIN}{PREVIEW_ROUTER}?={draft_id}"}

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while saving draft: {str(e)}."
        return jsonify(result)


