import pyJianYingDraft as draft
from settings.local import IS_CAPCUT_ENV
from util import generate_draft_url, hex_to_rgb
from pyJianYingDraft import trange, FontType
from typing import Optional, List  # add List type hint
from pyJianYingDraft import exceptions
from create_draft import get_or_create_draft
from pyJianYingDraft.text_segment import TextBubble, TextEffect, TextStyleRange

def add_text_impl(
    text: str,
    start: float,
    end: float,
    draft_id: str | None = None,  # Python 3.10+ 新语法
    transform_y: float = -0.8,
    transform_x: float = 0,
    font: Optional[str] = None,
    font_color: str = "#ffffff",
    font_size: float = 8.0,
    track_name: str = "text_main",
    align: int = 1,
    vertical: bool = False,
    font_alpha: float = 1.0,
    # Border parameters
    border_alpha: float = 1.0,
    border_color: str = "#000000",
    border_width: float = 0.0,
    # Background parameters
    background_color: str = "#000000",
    background_style: int = 1,
    background_alpha: float = 0.0,
    background_round_radius: float = 0.0,
    background_height: float = 0.14,
    background_width: float = 0.14,
    background_horizontal_offset: float = 0.5,
    background_vertical_offset: float = 0.5,
    # Shadow parameters
    shadow_enabled: bool = False,
    shadow_alpha: float = 0.9,
    shadow_angle: float = -45.0,
    shadow_color: str = "#000000",
    shadow_distance: float = 5.0,
    shadow_smoothing: float = 0.15,
    # Bubble effect
    bubble_effect_id: str | None = None,
    bubble_resource_id: str | None = None,
    # Text effect
    effect_effect_id: str | None = None,
    intro_animation: str | None = None,
    intro_duration: float = 0.5,
    outro_animation: str | None = None,
    outro_duration: float = 0.5,
    width: int = 1080,
    height: int = 1920,
    fixed_width: float = -1,  # Text fixed width ratio, default -1 means not fixed
    fixed_height: float = -1,  # Text fixed height ratio, default -1 means not fixed
    # 多样式文本参数
    text_styles: Optional[List[TextStyleRange]] = None,  # 文本的不同部分的样式列表
    # 默认全局样式
    bold: bool | None = None,
    italic: bool | None = None,
    underline: bool | None = None,
):
    """
    Add text subtitle to the specified draft (configurable parameter version)
    :param text: Text content
    :param start: Start time (seconds)
    :param end: End time (seconds)
    :param draft_id: Draft ID (optional, default None creates a new draft)
    :param transform_y: Y-axis position (default -0.8, bottom of screen)
    :param transform_x: X-axis position (default 0, center of screen)
    :param font: Font name (supports all fonts in Font_type)
    :param font_color: Font color #FFF0FF
    :param font_size: Font size (float value, default 8.0)
    :param track_name: Track name
    :param align: Text alignment (default 1, center, 0 left, 2 right)
    :param vertical: Whether to display vertically (default False)
    :param font_alpha: Text transparency, range 0.0-1.0 (default 1.0, completely opaque)
    :param border_alpha: Border transparency, range 0.0-1.0 (default 1.0)
    :param border_color: Border color (default black)
    :param border_width: Border width (default 0.0, no border display)
    :param background_color: Background color (default black)
    :param background_style: Background style (default 1)
    :param background_alpha: Background transparency (default 0.0, no background display)
    :param background_round_radius: 背景圆角半径，范围0.0-1.0（默认0.0）
    :param background_height: 背景高度，范围0.0-1.0（默认0.14）
    :param background_width: 背景宽度，范围0.0-1.0（默认0.14）
    :param background_horizontal_offset: 背景水平偏移，范围0.0-1.0（默认0.5）
    :param background_vertical_offset: 背景垂直偏移，范围0.0-1.0（默认0.5）
    :param shadow_enabled: 是否启用阴影（默认False）
    :param shadow_alpha: 阴影透明度，范围0.0-1.0（默认0.9）
    :param shadow_angle: 阴影角度，范围-180.0-180.0（默认-45.0）
    :param shadow_color: 阴影颜色（默认黑色）
    :param shadow_distance: 阴影距离（默认5.0）
    :param shadow_smoothing: 阴影平滑度，范围0.0-1.0（默认0.15）
    :param bubble_effect_id: Bubble effect ID
    :param bubble_resource_id: Bubble resource ID
    :param effect_effect_id: Text effect ID
    :param intro_animation: Intro animation type
    :param intro_duration: Intro animation duration (seconds), default 0.5 seconds
    :param outro_animation: Outro animation type
    :param outro_duration: Outro animation duration (seconds), default 0.5 seconds
    :param width: Video width (pixels)
    :param height: Video height (pixels)
    :param bold: Whether to use bold font
    :param italic: Whether to use italic font
    :param underline: Whether to use underline font
    :param fixed_width: Text fixed width ratio, range 0.0-1.0, default -1 means not fixed
    :param fixed_height: Text fixed height ratio, range 0.0-1.0, default -1 means not fixed
    :param text_styles: 文本的不同部分的样式列表，每个元素是一个TextStyleRange
    :return: Updated draft information
    """
    # Validate if font is in Font_type
    if font is None:
        font_type = None
    else:
        try:
            font_type = getattr(FontType, font)
        except:
            available_fonts = [attr for attr in dir(FontType) if not attr.startswith('_')]
            raise ValueError(f"Unsupported font: {font}, please use one of the fonts in Font_type: {available_fonts}")
    
    # Validate alpha value range
    if not 0.0 <= font_alpha <= 1.0:
        raise ValueError("alpha value must be between 0.0 and 1.0")
    if not 0.0 <= border_alpha <= 1.0:
        raise ValueError("border_alpha value must be between 0.0 and 1.0")
    if not 0.0 <= background_alpha <= 1.0:
        raise ValueError("background_alpha value must be between 0.0 and 1.0")
    
    # Get or create draft
    draft_id, script = get_or_create_draft(
        draft_id=draft_id,
        width=width,
        height=height
    )

    # Add text track
    if track_name is not None:
        try:
            imported_track = script.get_imported_track(draft.Track_type.text, name=track_name)
            # If no exception is thrown, the track already exists
        except exceptions.TrackNotFound:
            # Track doesn't exist, create a new track
            script.add_track(draft.Track_type.text, track_name=track_name)
    else:
        script.add_track(draft.Track_type.audio)

    # Convert hexadecimal color to RGB tuple
    try:
        rgb_color = hex_to_rgb(font_color)
        rgb_border_color = hex_to_rgb(border_color)
    except ValueError as e:
        raise ValueError(f"Color parameter error: {str(e)}")
    
    # Create text_border
    text_border = None
    if border_width > 0:
        text_border = draft.Text_border(
            alpha=border_alpha,
            color=rgb_border_color,
            width=border_width
        )
    
    # Create text_background
    text_background = None
    if background_alpha > 0:
        text_background = draft.Text_background(
            color=background_color,
            style=background_style,
            alpha=background_alpha,
            round_radius=background_round_radius,
            height=background_height,
            width=background_width,
            horizontal_offset=background_horizontal_offset,
            vertical_offset=background_vertical_offset
        )
    
    # 创建text_shadow (阴影)
    text_shadow = None
    if shadow_enabled:
        text_shadow = draft.Text_shadow(
            has_shadow=shadow_enabled,
            alpha=shadow_alpha,
            angle=shadow_angle,
            color=shadow_color,
            distance=shadow_distance,
            smoothing=shadow_smoothing
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
            effect_id=effect_effect_id
        )
    
    # Convert ratio to pixel value
    pixel_fixed_width = -1
    pixel_fixed_height = -1
    if fixed_width > 0:
        pixel_fixed_width = int(fixed_width * script.width)
    if fixed_height > 0:
        pixel_fixed_height = int(fixed_height * script.height)
    
    # Create text segment (using configurable parameters)
    text_segment = draft.Text_segment(
        text,
        trange(f"{start}s", f"{end-start}s"),
        font=font_type,  # Use font from Font_type
        style=draft.Text_style(
            color=rgb_color,
            size=font_size,
            bold=bold,
            italic=italic,
            underline=underline,
            align=align,
            vertical=vertical,  # Set whether to display vertically
            alpha=font_alpha  # Set transparency
        ),
        clip_settings=draft.Clip_settings(transform_y=transform_y, transform_x=transform_x),
        border=text_border,
        background=text_background,
        shadow=text_shadow,
        fixed_width=pixel_fixed_width,
        fixed_height=pixel_fixed_height
    )

    # 应用多样式文本设置
    if text_styles:
        for style_range in text_styles:
            # 验证范围有效性
            if style_range.start < 0 or style_range.end > len(text) or style_range.start >= style_range.end:
                raise ValueError(f"无效的文本范围: [{style_range.start}, {style_range.end}), 文本长度: {len(text)}")
            
            # 应用样式到特定文本范围
            text_segment.add_text_style(style_range)

    if text_bubble:
        text_segment.add_bubble(text_bubble.effect_id, text_bubble.resource_id)
    if text_effect:
        text_segment.add_effect(text_effect.effect_id)

    # Add intro animation
    if intro_animation:
        try:
            if IS_CAPCUT_ENV:
                animation_type = getattr(draft.CapCutTextIntro, intro_animation)
            else:
                animation_type = getattr(draft.TextIntro, intro_animation)
            # Convert seconds to microseconds
            duration_microseconds = int(intro_duration * 1000000)
            text_segment.add_animation(animation_type, duration_microseconds)  # Add intro animation, set duration
        except:
            print(f"Warning: Unsupported intro animation type {intro_animation}, this parameter will be ignored")

    # Add outro animation
    if outro_animation:
        try:
            if IS_CAPCUT_ENV:
                animation_type = getattr(draft.CapCutTextOutro, outro_animation)
            else:
                animation_type = getattr(draft.TextOutro, outro_animation)
            # Convert seconds to microseconds
            duration_microseconds = int(outro_duration * 1000000)
            text_segment.add_animation(animation_type, duration_microseconds)  # Add outro animation, set duration
        except:
            print(f"Warning: Unsupported outro animation type {outro_animation}, this parameter will be ignored")

    # Add text segment to track
    script.add_segment(text_segment, track_name=track_name)

    return {
        "draft_id": draft_id,
        "draft_url": generate_draft_url(draft_id)
    }
