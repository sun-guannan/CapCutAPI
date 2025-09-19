"""
SQLAlchemy database setup for PostgreSQL.
Reads DATABASE_URL from environment, provides Base, Session and init_db.
"""

import os
from contextlib import contextmanager
from typing import Iterator
import logging
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

logger = logging.getLogger(__name__)
Base = declarative_base()


# Load .env early so any importers that touch DB use the correct settings
_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    try:
        load_dotenv(_env_file)
        logger.info(f"Loaded environment from: {_env_file}")
    except Exception:
        # Best-effort; do not fail module import
        pass

def _database_url() -> str:
    url = os.getenv("DATABASE_URL")
    logger.info(f"DATABASE_URL: {url}")
    if url:
        return url
    # Fallback to individual parts if provided
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    dbname = os.getenv("POSTGRES_DB", "kox")
    logger.info(f"POSTGRES_USER: {user}, POSTGRES_PASSWORD: {password}, POSTGRES_HOST: {host}, POSTGRES_PORT: {port}, POSTGRES_DB: {dbname}")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"


def get_engine(echo: bool = False) -> Engine:
    dbEngine = create_engine(_database_url(), echo=echo, pool_pre_ping=True, future=True)
    logger.info(f"Engine: {dbEngine}")
    return dbEngine


@contextmanager
def get_session() -> Iterator[Session]:
    # Lazily create a sessionmaker bound to the current engine/env
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_db(engine: Engine | None = None) -> None:
    """Create tables if they do not exist."""
    eng = engine or get_engine()
    logger.info(f"Engine: {eng}")
    # Import models to ensure metadata is populated
    from models import Draft, VideoTask  # noqa: F401
    Base.metadata.create_all(bind=eng)
    # Simple connectivity check
    with eng.connect() as conn:
        conn.execute(text("SELECT 1"))
        conn.commit()


