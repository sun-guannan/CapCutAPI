"""定义文本片段及其相关类"""

import json
import uuid
from copy import deepcopy

from typing import Dict, Tuple, Any, List
from typing import Union, Optional, Literal

from pyJianYingDraft.metadata.capcut_text_animation_meta import CapCutTextIntro, CapCutTextOutro, CapCutTextLoopAnim

from .time_util import Timerange, tim
from .segment import Clip_settings, Visual_segment
from .animation import Segment_animations, Text_animation

from .metadata import FontType, EffectMeta
from .metadata import TextIntro, TextOutro, TextLoopAnim

class Text_style:
    """字体样式类"""

    size: float
    """字体大小"""

    bold: bool
    """是否加粗"""
    italic: bool
    """是否斜体"""
    underline: bool
    """是否加下划线"""

    color: Tuple[float, float, float]
    """字体颜色, RGB三元组, 取值范围为[0, 1]"""
    alpha: float
    """字体不透明度"""

    align: Literal[0, 1, 2]
    """对齐方式"""
    vertical: bool
    """是否为竖排文本"""

    letter_spacing: int
    """字符间距"""
    line_spacing: int
    """行间距"""

    def __init__(self, *, size: float = 8.0, bold: bool = False, italic: bool = False, underline: bool = False,
                 color: Tuple[float, float, float] = (1.0, 1.0, 1.0), alpha: float = 1.0,
                 align: Literal[0, 1, 2] = 0, vertical: bool = False,
                 letter_spacing: int = 0, line_spacing: int = 0):
        """
        Args:
            size (`float`, optional): 字体大小, 默认为8.0
            bold (`bool`, optional): 是否加粗, 默认为否
            italic (`bool`, optional): 是否斜体, 默认为否
            underline (`bool`, optional): 是否加下划线, 默认为否
            color (`Tuple[float, float, float]`, optional): 字体颜色, RGB三元组, 取值范围为[0, 1], 默认为白色
            alpha (`float`, optional): 字体不透明度, 取值范围[0, 1], 默认不透明
            align (`int`, optional): 对齐方式, 0: 左对齐, 1: 居中, 2: 右对齐, 默认为左对齐
            vertical (`bool`, optional): 是否为竖排文本, 默认为否
            letter_spacing (`int`, optional): 字符间距, 定义与剪映中一致, 默认为0
            line_spacing (`int`, optional): 行间距, 定义与剪映中一致, 默认为0
        """
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline

        self.color = color
        self.alpha = alpha

        self.align = align
        self.vertical = vertical

        self.letter_spacing = letter_spacing
        self.line_spacing = line_spacing

class Text_border:
    """文本描边的参数"""

    alpha: float
    """描边不透明度"""
    color: Tuple[float, float, float]
    """描边颜色, RGB三元组, 取值范围为[0, 1]"""
    width: float
    """描边宽度"""

    def __init__(self, *, alpha: float = 1.0, color: Tuple[float, float, float] = (0.0, 0.0, 0.0), width: float = 40.0):
        """
        Args:
            alpha (`float`, optional): 描边不透明度, 取值范围[0, 1], 默认为1.0
            color (`Tuple[float, float, float]`, optional): 描边颜色, RGB三元组, 取值范围为[0, 1], 默认为黑色
            width (`float`, optional): 描边宽度, 与剪映中一致, 取值范围为[0, 100], 默认为40.0
        """
        self.alpha = alpha
        self.color = color
        self.width = width / 100.0 * 0.2  # 此映射可能不完全正确

    def export_json(self) -> Dict[str, Any]:
        """导出JSON数据, 放置在素材content的styles中"""
        return {
            "content": {
                "solid": {
                    "alpha": self.alpha,
                    "color": list(self.color),
                }
            },
            "width": self.width
        }

class Text_background:
    """文本背景参数"""

    style: Literal[0, 2]
    """背景样式"""

    alpha: float
    """背景不透明度"""
    color: str
    """背景颜色, 格式为'#RRGGBB'"""
    round_radius: float
    """背景圆角半径"""
    height: float
    """背景高度"""
    width: float
    """背景宽度"""
    horizontal_offset: float
    """背景水平偏移"""
    vertical_offset: float
    """背景竖直偏移"""

    def __init__(self, *, color: str, style: Literal[1, 2] = 1, alpha: float = 1.0, round_radius: float = 0.0,
                 height: float = 0.14, width: float = 0.14,
                 horizontal_offset: float = 0.5, vertical_offset: float = 0.5):
        """
        Args:
            color (`str`): 背景颜色, 格式为'#RRGGBB'
            style (`int`, optional): 背景样式, 1和2分别对应剪映中的两种样式, 默认为1
            alpha (`float`, optional): 背景不透明度, 与剪映中一致, 取值范围[0, 1], 默认为1.0
            round_radius (`float`, optional): 背景圆角半径, 与剪映中一致, 取值范围[0, 1], 默认为0.0
            height (`float`, optional): 背景高度, 与剪映中一致, 取值范围为[0, 1], 默认为0.14
            width (`float`, optional): 背景宽度, 与剪映中一致, 取值范围为[0, 1], 默认为0.14
            horizontal_offset (`float`, optional): 背景水平偏移, 与剪映中一致, 取值范围为[0, 1], 默认为0.5
            vertical_offset (`float`, optional): 背景竖直偏移, 与剪映中一致, 取值范围为[0, 1], 默认为0.5
        """
        self.style = (0, 2)[style - 1]

        self.alpha = alpha
        self.color = color
        self.round_radius = round_radius
        self.height = height
        self.width = width
        self.horizontal_offset = horizontal_offset * 2 - 1
        self.vertical_offset = vertical_offset * 2 - 1

    def export_json(self) -> Dict[str, Any]:
        """生成子JSON数据, 在Text_segment导出时合并到其中"""
        return {
            "background_style": self.style,
            "background_color": self.color,
            "background_alpha": self.alpha,
            "background_round_radius": self.round_radius,
            "background_height": self.height,
            "background_width": self.width,
            "background_horizontal_offset": self.horizontal_offset,
            "background_vertical_offset": self.vertical_offset,
        }

class Text_shadow:
    """文本阴影参数"""

    has_shadow: bool
    """是否启用阴影"""
    alpha: float
    """阴影不透明度"""
    angle: float
    """阴影角度"""
    color: str
    """阴影颜色，格式为'#RRGGBB'"""
    distance: float
    """阴影距离"""
    smoothing: float
    """阴影平滑度"""

    def __init__(self, *, has_shadow: bool = False, alpha: float = 0.9, angle: float = -45.0,
                 color: str = "#000000", distance: float = 5.0, smoothing: float = 0.45):
        """
        Args:
            has_shadow (`bool`, optional): 是否启用阴影，默认为False
            alpha (`float`, optional): 阴影不透明度，取值范围[0, 1]，默认为0.9
            angle (`float`, optional): 阴影角度，取值范围[-180, 180], 默认为-45.0
            color (`str`, optional): 阴影颜色，格式为'#RRGGBB'，默认为黑色
            distance (`float`, optional): 阴影距离，默认为5.0
            smoothing (`float`, optional): 阴影平滑度，取值范围[0, 1], 默认0.15
        """
        self.has_shadow = has_shadow
        self.alpha = alpha
        self.angle = angle
        self.color = color
        self.distance = distance
        self.smoothing = smoothing

    def export_json(self) -> Dict[str, Any]:
        """生成子JSON数据，在Text_segment导出时合并到其中"""
        return {
            "has_shadow": self.has_shadow,
            "shadow_alpha": self.alpha,
            "shadow_angle": self.angle,
            "shadow_color": self.color,
            "shadow_distance": self.distance,
            "shadow_smoothing": self.smoothing * 3
        }

class TextBubble:
    """文本气泡素材, 与滤镜素材本质上一致"""

    global_id: str
    """气泡全局id, 由程序自动生成"""

    effect_id: str
    resource_id: str

    def __init__(self, effect_id: str, resource_id: str):
        self.global_id = uuid.uuid4().hex
        self.effect_id = effect_id
        self.resource_id = resource_id

    def export_json(self) -> Dict[str, Any]:
        return {
            "apply_target_type": 0,
            "effect_id": self.effect_id,
            "id": self.global_id,
            "resource_id": self.resource_id,
            "type": "text_shape",
            "value": 1.0,
            # 不导出path和request_id
        }

class TextEffect(TextBubble):
    """文本花字素材, 与滤镜素材本质上也一致"""

    def export_json(self) -> Dict[str, Any]:
        ret = super().export_json()
        ret["type"] = "text_effect"
        ret["source_platform"] = 1
        return ret

class TextStyleRange:
    """文本样式范围类，用于定义文本特定范围的样式"""
    
    start: int
    """起始位置（包含）"""
    end: int
    """结束位置（不包含）"""
    style: Text_style
    """字体样式"""
    border: Optional[Text_border]
    """文本描边参数，None表示无描边"""
    font: Optional[EffectMeta]
    """字体设置，None表示使用全局字体"""
    
    def __init__(self, start: int, end: int, style: Text_style, border: Optional[Text_border] = None, font_str:str = None):
        """创建文本样式范围
        
        Args:
            start (`int`): 起始位置（包含）
            end (`int`): 结束位置（不包含）
            style (`Text_style`): 字体样式
            border (`Text_border`, optional): 文本描边参数，默认为None（无描边）
            font (optional): 字体设置，默认为None（使用全局字体）
        """
        self.start = start
        self.end = end
        self.style = style
        self.border = border
        if font_str:
            try:
                font_type = getattr(FontType, font_str).value
            except:
                available_fonts = [attr for attr in dir(FontType) if not attr.startswith('_')]
                raise ValueError(f"不支持的字体：{font_str}，请使用Font_type中的字体之一：{available_fonts}")
            self.font = font_type
    
    def get_range(self) -> List[int]:
        """获取范围列表
        
        Returns:
            `List[int]`: [start, end] 形式的范围列表
        """
        return [self.start, self.end]

class Text_segment(Visual_segment):
    """文本片段类, 目前仅支持设置基本的字体样式"""

    text: str
    """文本内容"""
    font: Optional[EffectMeta]
    """字体类型"""
    style: Text_style
    """字体样式"""

    border: Optional[Text_border]
    """文本描边参数, None表示无描边"""
    background: Optional[Text_background]
    """文本背景参数, None表示无背景"""

    shadow: Optional[Text_shadow]
    """文本阴影参数, None表示无阴影"""

    bubble: Optional[TextBubble]
    """文本气泡效果, 在放入轨道时加入素材列表中"""
    effect: Optional[TextEffect]
    """文本花字效果, 在放入轨道时加入素材列表中, 目前仅支持一部分花字效果"""
    
    fixed_width: float
    """固定宽度, -1表示不固定"""
    fixed_height: float
    """固定高度, -1表示不固定"""
    
    text_styles: List[TextStyleRange]
    """文本的多种样式列表"""

    def __init__(self, text: str, timerange: Timerange, *,
                 font: Optional[FontType] = None,
                 style: Optional[Text_style] = None, clip_settings: Optional[Clip_settings] = None,
                 border: Optional[Text_border] = None, background: Optional[Text_background] = None,
                 shadow: Optional[Text_shadow] = None,
                 fixed_width: int = -1, fixed_height: int = -1):
        """创建文本片段, 并指定其时间信息、字体样式及图像调节设置

        片段创建完成后, 可通过`Script_file.add_segment`方法将其添加到轨道中

        Args:
            text (`str`): 文本内容
            timerange (`Timerange`): 片段在轨道上的时间范围
            font (`Font_type`, optional): 字体类型, 默认为系统字体
            style (`Text_style`, optional): 字体样式, 包含大小/颜色/对齐/透明度等.
            clip_settings (`Clip_settings`, optional): 图像调节设置, 默认不做任何变换
            border (`Text_border`, optional): 文本描边参数, 默认无描边
            background (`Text_background`, optional): 文本背景参数, 默认无背景
            fixed_width (`int`, optional): 文本固定宽度（像素值）, 默认为-1（不固定宽度）
            fixed_height (`int`, optional): 文本固定高度（像素值）, 默认为-1（不固定高度）
        """
        super().__init__(uuid.uuid4().hex, None, timerange, 1.0, 1.0, clip_settings=clip_settings)

        self.text = text
        self.font = font.value if font else None
        self.style = style or Text_style()
        self.border = border
        self.background = background
        self.shadow = shadow
    
        self.bubble = None
        self.effect = None
        
        self.fixed_width = fixed_width
        self.fixed_height = fixed_height
        self.text_styles = []

    # 修改设置特定范围的文本样式的方法
    def add_text_style(self, textStyleRange: TextStyleRange) -> "Text_segment":
        # 添加新的样式范围
        self.text_styles.append(textStyleRange)
        return self
        

    @classmethod
    def create_from_template(cls, text: str, timerange: Timerange, template: "Text_segment") -> "Text_segment":
        """根据模板创建新的文本片段, 并指定其文本内容"""
        new_segment = cls(text, timerange, style=deepcopy(template.style), clip_settings=deepcopy(template.clip_settings),
                          border=deepcopy(template.border), background=deepcopy(template.background))
        new_segment.font = deepcopy(template.font)

        # 处理动画等
        if template.animations_instance:
            new_segment.animations_instance = deepcopy(template.animations_instance)
            new_segment.animations_instance.animation_id = uuid.uuid4().hex
            new_segment.extra_material_refs.append(new_segment.animations_instance.animation_id)
        if template.bubble:
            new_segment.add_bubble(template.bubble.effect_id, template.bubble.resource_id)
        if template.effect:
            new_segment.add_effect(template.effect.effect_id)

        return new_segment

    def add_animation(self, animation_type: Union[TextIntro, TextOutro, TextLoopAnim,
                                                  CapCutTextIntro, CapCutTextOutro, CapCutTextLoopAnim],
                      duration: Union[str, float] = 500000) -> "Text_segment":
        """将给定的入场/出场/循环动画添加到此片段的动画列表中, 出入场动画的持续时间可以自行设置, 循环动画则会自动填满其余无动画部分

        注意: 若希望同时使用循环动画和入出场动画, 请**先添加出入场动画再添加循环动画**

        Args:
            animation_type (`Text_intro`, `Text_outro` or `Text_loop_anim`): 文本动画类型.
            duration (`str` or `float`, optional): 动画持续时间, 单位为微秒, 仅对入场/出场动画有效.
                若传入字符串则会调用`tim()`函数进行解析. 默认为0.5秒
        """
        duration = min(tim(duration), self.target_timerange.duration)

        if (isinstance(animation_type, TextIntro) or isinstance(animation_type, CapCutTextIntro)):
            start = 0
        elif (isinstance(animation_type, TextOutro) or isinstance(animation_type, CapCutTextOutro)):
            start = self.target_timerange.duration - duration
        elif (isinstance(animation_type, TextLoopAnim) or isinstance(animation_type, CapCutTextLoopAnim)):
            intro_trange = self.animations_instance and self.animations_instance.get_animation_trange("in")
            outro_trange = self.animations_instance and self.animations_instance.get_animation_trange("out")
            start = intro_trange.start if intro_trange else 0
            duration = self.target_timerange.duration - start - (outro_trange.duration if outro_trange else 0)
        else:
            raise TypeError("Invalid animation type %s" % type(animation_type))

        if self.animations_instance is None:
            self.animations_instance = Segment_animations()
            self.extra_material_refs.append(self.animations_instance.animation_id)

        self.animations_instance.add_animation(Text_animation(animation_type, start, duration))

        return self

    def add_bubble(self, effect_id: str, resource_id: str) -> "Text_segment":
        """根据素材信息添加气泡效果, 相应素材信息可通过`Script_file.inspect_material`从模板中获取

        Args:
            effect_id (`str`): 气泡效果的effect_id
            resource_id (`str`): 气泡效果的resource_id
        """
        self.bubble = TextBubble(effect_id, resource_id)
        self.extra_material_refs.append(self.bubble.global_id)
        return self

    def add_effect(self, effect_id: str) -> "Text_segment":
        """根据素材信息添加花字效果, 相应素材信息可通过`Script_file.inspect_material`从模板中获取

        Args:
            effect_id (`str`): 花字效果的effect_id, 也同时是其resource_id
        """
        self.effect = TextEffect(effect_id, effect_id)
        self.extra_material_refs.append(self.effect.global_id)
        return self

    def export_material(self) -> Dict[str, Any]:
        """与此文本片段联系的素材, 以此不再单独定义Text_material类"""
        # 叠加各类效果的flag
        check_flag: int = 7
        if self.border:
            check_flag |= 8
        if self.background:
            check_flag |= 16
        if self.shadow and self.shadow.has_shadow:  # 如果有阴影且启用了阴影
            check_flag |= 32  # 添加阴影标志
    
        # 构建styles数组
        styles = []
        
        if self.text_styles:
            # 创建一个排序后的样式范围列表
            sorted_styles = sorted(self.text_styles, key=lambda x: x.start)
            
            # 检查是否需要在开头添加默认样式
            if sorted_styles[0].start > 0:
                # 添加从0到第一个样式开始的默认样式
                default_style = {
                    "fill": {
                        "alpha": 1.0,
                        "content": {
                            "render_type": "solid",
                            "solid": {
                                "alpha": self.style.alpha,
                                "color": list(self.style.color)
                            }
                        }
                    },
                    "range": [0, sorted_styles[0].start],
                    "size": self.style.size,
                    "bold": self.style.bold,
                    "italic": self.style.italic,
                    "underline": self.style.underline,
                    "strokes": [self.border.export_json()] if self.border else []
                }
                
                # 如果有阴影设置，添加到样式中
                if self.shadow and self.shadow.has_shadow:
                    default_style["shadows"] = [
                        {
                            "diffuse": self.shadow.smoothing / 6,  # diffuse = smoothing/6
                            "angle": self.shadow.angle,
                            "content": {
                                "solid": {
                                    "color": [int(self.shadow.color[1:3], 16)/255, 
                                             int(self.shadow.color[3:5], 16)/255, 
                                             int(self.shadow.color[5:7], 16)/255]
                                }
                            },
                            "distance": self.shadow.distance,
                            "alpha": self.shadow.alpha
                        }
                    ]
                
                # 如果有全局字体设置，添加到样式中
                if self.font:
                    default_style["font"] = {
                        "id": self.font.resource_id,
                        "path": "D:"
                    }
                
                # 如果有特效设置，添加到样式中
                if self.effect:
                    default_style["effectStyle"] = {
                        "id": self.effect.effect_id,
                        "path": "C:"  # 并不会真正在此处放置素材文件
                    }
                    
                styles.append(default_style)
            
            # 处理每个样式范围
            for i, style_range in enumerate(sorted_styles):
                # 添加当前样式范围的样式
                style_item = {
                    "fill": {
                        "alpha": 1.0,
                        "content": {
                            "render_type": "solid",
                            "solid": {
                                "alpha": style_range.style.alpha,
                                "color": list(style_range.style.color)
                            }
                        }
                    },
                    "range": style_range.get_range(),
                    "size": style_range.style.size,
                    "bold": style_range.style.bold,
                    "italic": style_range.style.italic,
                    "underline": style_range.style.underline,
                    "strokes": [style_range.border.export_json()] if style_range.border else []
                }
                
                # 如果TextStyleRange有字体设置，优先使用它
                if hasattr(style_range, 'font') and style_range.font:
                    style_item["font"] = {
                        "id": style_range.font.resource_id,
                        "path": "C:/%s.ttf" % style_range.font.name
                    }
                # 否则，如果有全局字体设置，使用全局字体
                elif self.font:
                    style_item["font"] = {
                        "id": self.font.resource_id,
                        "path": "C:/%s.ttf" % self.font.name
                    }
                
                # 如果有特效设置，添加到样式中
                if self.effect:
                    style_item["effectStyle"] = {
                        "id": self.effect.effect_id,
                        "path": "C:"  # 并不会真正在此处放置素材文件
                    }
                    
                styles.append(style_item)
                
                # 检查是否需要在当前样式和下一个样式之间添加默认样式
                if i < len(sorted_styles) - 1 and style_range.end < sorted_styles[i+1].start:
                    # 添加从当前样式结束到下一个样式开始的默认样式
                    gap_style = {
                        "fill": {
                            "alpha": 1.0,
                            "content": {
                                "render_type": "solid",
                                "solid": {
                                    "alpha": self.style.alpha,
                                    "color": list(self.style.color)
                                }
                            }
                        },
                        "range": [style_range.end, sorted_styles[i+1].start],
                        "size": self.style.size,
                        "bold": self.style.bold,
                        "italic": self.style.italic,
                        "underline": self.style.underline,
                        "strokes": [self.border.export_json()] if self.border else []
                    }
                    
                    # 如果有全局字体设置，添加到样式中
                    if self.font:
                        gap_style["font"] = {
                            "id": self.font.resource_id,
                            "path": "C:/%s.ttf" % self.font.name
                        }
                    
                    # 如果有特效设置，添加到样式中
                    if self.effect:
                        gap_style["effectStyle"] = {
                            "id": self.effect.effect_id,
                            "path": "C:"  # 并不会真正在此处放置素材文件
                        }
                        
                    styles.append(gap_style)
            
            # 检查是否需要在最后一个样式之后添加默认样式
            if sorted_styles[-1].end < len(self.text):
                # 添加从最后一个样式结束到文本结尾的默认样式
                end_style = {
                    "fill": {
                        "alpha": 1.0,
                        "content": {
                            "render_type": "solid",
                            "solid": {
                                "alpha": self.style.alpha,
                                "color": list(self.style.color)
                            }
                        }
                    },
                    "range": [sorted_styles[-1].end, len(self.text)],
                    "size": self.style.size,
                    "bold": self.style.bold,
                    "italic": self.style.italic,
                    "underline": self.style.underline,
                    "strokes": [self.border.export_json()] if self.border else []
                }
                
                # 如果有全局字体设置，添加到样式中
                if self.font:
                    end_style["font"] = {
                        "id": self.font.resource_id,
                        "path": "C:/%s.ttf" % self.font.name
                    }
                
                # 如果有特效设置，添加到样式中
                if self.effect:
                    end_style["effectStyle"] = {
                        "id": self.effect.effect_id,
                        "path": "C:"  # 并不会真正在此处放置素材文件
                    }
                    
                styles.append(end_style)
        else:
            # 如果text_styles为空，使用全局样式创建一个默认的style
            style_item = {
                "fill": {
                    "alpha": 1.0,
                    "content": {
                        "render_type": "solid",
                        "solid": {
                            "alpha": self.style.alpha,
                            "color": list(self.style.color)
                        }
                    }
                },
                "range": [0, len(self.text)],
                "size": self.style.size,
                "bold": self.style.bold,
                "italic": self.style.italic,
                "underline": self.style.underline,
                "strokes": [self.border.export_json()] if self.border else []
            }
            
            # 如果有阴影设置，添加到样式中
            if self.shadow and self.shadow.has_shadow:
                style_item["shadows"] = [
                    {
                        "diffuse": self.shadow.smoothing / 6,  # diffuse = smoothing/6
                        "angle": self.shadow.angle,
                        "content": {
                            "solid": {
                                "color": [int(self.shadow.color[1:3], 16)/255, 
                                            int(self.shadow.color[3:5], 16)/255, 
                                            int(self.shadow.color[5:7], 16)/255]
                            }
                        },
                        "distance": self.shadow.distance,
                        "alpha": self.shadow.alpha
                    }
                ]
                
            # 如果有全局字体设置，添加到样式中
            if self.font:
                style_item["font"] = {
                    "id": self.font.resource_id,
                    "path": "D:" # 并不会真正在此处放置字体文件
                }
            
            # 如果有特效设置，添加到样式中
            if self.effect:
                style_item["effectStyle"] = {
                    "id": self.effect.effect_id,
                    "path": "C:"  # 并不会真正在此处放置素材文件
                }
                
            styles.append(style_item)

        content_json = {
            "styles": styles,
            "text": self.text
        }

        ret = {
            "id": self.material_id,
            "content": json.dumps(content_json, ensure_ascii=False),

            "typesetting": int(self.style.vertical),
            "alignment": self.style.align,
            "letter_spacing": self.style.letter_spacing * 0.05,
            "line_spacing": 0.02 + self.style.line_spacing * 0.05,

            "line_feed": 1,
            "line_max_width": 0.82,
            "force_apply_line_max_width": False,

            "check_flag": check_flag,

            "type": "text",
            
            "fixed_width": self.fixed_width,
            "fixed_height": self.fixed_height,

            # 混合 (+4)
            # "global_alpha": 1.0,

            # 发光 (+64)，属性由extra_material_refs记录

            # 阴影 (+32)
            # "has_shadow": False,
            # "shadow_alpha": 0.9,
            # "shadow_angle": -45.0,
            # "shadow_color": "",
            # "shadow_distance": 5.0,
            # "shadow_point": {
            #     "x": 0.6363961030678928,
            #     "y": -0.6363961030678928
            # },
            # "shadow_smoothing": 0.45,

                        # 整体字体设置
            "font_category_id": "",
            "font_category_name": "",
            "font_id": "",
            "font_name": "",
            "font_path": "",
            "font_resource_id": "",
            "font_size": 15.0,
            "font_source_platform": 0,
            "font_team_id": "",
            "font_title": "none",
            "font_url": "",
            "fonts": [] if not self.text_styles else [
                # 根据text_styles生成fonts数组
                *[{
                    "category_id": "preset",
                    "category_name": "剪映预设",
                    "effect_id": style_range.font.resource_id if hasattr(style_range, 'font') and style_range.font else (self.font.resource_id if self.font else ""),
                    "file_uri": "",
                    "id": "BFBA9655-1FE5-41A0-A85D-577EFFF17BDD",
                    "path": "C:/%s.ttf" % (style_range.font.name if hasattr(style_range, 'font') and style_range.font else (self.font.name if self.font else "")),
                    "request_id": "20250713102314DA3D8F267527925ADC9A",
                    "resource_id": style_range.font.resource_id if hasattr(style_range, 'font') and style_range.font else (self.font.resource_id if self.font else ""),
                    "source_platform": 0,
                    "team_id": "",
                    "title": style_range.font.name if hasattr(style_range, 'font') and style_range.font else (self.font.name if self.font else "")
                } for style_range in self.text_styles if (hasattr(style_range, 'font') and style_range.font) or self.font]
            ],

            # 似乎会被content覆盖
            # "text_alpha": 1.0,
            # "text_color": "#FFFFFF",
            # "text_curve": None,
            # "text_preset_resource_id": "",
            # "text_size": 30,
            # "underline": False,
        }

        if self.background:
            ret.update(self.background.export_json())
        
        # 添加阴影参数
        if self.shadow and self.shadow.has_shadow:
            shadow_json = self.shadow.export_json()
            ret.update(shadow_json)  # 将阴影参数合并到返回的字典中
        
        return ret
