from collections import OrderedDict
import pyJianYingDraft as draft
from typing import Dict, Optional
import logging
from redis_draft_storage import get_redis_storage

logger = logging.getLogger(__name__)

# Keep in-memory cache for active drafts (faster access)
DRAFT_CACHE: Dict[str, 'draft.Script_file'] = OrderedDict()  # Use Dict for type hinting
MAX_CACHE_SIZE = 100  # Reduced size since Redis is primary storage

def update_cache(key: str, value: draft.Script_file) -> None:
    """Update cache in both memory and Redis"""
    try:
        # Update Redis storage (persistent)
        redis_storage = get_redis_storage()
        redis_storage.save_draft(key, value, ttl=86400)  # 24 hours TTL
        
        # Update in-memory cache (fast access)
        if key in DRAFT_CACHE:
            # If the key exists, delete the old item
            DRAFT_CACHE.pop(key)
        elif len(DRAFT_CACHE) >= MAX_CACHE_SIZE:
            print(f"{key}, Cache is full, deleting the least recently used item")
            # If the cache is full, delete the least recently used item (the first item)
            DRAFT_CACHE.popitem(last=False)
        # Add new item to the end (most recently used)
        DRAFT_CACHE[key] = value
        
        logger.info(f"Updated draft {key} in both Redis and memory cache")
        
    except Exception as e:
        logger.error(f"Failed to update cache for {key}: {e}")
        # Fallback to memory-only cache
        if key in DRAFT_CACHE:
            DRAFT_CACHE.pop(key)
        elif len(DRAFT_CACHE) >= MAX_CACHE_SIZE:
            DRAFT_CACHE.popitem(last=False)
        DRAFT_CACHE[key] = value

def get_from_cache(key: str) -> Optional[draft.Script_file]:
    """Get draft from cache (memory first, then Redis)"""
    try:
        # Try memory cache first (fastest)
        if key in DRAFT_CACHE:
            logger.debug(f"Retrieved draft {key} from memory cache")
            return DRAFT_CACHE[key]
        
        # Try Redis cache
        redis_storage = get_redis_storage()
        draft_obj = redis_storage.get_draft(key)
        
        if draft_obj is not None:
            # Add to memory cache for faster future access
            if len(DRAFT_CACHE) >= MAX_CACHE_SIZE:
                DRAFT_CACHE.popitem(last=False)
            DRAFT_CACHE[key] = draft_obj
            logger.info(f"Retrieved draft {key} from Redis and cached in memory")
            return draft_obj
        
        logger.warning(f"Draft {key} not found in any cache")
        return None
        
    except Exception as e:
        logger.error(f"Failed to get draft {key} from cache: {e}")
        # Fallback to memory cache only
        return DRAFT_CACHE.get(key)

def remove_from_cache(key: str) -> bool:
    """Remove draft from both memory and Redis cache"""
    try:
        redis_storage = get_redis_storage()
        redis_removed = redis_storage.delete_draft(key)
        
        memory_removed = key in DRAFT_CACHE
        if memory_removed:
            DRAFT_CACHE.pop(key)
        
        logger.info(f"Removed draft {key} from cache (Redis: {redis_removed}, Memory: {memory_removed})")
        return redis_removed or memory_removed
        
    except Exception as e:
        logger.error(f"Failed to remove draft {key} from cache: {e}")
        # Fallback to memory cache only
        if key in DRAFT_CACHE:
            DRAFT_CACHE.pop(key)
            return True
        return False

def cache_exists(key: str) -> bool:
    """Check if draft exists in cache"""
    try:
        if key in DRAFT_CACHE:
            return True
        
        redis_storage = get_redis_storage()
        return redis_storage.exists(key)
        
    except Exception as e:
        logger.error(f"Failed to check if draft {key} exists: {e}")
        return key in DRAFT_CACHE

def get_cache_stats() -> Dict:
    """Get cache statistics"""
    try:
        redis_storage = get_redis_storage()
        redis_stats = redis_storage.get_stats()
        
        return {
            'memory_cache_size': len(DRAFT_CACHE),
            'memory_cache_max': MAX_CACHE_SIZE,
            'redis_stats': redis_stats
        }
    except Exception as e:
        logger.error(f"Failed to get cache stats: {e}")
        return {
            'memory_cache_size': len(DRAFT_CACHE),
            'memory_cache_max': MAX_CACHE_SIZE,
            'redis_stats': {}
        }