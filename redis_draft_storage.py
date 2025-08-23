"""
Compatibility layer that provides the same API as the previous Redis-based draft storage,
but persists data in PostgreSQL via SQLAlchemy.
"""

import logging
from typing import Optional, Dict, Any
import pyJianYingDraft as draft

from postgres_draft_storage import get_postgres_storage, PostgresDraftStorage


logger = logging.getLogger(__name__)


class RedisDraftStorage:
    """Shim class delegating to PostgresDraftStorage, preserving public methods."""

    def __init__(self, *args, **kwargs):
        self._delegate: PostgresDraftStorage = get_postgres_storage()
        # Kept for backward compat where code might access attribute existence
        self.redis_client = None

    def save_draft(self, draft_id: str, script_obj: draft.Script_file, ttl: Optional[int] = None) -> bool:
        return self._delegate.save_draft(draft_id, script_obj, ttl)

    def get_draft(self, draft_id: str) -> Optional[draft.Script_file]:
        return self._delegate.get_draft(draft_id)

    def exists(self, draft_id: str) -> bool:
        return self._delegate.exists(draft_id)

    def delete_draft(self, draft_id: str) -> bool:
        return self._delegate.delete_draft(draft_id)

    def get_metadata(self, draft_id: str) -> Optional[Dict[str, Any]]:
        return self._delegate.get_metadata(draft_id)

    def list_drafts(self, limit: int = 100) -> list:
        return self._delegate.list_drafts(limit)

    def cleanup_expired(self) -> int:
        return self._delegate.cleanup_expired()

    def get_stats(self) -> Dict[str, Any]:
        stats = self._delegate.get_stats()
        stats['backend'] = 'postgresql'
        return stats


# Global instance for easy import
redis_storage = None


def get_redis_storage() -> RedisDraftStorage:
    """Return a singleton shim that uses PostgreSQL under the hood."""
    global redis_storage
    if redis_storage is None:
        redis_storage = RedisDraftStorage()
    return redis_storage
