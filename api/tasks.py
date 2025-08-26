from flask import Blueprint, request, jsonify
import logging
from typing import Any, Dict

from sqlalchemy import select

from db import get_session
from models import VideoTask


logger = logging.getLogger(__name__)
bp = Blueprint('tasks', __name__)


@bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() or {}
    task_id = data.get('task_id')
    draft_id = data.get('draft_id')
    extra = data.get('extra')

    if not task_id or not draft_id:
        return jsonify({"success": False, "error": "task_id and draft_id are required"}), 400

    with get_session() as session:
        existing = session.execute(select(VideoTask).where(VideoTask.task_id == task_id)).scalar_one_or_none()
        if existing:
            return jsonify({"success": True, "output": {"task_id": existing.task_id}})

        row = VideoTask(task_id=task_id, draft_id=draft_id, status='initialized', extra=extra)
        session.add(row)

    return jsonify({"success": True, "output": {"task_id": task_id}})


@bp.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id: str):
    with get_session() as session:
        row = session.execute(select(VideoTask).where(VideoTask.task_id == task_id)).scalar_one_or_none()
        if not row:
            return jsonify({"success": False, "error": "not_found"}), 404
        return jsonify({
            "success": True,
            "output": {
                "task_id": row.task_id,
                "draft_id": row.draft_id,
                "status": row.status,
                "progress": row.progress,
                "message": row.message,
                "draft_url": row.draft_url,
                "extra": row.extra,
            }
        })


@bp.route('/tasks/<task_id>', methods=['PATCH'])
def update_task(task_id: str):
    data: Dict[str, Any] = request.get_json() or {}
    with get_session() as session:
        row = session.execute(select(VideoTask).where(VideoTask.task_id == task_id)).scalar_one_or_none()
        if not row:
            return jsonify({"success": False, "error": "not_found"}), 404

        allowed = {'status', 'progress', 'message', 'draft_url', 'extra'}
        for key, value in data.items():
            if key in allowed:
                setattr(row, key, value)

    return jsonify({"success": True, "output": {"task_id": task_id}})


@bp.route('/tasks/by_draft/<draft_id>', methods=['PATCH'])
def update_tasks_by_draft(draft_id: str):
    data: Dict[str, Any] = request.get_json() or {}
    with get_session() as session:
        rows = session.execute(select(VideoTask).where(VideoTask.draft_id == draft_id)).scalars().all()
        if not rows:
            return jsonify({"success": False, "error": "not_found"}), 404

        allowed = {'status', 'progress', 'message', 'draft_url', 'extra'}
        updates = {k: v for k, v in data.items() if k in allowed}
        if not updates:
            return jsonify({"success": False, "error": "no_valid_fields"}), 400

        for row in rows:
            for key, value in updates.items():
                setattr(row, key, value)

        updated_task_ids = [row.task_id for row in rows]

    return jsonify({
        "success": True,
        "output": {
            "updated": len(updated_task_ids),
            "task_ids": updated_task_ids,
            "draft_id": draft_id
        }
    })


