"""
API endpoints for managing drafts stored in PostgreSQL.
Add these endpoints to your Flask application.
"""

from flask import Blueprint, jsonify, request
import json
from postgres_draft_storage import get_postgres_storage
from draft_cache import get_cache_stats, remove_from_cache
import logging
import os
import hmac

logger = logging.getLogger(__name__)

# Create a blueprint for draft management
draft_bp = Blueprint('draft_management', __name__, url_prefix='/api/drafts')


def _get_configured_tokens():
    """Read expected API tokens from environment variables.

    Supports a single token (DRAFT_API_TOKEN/API_TOKEN/AUTH_TOKEN) or
    a comma-separated list in DRAFT_API_TOKENS.
    """
    tokens_env = os.getenv('DRAFT_API_TOKENS')
    single_token = (
        os.getenv('DRAFT_API_TOKEN')
        or os.getenv('API_TOKEN')
        or os.getenv('AUTH_TOKEN')
    )

    tokens = []
    if tokens_env:
        tokens.extend([t.strip() for t in tokens_env.split(',') if t.strip()])
    if single_token:
        tokens.append(single_token.strip())

    # Dedupe while preserving order
    unique: list[str] = []
    seen: set[str] = set()
    for token in tokens:
        if token and token not in seen:
            unique.append(token)
            seen.add(token)
    return unique


def _extract_token_from_request(req):
    """Extract bearer/API token from request headers or query params."""
    auth_header = req.headers.get('Authorization', '')
    if auth_header:
        parts = auth_header.split(None, 1)
        if len(parts) == 2 and parts[0].lower() in ('bearer', 'token'):
            return parts[1].strip()

    for header_name in ('X-API-Token', 'X-Auth-Token', 'X-Token'):
        header_val = req.headers.get(header_name)
        if header_val:
            return header_val.strip()

    # Optional fallback to query params for convenience
    token_param = req.args.get('api_token') or req.args.get('token')
    if token_param:
        return token_param.strip()

    return None


@draft_bp.before_request
def _require_authentication():
    """Protect all draft management endpoints with token authentication.

    Configure one of the following env vars for valid tokens:
      - DRAFT_API_TOKEN (single token)
      - DRAFT_API_TOKENS (comma-separated list)
    Fallbacks supported: API_TOKEN, AUTH_TOKEN

    Client should send the token via:
      - Authorization: Bearer <token>
      - X-API-Token: <token> (or X-Auth-Token / X-Token)
      - ?api_token=<token> (query param, not recommended)
    """
    expected_tokens = _get_configured_tokens()
    if not expected_tokens:
        logger.error("Draft management API token not configured. Set DRAFT_API_TOKEN or DRAFT_API_TOKENS.")
        return jsonify({
            'success': False,
            'error': 'Unauthorized: server missing token configuration'
        }), 401

    provided_token = _extract_token_from_request(request)
    if not provided_token:
        return jsonify({'success': False, 'error': 'Unauthorized: missing token'}), 401

    for expected in expected_tokens:
        if hmac.compare_digest(provided_token, expected):
            return None  # Authorized

    return jsonify({'success': False, 'error': 'Unauthorized: invalid token'}), 401

@draft_bp.route('/list', methods=['GET'])
def list_drafts():
    """List all stored drafts with metadata"""
    try:
        limit = request.args.get('limit', 100, type=int)
        pg_storage = get_postgres_storage()
        drafts = pg_storage.list_drafts(limit=limit)
        
        return jsonify({
            'success': True,
            'drafts': drafts,
            'count': len(drafts)
        })
    except Exception as e:
        logger.error(f"Failed to list drafts: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@draft_bp.route('/<draft_id>', methods=['GET'])
def get_draft_info(draft_id):
    """Get draft metadata without loading the full object"""
    try:
        pg_storage = get_postgres_storage()
        metadata = pg_storage.get_metadata(draft_id)
        
        if metadata is None:
            return jsonify({
                'success': False,
                'error': 'Draft not found'
            }), 404
        
        return jsonify({
            'success': True,
            'draft': metadata
        })
    except Exception as e:
        logger.error(f"Failed to get draft {draft_id}: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@draft_bp.route('/<draft_id>/content', methods=['GET'])
def get_draft_content(draft_id):
    """Fetch full draft content JSON stored in Postgres."""
    try:
        pg_storage = get_postgres_storage()
        script_obj = pg_storage.get_draft(draft_id)

        if script_obj is None:
            return jsonify({
                'success': False,
                'error': 'Draft not found'
            }), 404

        try:
            draft_content = json.loads(script_obj.dumps())
        except Exception as decode_err:
            logger.warning(f"Failed to decode draft {draft_id} to JSON object: {decode_err}")
            draft_content = script_obj.dumps()

        return jsonify({
            'success': True,
            'draft_id': draft_id,
            'content': draft_content
        })
    except Exception as e:
        logger.error(f"Failed to get draft content for {draft_id}: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@draft_bp.route('/<draft_id>', methods=['DELETE'])
def delete_draft(draft_id):
    """Delete a draft from cache and soft-delete from database"""
    try:
        cache_removed = remove_from_cache(draft_id)

        pg_storage = get_postgres_storage()
        db_deleted = pg_storage.delete_draft(draft_id)

        if cache_removed or db_deleted:
            return jsonify({
                'success': True,
                'message': f'Draft {draft_id} deleted (cache_removed={cache_removed}, db_deleted={db_deleted})'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Draft not found or could not be deleted'
            }), 404

    except Exception as e:
        logger.error(f"Failed to delete draft {draft_id}: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@draft_bp.route('/<draft_id>/exists', methods=['GET'])
def check_draft_exists(draft_id):
    """Check if a draft exists in storage"""
    try:
        pg_storage = get_postgres_storage()
        exists = pg_storage.exists(draft_id)
        
        return jsonify({
            'success': True,
            'exists': exists,
            'draft_id': draft_id
        })
    except Exception as e:
        logger.error(f"Failed to check if draft {draft_id} exists: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@draft_bp.route('/stats', methods=['GET'])
def get_storage_stats():
    """Get storage statistics"""
    try:
        stats = get_cache_stats()
        return jsonify({
            'success': True,
            'stats': stats
        })
    except Exception as e:
        logger.error(f"Failed to get storage stats: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@draft_bp.route('/cleanup', methods=['POST'])
def cleanup_expired():
    """Clean up expired or orphaned drafts"""
    try:
        pg_storage = get_postgres_storage()
        cleanup_count = pg_storage.cleanup_expired()
        
        return jsonify({
            'success': True,
            'message': f'Cleaned up {cleanup_count} expired drafts',
            'cleanup_count': cleanup_count
        })
    except Exception as e:
        logger.error(f"Failed to cleanup expired drafts: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@draft_bp.route('/search', methods=['GET'])
def search_drafts():
    """Search drafts by criteria"""
    try:
        # Get search parameters
        width = request.args.get('width', type=int)
        height = request.args.get('height', type=int)
        min_duration = request.args.get('min_duration', type=float)
        max_duration = request.args.get('max_duration', type=float)
        
        pg_storage = get_postgres_storage()
        all_drafts = pg_storage.list_drafts()
        
        # Filter drafts based on criteria
        filtered_drafts = []
        for draft in all_drafts:
            if width and draft.get('width') != width:
                continue
            if height and draft.get('height') != height:
                continue
            if min_duration and draft.get('duration', 0) < min_duration:
                continue
            if max_duration and draft.get('duration', 0) > max_duration:
                continue
            filtered_drafts.append(draft)
        
        return jsonify({
            'success': True,
            'drafts': filtered_drafts,
            'count': len(filtered_drafts),
            'total_drafts': len(all_drafts)
        })
    except Exception as e:
        logger.error(f"Failed to search drafts: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# Usage example for integrating with your Flask app:
"""
To add these endpoints to your Flask app (capcut_server.py), add:

from draft_management_api import draft_bp
app.register_blueprint(draft_bp)

Then you can use these endpoints:
- GET /api/drafts/list - List all drafts
- GET /api/drafts/<draft_id> - Get draft metadata
- DELETE /api/drafts/<draft_id> - Delete a draft
- GET /api/drafts/<draft_id>/exists - Check if draft exists
- GET /api/drafts/stats - Get storage statistics
- POST /api/drafts/cleanup - Clean up expired drafts
- GET /api/drafts/search?width=1080&height=1920 - Search drafts
"""
