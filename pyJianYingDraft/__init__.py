import sys

from .local_materials import Crop_settings, Video_material, Audio_material
from .keyframe import Keyframe_property

from .time_util import Timerange
from .audio_segment import Audio_segment
from .video_segment import Video_segment, Sticker_segment, Clip_settings
from .effect_segment import Effect_segment, Filter_segment
from .text_segment import Text_segment, Text_style, Text_border, Text_background, Text_shadow

from .metadata import FontType
from .metadata import MaskType
from .metadata import CapCutMaskType
from .metadata import TransitionType, FilterType
from .metadata import CapCutTransitionType
from .metadata import IntroType, OutroType, GroupAnimationType
from .metadata import CapCutIntroType, CapCutOutroType, CapCutGroupAnimationType
from .metadata import TextIntro, TextOutro, TextLoopAnim
from .metadata import CapCutTextIntro, CapCutTextOutro, CapCutTextLoopAnim
from .metadata import AudioSceneEffectType, ToneEffectType, SpeechToSongType
from .metadata import CapCutVoiceFiltersEffectType, CapCutVoiceCharactersEffectType, CapCutSpeechToSongEffectType
from .metadata import VideoSceneEffectType, VideoCharacterEffectType
from .metadata import CapCutVideoSceneEffectType, CapCutVideoCharacterEffectType

from .track import Track_type
from .template_mode import Shrink_mode, Extend_mode
from .script_file import Script_file
from .draft_folder import Draft_folder

# 仅在Windows系统下导入jianying_controller
# ISWIN = (sys.platform == 'win32')
# if ISWIN:
#     from .jianying_controller import Jianying_controller, Export_resolution, Export_framerate

from .time_util import SEC, tim, trange

__all__ = [
    "FontType",
    "MaskType",
    "CapCutMaskType",
    "FilterType",
    "TransitionType",
    "CapCutTransitionType",
    "IntroType",
    "OutroType",
    "GroupAnimationType",
    "CapCutIntroType",
    "CapCutOutroType",
    "CapCutGroupAnimationType",
    "TextIntro",
    "TextOutro",
    "TextLoopAnim",
    "CapCutTextIntro",
    "CapCutTextOutro",
    "CapCutTextLoopAnim",
    "AudioSceneEffectType",
    "ToneEffectType",
    "SpeechToSongType",
    "VideoSceneEffectType",
    "VideoCharacterEffectType",
    "CapCutVoiceFiltersEffectType",
    "CapCutVoiceCharactersEffectType",
    "CapCutSpeechToSongEffectType",
    "CapCutVideoSceneEffectType",
    "CapCutVideoCharacterEffectType",
    "Crop_settings",
    "Video_material",
    "Audio_material",
    "Keyframe_property",
    "Timerange",
    "Audio_segment",
    "Video_segment",
    "Sticker_segment",
    "Clip_settings",
    "Effect_segment",
    "Filter_segment",
    "Text_segment",
    "Text_style",
    "Text_border",
    "Text_background",
    "Text_shadow",
    "Track_type",
    "Shrink_mode",
    "Extend_mode",
    "Script_file",
    "Draft_folder",
    "SEC",
    "tim",
    "trange"
]

# # 仅在Windows系统下添加jianying_controller相关的导出
# if ISWIN:
#     __all__.extend([
#         "JianyingController",
#         "ExportResolution",
#         "ExportFramerate",
#         "Jianying_controller",
#         "Export_resolution",
#         "Export_framerate",
#     ])