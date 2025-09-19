import pyJianYingDraft as draft
from util import generate_draft_url, hex_to_rgb
from draft_cache import update_cache
from create_draft import get_or_create_draft
from pyJianYingDraft.text_segment import TextBubble, TextEffect
from typing import Optional
import requests
import os

def add_subtitle_impl(
    srt_path: str,
    draft_id: str = None,
    track_name: str = "subtitle",
    time_offset: float = 0,
    # Font style parameters
    font: str = None,
    font_size: float = 8.0,
    bold: bool = False,
    italic: bool = False,
    underline: bool = False,
    font_color: str = "#FFFFFF",
    
    # Border parameters
    border_alpha: float = 1.0,
    border_color: str = "#000000",
    border_width: float = 0.0,  # Default no border display
    
    # Background parameters
    background_color: str = "#000000",
    background_style: int = 1,
    background_alpha: float = 0.0,  # Default no background display
    
    # Bubble effect
    bubble_effect_id: Optional[str] = None,
    bubble_resource_id: Optional[str] = None,
    
    # Text effect
    effect_effect_id: Optional[str] = None,
    # Image adjustment parameters
    transform_x: float = 0.0,
    transform_y: float = -0.8,  # Default subtitle position at bottom
    scale_x: float = 1.0,
    scale_y: float = 1.0,
    rotation: float = 0.0,
    style_reference: draft.Text_segment = None,
    align: int = 1,
    vertical: bool = True,  # New parameter: whether to display vertically
    alpha: float = 0.4,
    width: int = 1080,  # New parameter
    height: int = 1920  # New parameter
):
    """
    Add subtitles to draft
    :param srt_path: Subtitle file path or URL or SRT text content
    :param draft_id: Draft ID, if None, create a new draft
    :param track_name: Track name, default is "subtitle"
    :param time_offset: Time offset, default is "0"s
    :param text_style: Text style, default is None
    :param clip_settings: Clip settings, default is None
    :param style_reference: Style reference, default is None
    :param align: Text alignment (default 1, center, 0 left, 2 right)
    :return: Draft information
    """
    # Get or create draft
    draft_id, script = get_or_create_draft(
        draft_id=draft_id,
        width=width,
        height=height
    )
    
    # Process subtitle content
    srt_content = None
    
    # Check if it's a URL
    if srt_path.startswith(('http://', 'https://')):
        try:
            response = requests.get(srt_path)
            response.raise_for_status()

            response.encoding = 'utf-8'
            srt_content = response.text
        except Exception as e:
            raise Exception(f"Failed to download subtitle file: {str(e)}")
    elif os.path.isfile(srt_path):  # Check if it's a file
        try:
            with open(srt_path, 'r', encoding='utf-8-sig') as f:
                srt_content = f.read()
        except Exception as e:
            raise Exception(f"Failed to read local subtitle file: {str(e)}")
    else:
        # If not a URL or local file, use content directly
        srt_content = srt_path
        # Handle possible escape characters
        srt_content = srt_content.replace('\\n', '\n').replace('/n', '\n')
    
    # Import subtitles
    # Convert hexadecimal color to RGB
    rgb_color = hex_to_rgb(font_color)

    # Create text_border
    text_border = None
    if border_width > 0:
        text_border = draft.Text_border(
            alpha=border_alpha,
            color=hex_to_rgb(border_color),
            width=border_width
        )
    
    # Create text_background
    text_background = None
    if background_alpha > 0:
        text_background = draft.Text_background(
            color=background_color,
            style=background_style,
            alpha=background_alpha
        )
    
    # Create text_style
    text_style = draft.Text_style(
        size=font_size,
        bold=bold,
        italic=italic,
        underline=underline,
        color=rgb_color,
        align=align,  # Keep center alignment
        vertical=vertical,  # Use the passed vertical parameter
        alpha=alpha  # Use the passed alpha parameter
    )
    
    # Create bubble effect
    text_bubble = None
    if bubble_effect_id and bubble_resource_id:
        text_bubble = TextBubble(
            effect_id=bubble_effect_id,
            resource_id=bubble_resource_id
        )
    
    # Create text effect
    text_effect = None
    if effect_effect_id:
        text_effect = TextEffect(
            effect_id=effect_effect_id,
            resource_id=effect_effect_id
        )
    
    # Create clip_settings
    clip_settings = draft.Clip_settings(
        transform_x=transform_x,
        transform_y=transform_y,
        scale_x=scale_x,
        scale_y=scale_y,
        rotation=rotation
    )

    script.import_srt(
        srt_content,
        track_name=track_name,
        time_offset=int(time_offset * 1000000),  # Convert seconds to microseconds
        text_style=text_style,
        font=font,
        clip_settings=clip_settings,
        style_reference=style_reference,
        border=text_border,
        background=text_background,
        bubble=text_bubble,
        effect=text_effect
    )

    # Persist updated script
    update_cache(draft_id, script)

    return {
        "draft_id": draft_id,
        # "draft_url": generate_draft_url(draft_id)
    }
