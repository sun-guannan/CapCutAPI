"""
ORM models for Draft and VideoTask.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, LargeBinary, Text, DateTime, Float, Boolean
from sqlalchemy.dialects.postgresql import JSONB

from db import Base


class Draft(Base):
    __tablename__ = "drafts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    draft_id = Column(String(255), unique=True, index=True, nullable=False)

    # Serialized Script_file object (pickle bytes)
    data = Column(LargeBinary, nullable=False)

    # Quick access metadata
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    duration = Column(Integer, nullable=True)  # microseconds
    fps = Column(Float, nullable=True)
    version = Column(String(64), nullable=True)
    size_bytes = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    accessed_at = Column(DateTime, nullable=True)


class VideoTask(Base):
    __tablename__ = "video_tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(255), unique=True, index=True, nullable=False)
    draft_id = Column(String(255), index=True, nullable=False)

    # status: initialized, processing, completed, failed
    status = Column(String(64), index=True, nullable=False, default="initialized")
    progress = Column(Integer, nullable=True)
    message = Column(Text, nullable=True)
    draft_url = Column(Text, nullable=True)

    # arbitrary extra data (e.g., Celery IDs, etc.)
    extra = Column(JSONB, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


