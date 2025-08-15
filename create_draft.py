import uuid
import pyJianYingDraft as draft
import time
from draft_cache import update_cache, get_from_cache, cache_exists

def create_draft(width=1080, height=1920):
    """
    Create new CapCut draft
    :param width: Video width, default 1080
    :param height: Video height, default 1920
    :return: (draft_name, draft_path, draft_id, draft_url)
    """
    # Generate timestamp and draft_id
    unix_time = int(time.time())
    unique_id = uuid.uuid4().hex[:8]  # Take the first 8 digits of UUID
    draft_id = f"dfd_cat_{unix_time}_{unique_id}"  # Use Unix timestamp and UUID combination
    
    # Create CapCut draft with specified resolution
    script = draft.Script_file(width, height)
    
    # Store in global cache
    update_cache(draft_id, script)
    
    return script, draft_id

def get_or_create_draft(draft_id=None, width=1080, height=1920):
    """
    Get or create CapCut draft (now with Redis persistence)
    :param draft_id: Draft ID, if None or not found in storage, create new draft
    :param width: Video width, default 1080
    :param height: Video height, default 1920
    :return: (draft_id, script)
    """
    if draft_id is not None and cache_exists(draft_id):
        # Get existing draft from cache (memory or Redis)
        print(f"Getting draft from storage: {draft_id}")
        script = get_from_cache(draft_id)
        if script is not None:
            # Update last access time by re-saving
            update_cache(draft_id, script)
            return draft_id, script
        else:
            print(f"Failed to retrieve draft {draft_id}, creating new one")

    # Create new draft logic
    print("Creating new draft")
    script, generate_draft_id = create_draft(
        width=width,
        height=height,
    )
    return generate_draft_id, script
    