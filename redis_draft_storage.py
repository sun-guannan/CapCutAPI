"""
Redis-based draft storage for CapCut drafts.
Provides persistent storage for draft objects with caching capabilities.
"""

import json
import pickle
import redis
import logging
import time
from typing import Optional, Dict, Any
from datetime import datetime, timedelta
import pyJianYingDraft as draft

logger = logging.getLogger(__name__)

class RedisDraftStorage:
    """Redis-based storage for CapCut draft objects"""
    
    def __init__(self, 
                 host: str = 'localhost', 
                 port: int = 6379, 
                 db: int = 1,  # Use db=1 to separate from Celery (which uses db=0)
                 password: str = None,
                 decode_responses: bool = False):
        """
        Initialize Redis connection
        
        Args:
            host: Redis server host
            port: Redis server port  
            db: Redis database number (use 1 to avoid conflict with Celery)
            password: Redis password if authentication is required
            decode_responses: Whether to decode responses (keep False for binary data)
        """
        try:
            self.redis_client = redis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
                decode_responses=decode_responses,
                socket_timeout=5,
                socket_connect_timeout=5,
                retry_on_timeout=True
            )
            # Test connection
            self.redis_client.ping()
            logger.info(f"Connected to Redis at {host}:{port} db={db}")
        except redis.ConnectionError as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise
        except Exception as e:
            logger.error(f"Redis initialization error: {e}")
            raise
    
    def _draft_key(self, draft_id: str) -> str:
        """Generate Redis key for draft data"""
        return f"draft:data:{draft_id}"
    
    def _meta_key(self, draft_id: str) -> str:
        """Generate Redis key for draft metadata"""
        return f"draft:meta:{draft_id}"
    
    def _index_key(self) -> str:
        """Generate Redis key for draft index"""
        return "draft:index"
    
    def save_draft(self, draft_id: str, script_obj: draft.Script_file, ttl: Optional[int] = None) -> bool:
        """
        Save draft to Redis
        
        Args:
            draft_id: Unique draft identifier
            script_obj: Draft script object
            ttl: Time to live in seconds (None = no expiration)
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            # Serialize the script object using pickle for full object preservation
            serialized_data = pickle.dumps(script_obj)
            
            # Save draft data
            draft_key = self._draft_key(draft_id)
            if ttl:
                self.redis_client.setex(draft_key, ttl, serialized_data)
            else:
                self.redis_client.set(draft_key, serialized_data)
            
            # Save metadata for quick queries
            metadata = {
                'draft_id': draft_id,
                'width': script_obj.width,
                'height': script_obj.height,
                'duration': script_obj.duration,
                'fps': script_obj.fps,
                'created_at': time.time(),
                'updated_at': time.time(),
                'version': getattr(script_obj, 'version', '1.0'),
                'size_bytes': len(serialized_data)
            }
            
            meta_key = self._meta_key(draft_id)
            if ttl:
                self.redis_client.setex(meta_key, ttl, json.dumps(metadata))
            else:
                self.redis_client.set(meta_key, json.dumps(metadata))
            
            # Add to index for listing drafts
            self.redis_client.sadd(self._index_key(), draft_id)
            
            logger.info(f"Successfully saved draft {draft_id} to Redis (size: {len(serialized_data)} bytes)")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save draft {draft_id} to Redis: {e}")
            return False
    
    def get_draft(self, draft_id: str) -> Optional[draft.Script_file]:
        """
        Retrieve draft from Redis
        
        Args:
            draft_id: Unique draft identifier
            
        Returns:
            Script_file object if found, None otherwise
        """
        try:
            draft_key = self._draft_key(draft_id)
            serialized_data = self.redis_client.get(draft_key)
            
            if serialized_data is None:
                logger.warning(f"Draft {draft_id} not found in Redis")
                return None
            
            # Deserialize the script object
            script_obj = pickle.loads(serialized_data)
            
            # Update access time in metadata
            self._update_access_time(draft_id)
            
            logger.info(f"Successfully retrieved draft {draft_id} from Redis")
            return script_obj
            
        except Exception as e:
            logger.error(f"Failed to retrieve draft {draft_id} from Redis: {e}")
            return None
    
    def exists(self, draft_id: str) -> bool:
        """Check if draft exists in Redis"""
        try:
            return bool(self.redis_client.exists(self._draft_key(draft_id)))
        except Exception as e:
            logger.error(f"Failed to check if draft {draft_id} exists: {e}")
            return False
    
    def delete_draft(self, draft_id: str) -> bool:
        """
        Delete draft from Redis
        
        Args:
            draft_id: Unique draft identifier
            
        Returns:
            bool: True if deleted successfully, False otherwise
        """
        try:
            draft_key = self._draft_key(draft_id)
            meta_key = self._meta_key(draft_id)
            
            # Delete data and metadata
            deleted_count = self.redis_client.delete(draft_key, meta_key)
            
            # Remove from index
            self.redis_client.srem(self._index_key(), draft_id)
            
            success = deleted_count > 0
            if success:
                logger.info(f"Successfully deleted draft {draft_id} from Redis")
            else:
                logger.warning(f"Draft {draft_id} was not found for deletion")
                
            return success
            
        except Exception as e:
            logger.error(f"Failed to delete draft {draft_id} from Redis: {e}")
            return False
    
    def get_metadata(self, draft_id: str) -> Optional[Dict[str, Any]]:
        """Get draft metadata without loading the full object"""
        try:
            meta_key = self._meta_key(draft_id)
            metadata_json = self.redis_client.get(meta_key)
            
            if metadata_json is None:
                return None
                
            return json.loads(metadata_json.decode('utf-8') if isinstance(metadata_json, bytes) else metadata_json)
            
        except Exception as e:
            logger.error(f"Failed to get metadata for draft {draft_id}: {e}")
            return None
    
    def list_drafts(self, limit: int = 100) -> list:
        """
        List all draft IDs and their metadata
        
        Args:
            limit: Maximum number of drafts to return
            
        Returns:
            List of draft metadata dictionaries
        """
        try:
            draft_ids = list(self.redis_client.smembers(self._index_key()))
            drafts = []
            
            for draft_id in draft_ids[:limit]:
                if isinstance(draft_id, bytes):
                    draft_id = draft_id.decode('utf-8')
                    
                metadata = self.get_metadata(draft_id)
                if metadata:
                    drafts.append(metadata)
            
            # Sort by updated_at descending
            drafts.sort(key=lambda x: x.get('updated_at', 0), reverse=True)
            return drafts
            
        except Exception as e:
            logger.error(f"Failed to list drafts: {e}")
            return []
    
    def cleanup_expired(self) -> int:
        """
        Clean up drafts that have expired or are orphaned
        
        Returns:
            Number of drafts cleaned up
        """
        try:
            cleanup_count = 0
            draft_ids = list(self.redis_client.smembers(self._index_key()))
            
            for draft_id in draft_ids:
                if isinstance(draft_id, bytes):
                    draft_id = draft_id.decode('utf-8')
                
                # Check if draft data still exists
                if not self.redis_client.exists(self._draft_key(draft_id)):
                    # Remove from index if data is missing
                    self.redis_client.srem(self._index_key(), draft_id)
                    self.redis_client.delete(self._meta_key(draft_id))
                    cleanup_count += 1
                    logger.info(f"Cleaned up orphaned draft {draft_id}")
            
            logger.info(f"Cleanup completed: {cleanup_count} drafts removed")
            return cleanup_count
            
        except Exception as e:
            logger.error(f"Failed to cleanup expired drafts: {e}")
            return 0
    
    def _update_access_time(self, draft_id: str):
        """Update the access time in metadata"""
        try:
            metadata = self.get_metadata(draft_id)
            if metadata:
                metadata['accessed_at'] = time.time()
                meta_key = self._meta_key(draft_id)
                self.redis_client.set(meta_key, json.dumps(metadata))
        except Exception as e:
            logger.error(f"Failed to update access time for draft {draft_id}: {e}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get storage statistics"""
        try:
            draft_count = self.redis_client.scard(self._index_key())
            
            # Get total memory usage (approximate)
            info = self.redis_client.info('memory')
            memory_usage = info.get('used_memory', 0)
            
            return {
                'total_drafts': draft_count,
                'memory_usage_bytes': memory_usage,
                'memory_usage_mb': round(memory_usage / (1024 * 1024), 2),
                'redis_info': {
                    'version': self.redis_client.info('server').get('redis_version'),
                    'connected_clients': self.redis_client.info('clients').get('connected_clients'),
                    'used_memory_human': info.get('used_memory_human')
                }
            }
        except Exception as e:
            logger.error(f"Failed to get storage stats: {e}")
            return {}

# Global instance for easy import
redis_storage = None

def get_redis_storage() -> RedisDraftStorage:
    """Get or create the global Redis storage instance"""
    global redis_storage
    if redis_storage is None:
        # Try to get Redis configuration from environment
        import os
        host = os.getenv('REDIS_HOST', 'localhost')
        port = int(os.getenv('REDIS_PORT', 6379))
        password = os.getenv('REDIS_PASSWORD', None)
        db = int(os.getenv('REDIS_DRAFT_DB', 1))  # Separate from Celery
        
        redis_storage = RedisDraftStorage(
            host=host,
            port=port,
            password=password,
            db=db
        )
    return redis_storage
