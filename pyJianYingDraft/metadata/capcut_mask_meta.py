from .effect_meta import EffectEnum
from .mask_meta import MaskMeta

class CapCutMaskType(EffectEnum):
    """CapCut自带的蒙版类型"""

    Split        = MaskMeta("Split", "line", "7374020197990011409", "B52CD1BC-63CE-4B74-B180-0B61E4AC928A", "4c6a0ef5de6a844342d40330e00c59eb", 1.0)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.0, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Filmstrip    = MaskMeta("Filmstrip", "mirror", "7374021024985125377", "C4A9A4BD-280D-4625-AA7D-F5F70E97B438", "95ac211c99063c41b86b9b63742f4a6d", 1.0)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.5, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Circle       = MaskMeta("Circle", "circle", "7374021188315517456", "E827751C-8DA7-412C-800D-DF2FE8712F77", "3ab1c47350d987c8ad415497e020a38b", 1.0)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.5, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Rectangle    = MaskMeta("Rectangle", "rectangle", "7374021450748924432", "E55A3414-9C81-4664-BB2B-42528D098F2F", "02b8999168d121538a98ea59127483ef", 1.0)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.5, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Stars        = MaskMeta("Stars", "pentagram", "7374021798087627265", "D824ED5D-D0C1-4EE2-B098-65F99CB38B95", "d3eb0298b2b1c345c123470c9194c8ad", 1.0471014493)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.5, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Heart        = MaskMeta("Heart", "heart", "7350964630979613186", "2CA4F90A-87A6-483E-B71B-FDA65EE46860", "cfa1154e4873fda2c09716c8aa546236", 1.1148148148)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.5, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Text         = MaskMeta("Text", "text", "7439320146876830225", "61E0D039-1A51-4570-B3F1-6AAC82AC1520", "ada210b1e21e860006c8324db359d8a3", 1.0)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.5, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Brush        = MaskMeta("Brush", "custom", "7374021798087627265", "31AC68F1-9EC3-4A4E-8D53-D556B7CDAC9E", "7e3c26bd14a0b68a84fee058db7f1ade", 1.0)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 0.5, invert: False, rotation: 0.0, roundCorner: 0.0, width: 0.16"""
    Pen          = MaskMeta("Pen", "contour", "7414333113955783185", "E3F45CAF-D445-4975-BE57-67AA716425D3", "9ee4e93af66335a75843446555efd8a6", 1.0)
    """配置: centerX: 0.0, centerY: 0.0, expansion: 0.0, feather: 0.0, height: 1.0, invert: False, rotation: 0.0, roundCorner: 0.0, width: 1.0"""
