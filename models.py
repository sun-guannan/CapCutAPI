"""
ORM models for Draft and VideoTask.
"""

from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, LargeBinary, Text, DateTime, Float, Enum as SAEnum, Boolean
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
    draft_name = Column(String(255), nullable=True)
    # Resource origin of the draft: 'api' or 'mcp'
    resource = Column(SAEnum('api', 'mcp', name='draft_resource'), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    accessed_at = Column(DateTime(timezone=True), nullable=True)

    # Soft delete flag
    is_deleted = Column(Boolean, nullable=False, default=False, index=True)


class VideoTask(Base):
    __tablename__ = "video_tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(255), unique=True, index=True, nullable=False)
    draft_id = Column(String(255), index=True, nullable=False)
    # Name of the video/draft at the time of task creation
    video_name = Column(String(255), nullable=True)

    # status: initialized, processing, completed, failed
    status = Column(String(64), index=True, nullable=False, default="initialized")
    progress = Column(Integer, nullable=True)
    message = Column(Text, nullable=True)
    draft_url = Column(Text, nullable=True)

    # arbitrary extra data (e.g., Celery IDs, etc.)
    extra = Column(JSONB, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


