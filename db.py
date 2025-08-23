"""
SQLAlchemy database setup for PostgreSQL.
Reads DATABASE_URL from environment, provides Base, Session and init_db.
"""

import os
from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Session


Base = declarative_base()


def _database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if url:
        return url
    # Fallback to individual parts if provided
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    dbname = os.getenv("POSTGRES_DB", "kox")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"


def get_engine(echo: bool = False) -> Engine:
    return create_engine(_database_url(), echo=echo, pool_pre_ping=True, future=True)


# Thread-safe scoped session
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=get_engine()))


@contextmanager
def get_session() -> Iterator[Session]:
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
    # Import models to ensure metadata is populated
    from models import Draft, VideoTask  # noqa: F401
    Base.metadata.create_all(bind=eng)
    # Simple connectivity check
    with eng.connect() as conn:
        conn.execute(text("SELECT 1"))
        conn.commit()


