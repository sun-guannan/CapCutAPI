from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
import logging
from settings.local import PORT
from api import register_blueprints
from db import init_db
import threading
from flask import request, Response
import requests as http
import uvicorn
from mcp_stream_server import create_fastmcp_app

# Load environment variables from .env file
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

app = Flask(__name__)
register_blueprints(app)
try:
    init_db()
except Exception as e:
    logger.error(f"Database initialization failed: {e}")

_MCP_HOST = "127.0.0.1"
_MCP_PORT = 3333

def _run_mcp_server():
    # Serve FastMCP Streamable HTTP at root path ("/") so Flask can map /mcp -> /
    mcp_app = create_fastmcp_app(host=_MCP_HOST, port=_MCP_PORT, path="/")
    asgi_app = mcp_app.streamable_http_app()
    uvicorn.run(asgi_app, host=_MCP_HOST, port=_MCP_PORT, log_level="info")

# Start the MCP server lazily on first request (Flask 3 removed before_first_request)
_mcp_started = False

@app.before_request
def _ensure_mcp_started():
    global _mcp_started
    if not _mcp_started:
        thr = threading.Thread(target=_run_mcp_server, name="mcp-uvicorn", daemon=True)
        thr.start()
        _mcp_started = True
        logger.info(f"Started embedded FastMCP on http://{_MCP_HOST}:{_MCP_PORT}/")

@app.route('/mcp', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
@app.route('/mcp/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def _proxy_mcp(path: str):
    target_url = f"http://{_MCP_HOST}:{_MCP_PORT}/{path}"
    headers = {k: v for k, v in request.headers if k.lower() != 'host'}
    resp = http.request(
        method=request.method,
        url=target_url,
        params=request.args,
        headers=headers,
        data=request.get_data(),
    )
    excluded = {'content-encoding', 'content-length', 'transfer-encoding', 'connection'}
    response_headers = [(k, v) for k, v in resp.headers.items() if k.lower() not in excluded]
    return Response(resp.content, status=resp.status_code, headers=response_headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
