from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
import logging

# Load environment variables from .env file BEFORE importing modules that may touch DB
env_file = Path(__file__).parent / ".env"
logger = logging.getLogger(__name__)
if not logging.getLogger().hasHandlers():
    logging.basicConfig(level=logging.INFO)
if env_file.exists():
    load_dotenv(env_file)
    logger.info(f"Loaded environment from: {env_file}")
else:
    logger.warning(f"Environment file not found: {env_file}")
    logger.info("Using default environment variables")

from settings.local import PORT  # noqa: E402
from api import register_blueprints  # noqa: E402
from db import init_db  # noqa: E402

app = Flask(__name__)
register_blueprints(app)
try:
    init_db()
    logger.info("Database initialization successful")
except Exception as e:
    logger.error(f"Database initialization failed: {e}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
