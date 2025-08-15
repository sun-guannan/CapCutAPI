"""
API endpoints for managing drafts stored in Redis.
Add these endpoints to your Flask application.
"""

from flask import Blueprint, jsonify, request
from redis_draft_storage import get_redis_storage
from draft_cache import get_cache_stats, remove_from_cache
import logging

logger = logging.getLogger(__name__)

# Create a blueprint for draft management
draft_bp = Blueprint('draft_management', __name__, url_prefix='/api/drafts')

@draft_bp.route('/list', methods=['GET'])
def list_drafts():
    """List all stored drafts with metadata"""
    try:
        limit = request.args.get('limit', 100, type=int)
        redis_storage = get_redis_storage()
        drafts = redis_storage.list_drafts(limit=limit)
        
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
        redis_storage = get_redis_storage()
        metadata = redis_storage.get_metadata(draft_id)
        
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

@draft_bp.route('/<draft_id>', methods=['DELETE'])
def delete_draft(draft_id):
    """Delete a draft from storage"""
    try:
        success = remove_from_cache(draft_id)
        
        if success:
            return jsonify({
                'success': True,
                'message': f'Draft {draft_id} deleted successfully'
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
        redis_storage = get_redis_storage()
        exists = redis_storage.exists(draft_id)
        
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
        redis_storage = get_redis_storage()
        cleanup_count = redis_storage.cleanup_expired()
        
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
        
        redis_storage = get_redis_storage()
        all_drafts = redis_storage.list_drafts()
        
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
