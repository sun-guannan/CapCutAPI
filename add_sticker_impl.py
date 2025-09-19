import pyJianYingDraft as draft
from pyJianYingDraft import trange
from typing import Dict
from pyJianYingDraft import exceptions
from create_draft import get_or_create_draft
from util import generate_draft_url
from draft_cache import update_cache

def add_sticker_impl(
    resource_id: str,
    start: float,
    end: float,
    draft_id: str = None,
    transform_y: float = 0,
    transform_x: float = 0,
    alpha: float = 1.0,
    flip_horizontal: bool = False,
    flip_vertical: bool = False,
    rotation: float = 0.0,
    scale_x: float = 1.0,
    scale_y: float = 1.0,
    track_name: str = "sticker_main",
    relative_index: int = 0,
    width: int = 1080,
    height: int = 1920
) -> Dict[str, str]:
    """
    Add sticker to specified draft
    :param resource_id: Sticker resource ID
    :param start: Start time (seconds)
    :param end: End time (seconds)
    :param draft_id: Draft ID (optional, default None creates a new draft)
    :param transform_y: Y-axis position (default 0, screen center)
    :param transform_x: X-axis position (default 0, screen center)
    :param alpha: Image opacity, range 0-1 (default 1.0, completely opaque)
    :param flip_horizontal: Whether to flip horizontally (default False)
    :param flip_vertical: Whether to flip vertically (default False)
    :param rotation: Clockwise rotation angle, can be positive or negative (default 0.0)
    :param scale_x: Horizontal scale ratio (default 1.0)
    :param scale_y: Vertical scale ratio (default 1.0)
    :param track_name: Track name
    :param relative_index: Relative layer position (of the same track type), higher is closer to foreground (default 0)
    :param width: Video width, default 1080
    :param height: Video height, default 1920
    :return: Updated draft information
    """
    # Get or create draft
    draft_id, script = get_or_create_draft(
        draft_id=draft_id,
        width=width,
        height=height
    )

    # Add sticker track
    if track_name is not None:
        try:
            imported_track = script.get_imported_track(draft.Track_type.sticker, name=track_name)
            # If no exception is thrown, the track already exists
        except exceptions.TrackNotFound:
            # Track doesn't exist, create a new track
            script.add_track(draft.Track_type.sticker, track_name=track_name, relative_index=relative_index)
    else:
        script.add_track(draft.Track_type.sticker, relative_index=relative_index)
    
    # Create sticker segment
    sticker_segment = draft.Sticker_segment(
        resource_id,
        trange(f"{start}s", f"{end-start}s"),
        clip_settings=draft.Clip_settings(
            transform_y=transform_y,
            transform_x=transform_x,
            alpha=alpha,
            flip_horizontal=flip_horizontal,
            flip_vertical=flip_vertical,
            rotation=rotation,
            scale_x=scale_x,
            scale_y=scale_y
        )
    )

    # Add sticker segment to track
    script.add_segment(sticker_segment, track_name=track_name)

    # Persist updated script to PostgreSQL and cache
    update_cache(draft_id, script)

    return {
        "draft_id": draft_id,
        # "draft_url": generate_draft_url(draft_id)
    }
