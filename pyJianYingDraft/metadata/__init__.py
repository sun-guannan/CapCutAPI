"""记录各种特效/音效/滤镜等的元数据"""

from .effect_meta import EffectMeta, EffectParamInstance, AnimationMeta

from .capcut_mask_meta import CapCutMaskType
from .capcut_transition_meta import CapCutTransitionType
from .capcut_animation_meta import CapCutIntroType, CapCutOutroType, CapCutGroupAnimationType
from .capcut_text_animation_meta import CapCutTextIntro, CapCutTextOutro, CapCutTextLoopAnim
from .capcut_audio_effect_meta import CapCutVoiceFiltersEffectType, CapCutVoiceCharactersEffectType, CapCutSpeechToSongEffectType
from .capcut_effect_meta import CapCutVideoSceneEffectType, CapCutVideoCharacterEffectType

# 视频特效
from .video_scene_effect import VideoSceneEffectType
from .video_character_effect import VideoCharacterEffectType

# 视频动画
from .video_intro import IntroType
from .video_outro import OutroType
from .video_group_animation import GroupAnimationType

# 音频特效
from .audio_scene_effect import AudioSceneEffectType
from .tone_effect import ToneEffectType
from .speech_to_song import SpeechToSongType

# 文本动画
from .text_intro import TextIntro
from .text_outro import TextOutro
from .text_loop import TextLoopAnim

# 其它
from .font_meta import FontType
from .mask_meta import MaskType, MaskMeta
from .filter_meta import FilterType
from .transition_meta import TransitionType

__all__ = [
    AnimationMeta,
    "EffectMeta",
    "EffectParamInstance",
    "MaskType",
    "MaskMeta",
    "CapCutMaskType",
    "FilterType",
    "FontType",
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
    "CapCutVoiceFiltersEffectType",
    "CapCutVoiceCharactersEffectType",
    "CapCutSpeechToSongEffectType",
    "VideoSceneEffectType",
    "VideoCharacterEffectType",
    "CapCutVideoSceneEffectType",
    "CapCutVideoCharacterEffectType"
]
