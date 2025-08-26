"""
PostgreSQL-backed storage for CapCut draft objects.
Retains a compatible interface with redis_draft_storage.RedisDraftStorage where practical.
"""

import json
import pickle
import logging
import time
from typing import Optional, Dict, Any
from datetime import datetime

import pyJianYingDraft as draft
from sqlalchemy import select, delete, update
from sqlalchemy.exc import SQLAlchemyError

from db import get_session, init_db
from models import Draft as DraftModel


logger = logging.getLogger(__name__)


class PostgresDraftStorage:
    def __init__(self) -> None:
        # Ensure tables exist
        try:
            init_db()
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise

    def save_draft(self, draft_id: str, script_obj: draft.Script_file) -> bool:
        try:
            serialized_data = pickle.dumps(script_obj)

            with get_session() as session:
                q = session.execute(select(DraftModel).where(DraftModel.draft_id == draft_id))
                existing = q.scalar_one_or_none()

                if existing is None:
                    row = DraftModel(
                        draft_id=draft_id,
                        data=serialized_data,
                        width=getattr(script_obj, 'width', None),
                        height=getattr(script_obj, 'height', None),
                        duration=getattr(script_obj, 'duration', None),
                        fps=getattr(script_obj, 'fps', None),
                        version=getattr(script_obj, 'version', '1.0'),
                        size_bytes=len(serialized_data),
                        accessed_at=datetime.utcnow(),
                    )
                    session.add(row)
                else:
                    existing.data = serialized_data
                    existing.width = getattr(script_obj, 'width', None)
                    existing.height = getattr(script_obj, 'height', None)
                    existing.duration = getattr(script_obj, 'duration', None)
                    existing.fps = getattr(script_obj, 'fps', None)
                    existing.version = getattr(script_obj, 'version', '1.0')
                    existing.size_bytes = len(serialized_data)
                    existing.accessed_at = datetime.utcnow()

            logger.info(f"Successfully saved draft {draft_id} to Postgres (size: {len(serialized_data)} bytes)")
            return True
        except SQLAlchemyError as e:
            logger.error(f"Database error saving draft {draft_id}: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to save draft {draft_id}: {e}")
            return False

    def get_draft(self, draft_id: str) -> Optional[draft.Script_file]:
        try:
            with get_session() as session:
                q = session.execute(select(DraftModel).where(DraftModel.draft_id == draft_id))
                row = q.scalar_one_or_none()
                if row is None:
                    logger.warning(f"Draft {draft_id} not found in Postgres")
                    return None
                script_obj = pickle.loads(row.data)
                row.accessed_at = datetime.utcnow()
                return script_obj
        except SQLAlchemyError as e:
            logger.error(f"Database error retrieving draft {draft_id}: {e}")
            return None
        except Exception as e:
            logger.error(f"Failed to retrieve draft {draft_id}: {e}")
            return None

    def exists(self, draft_id: str) -> bool:
        try:
            with get_session() as session:
                q = session.execute(select(DraftModel.id).where(DraftModel.draft_id == draft_id))
                return q.scalar_one_or_none() is not None
        except Exception as e:
            logger.error(f"Failed to check existence of draft {draft_id}: {e}")
            return False

    def delete_draft(self, draft_id: str) -> bool:
        try:
            with get_session() as session:
                result = session.execute(delete(DraftModel).where(DraftModel.draft_id == draft_id))
                return result.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to delete draft {draft_id}: {e}")
            return False

    def get_metadata(self, draft_id: str) -> Optional[Dict[str, Any]]:
        try:
            with get_session() as session:
                q = session.execute(select(DraftModel).where(DraftModel.draft_id == draft_id))
                row = q.scalar_one_or_none()
                if row is None:
                    return None
                return {
                    'draft_id': row.draft_id,
                    'width': row.width,
                    'height': row.height,
                    'duration': row.duration,
                    'fps': row.fps,
                    'created_at': int(row.created_at.timestamp()),
                    'updated_at': int(row.updated_at.timestamp()),
                    'version': row.version,
                    'size_bytes': row.size_bytes,
                    'accessed_at': int(row.accessed_at.timestamp()) if row.accessed_at else None,
                }
        except Exception as e:
            logger.error(f"Failed to get metadata for draft {draft_id}: {e}")
            return None

    def list_drafts(self, limit: int = 100) -> list:
        try:
            with get_session() as session:
                q = session.execute(
                    select(DraftModel).order_by(DraftModel.updated_at.desc()).limit(limit)
                )
                rows = q.scalars().all()
                results = []
                for row in rows:
                    results.append({
                        'draft_id': row.draft_id,
                        'width': row.width,
                        'height': row.height,
                        'duration': row.duration,
                        'fps': row.fps,
                        'created_at': int(row.created_at.timestamp()),
                        'updated_at': int(row.updated_at.timestamp()),
                        'version': row.version,
                        'size_bytes': row.size_bytes,
                    })
                return results
        except Exception as e:
            logger.error(f"Failed to list drafts: {e}")
            return []

    def cleanup_expired(self) -> int:
        # TTL semantics are not supported here; return 0 for compatibility
        return 0

    def get_stats(self) -> Dict[str, Any]:
        try:
            with get_session() as session:
                total = session.execute(select(DraftModel.id)).scalars().all()
                return {
                    'total_drafts': len(total),
                    'backend': 'postgresql'
                }
        except Exception as e:
            logger.error(f"Failed to get storage stats: {e}")
            return {}


# Global instance for easy import
pg_storage: Optional[PostgresDraftStorage] = None


def get_postgres_storage() -> PostgresDraftStorage:
    global pg_storage
    if pg_storage is None:
        pg_storage = PostgresDraftStorage()
    return pg_storage


