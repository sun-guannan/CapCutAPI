from flask import Blueprint, jsonify
from datetime import datetime

from sqlalchemy import text
from db import get_engine


bp = Blueprint('health', __name__)


@bp.route('/health', methods=['GET'])
def health_check():
    try:
        db_status = "unknown"
        try:
            # Try opening a connection
            eng = get_engine()
            with eng.connect() as conn:
                conn.execute(text("SELECT 1"))
            db_status = "healthy"
        except Exception:
            db_status = "unavailable"

        health_info = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0",
            "services": {"postgres": db_status, "api": "healthy"},
        }

        return jsonify(health_info), 200

    except Exception as e:
        error_info = {"status": "unhealthy", "timestamp": datetime.now().isoformat(), "error": str(e)}
        return jsonify(error_info), 503


