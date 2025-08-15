"""
Redis configuration settings for draft storage.
"""

import os
from typing import Optional

# Redis connection settings
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_DRAFT_DB = int(os.getenv('REDIS_DRAFT_DB', 1))  # Separate from Celery (db=0)

# Draft storage settings
DRAFT_TTL_SECONDS = int(os.getenv('DRAFT_TTL_SECONDS', 86400))  # 24 hours default
MEMORY_CACHE_SIZE = int(os.getenv('MEMORY_CACHE_SIZE', 100))

# Redis connection pool settings
REDIS_SOCKET_TIMEOUT = int(os.getenv('REDIS_SOCKET_TIMEOUT', 5))
REDIS_SOCKET_CONNECT_TIMEOUT = int(os.getenv('REDIS_SOCKET_CONNECT_TIMEOUT', 5))

def get_redis_url() -> str:
    """Get Redis URL for connection"""
    if REDIS_PASSWORD:
        return f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DRAFT_DB}"
    else:
        return f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DRAFT_DB}"

def print_redis_config():
    """Print current Redis configuration"""
    print("Redis Configuration:")
    print(f"  Host: {REDIS_HOST}")
    print(f"  Port: {REDIS_PORT}")
    print(f"  Database: {REDIS_DRAFT_DB}")
    print(f"  Password: {'***' if REDIS_PASSWORD else 'None'}")
    print(f"  Draft TTL: {DRAFT_TTL_SECONDS} seconds")
    print(f"  Memory Cache Size: {MEMORY_CACHE_SIZE}")
