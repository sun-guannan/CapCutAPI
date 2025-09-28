import os
import json
import logging

from flask import Blueprint, request, jsonify

from create_draft import create_draft, DraftFramerate
from save_draft_impl import save_draft_impl, query_task_status, query_script_impl
# from util import generate_draft_url as utilgenerate_draft_url


bp = Blueprint('drafts', __name__)
logger = logging.getLogger(__name__)


@bp.route('/create_draft', methods=['POST'])
def create_draft_service():
    data = request.get_json()

    width = data.get('width', 1080)
    height = data.get('height', 1920)
    framerate = data.get('framerate', DraftFramerate.FR_30.value)
    name = data.get('name', "draft")
    resource = data.get('resource')  # 'api' or 'mcp'

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    try:
        script, draft_id = create_draft(width=width, height=height, framerate=framerate, name=name, resource=resource)

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
    draft_folder = data.get('draft_folder')  # noqa: F841

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


@bp.route('/archive_draft', methods=['POST'])
def archive_draft():
    data = request.get_json() or {}

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
        from celery import Celery

        broker_url = os.getenv('CELERY_BROKER_URL') or os.getenv('REDIS_URL')
        backend_url = os.getenv('CELERY_RESULT_BACKEND') or os.getenv('REDIS_URL')

        if not broker_url or not backend_url:
            result["error"] = "CELERY_BROKER_URL and CELERY_RESULT_BACKEND environment variables are required"
            return jsonify(result)

        celery_client = Celery(broker=broker_url, backend=backend_url)
        try:
            insp = celery_client.control.inspect(timeout=1)
            ping_result = insp.ping() if insp else None
        except Exception:
            ping_result = None
        if not ping_result:
            logger.warning("No Celery workers responded to ping. Verify worker is running and connected to the same broker/result backend.")

        script = query_script_impl(draft_id=draft_id, force_update=False)
        if script is None:
            result["error"] = f"Draft {draft_id} not found in cache. Please create or save the draft first."
            return jsonify(result)

        draft_content = json.loads(script.dumps())

        archive_sig = celery_client.signature(
            's3_asset_downloader.tasks.archive_draft_directory',
            kwargs={'draft_content': draft_content, 'assets_path': draft_folder},
            queue='default'
        )

        async_result = archive_sig.apply_async()
        task_id = async_result.id
        logger.info(f"Dispatched archive_draft_directory task. Task id: {task_id}")

        result["success"] = True
        result["output"] = {"task_id": task_id}
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while archiving draft: {str(e)}"
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


