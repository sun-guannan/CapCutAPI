"""辅助函数，主要与模板模式有关"""

import inspect

from typing import Union, Type
from typing import List, Dict, Any

JsonExportable = Union[int, float, bool, str, List["JsonExportable"], Dict[str, "JsonExportable"]]

def provide_ctor_defaults(cls: Type) -> Dict[str, Any]:
    """为构造函数提供默认值，以绕开构造函数的参数限制"""

    signature = inspect.signature(cls.__init__)
    provided_defaults: Dict[str, Any] = {}

    for name, param in signature.parameters.items():
        if name == 'self': continue
        if param.default is not inspect.Parameter.empty: continue

        if param.annotation is int or param.annotation is float:
            provided_defaults[name] = 0
        elif param.annotation is str:
            provided_defaults[name] = ""
        elif param.annotation is bool:
            provided_defaults[name] = False
        else:
            raise ValueError(f"Unsupported parameter type: {param.annotation}")

    return provided_defaults

def assign_attr_with_json(obj: object, attrs: List[str], json_data: Dict[str, Any]):
    """根据json数据赋值给指定的对象属性

    若有复杂类型，则尝试调用其`import_json`方法进行构造
    """
    type_hints: Dict[str, Type] = {}
    for cls in obj.__class__.__mro__:
        if '__annotations__' in cls.__dict__:
            type_hints.update(cls.__annotations__)

    for attr in attrs:
        if hasattr(type_hints[attr], 'import_json'):
            obj.__setattr__(attr, type_hints[attr].import_json(json_data[attr]))
        else:
            obj.__setattr__(attr, type_hints[attr](json_data[attr]))

def export_attr_to_json(obj: object, attrs: List[str]) -> Dict[str, JsonExportable]:
    """将对象属性导出为json数据

    若有复杂类型，则尝试调用其`export_json`方法进行导出
    """
    json_data: Dict[str, Any] = {}
    for attr in attrs:
        if hasattr(getattr(obj, attr), 'export_json'):
            json_data[attr] = getattr(obj, attr).export_json()
        else:
            json_data[attr] = getattr(obj, attr)
    return json_data


def _is_emoji_codepoint(code_point: int) -> bool:
    """Rudimentary check whether a code point is commonly used as emoji.

    Covers major emoji blocks and symbols typically rendered as emoji.
    """
    # Supplemental Symbols and Pictographs
    if 0x1F900 <= code_point <= 0x1F9FF:
        return True
    # Symbols and Pictographs Extended-A
    if 0x1FA70 <= code_point <= 0x1FAFF:
        return True
    # Misc Symbols and Pictographs + Transport and Map
    if 0x1F300 <= code_point <= 0x1F6FF:
        return True
    # Emoticons
    if 0x1F600 <= code_point <= 0x1F64F:
        return True
    # Misc Symbols + Dingbats
    if 0x2600 <= code_point <= 0x27BF:
        return True
    # Regional Indicator Symbols (used for flags)
    if 0x1F1E6 <= code_point <= 0x1F1FF:
        return True
    # Skin tone modifiers
    if 0x1F3FB <= code_point <= 0x1F3FF:
        return True
    # Variation selectors are not emoji themselves
    return False


def len_emoji_as_two(text: str) -> int:
    """Compute display length counting emoji clusters as 2 and others as 1.

    Heuristics handled:
    - ZWJ sequences are treated as a single emoji cluster (length 2)
    - Flag sequences (two regional indicators) count as a single cluster (2)
    - Keycap sequences (e.g. 1\ufe0f\u20e3) count as 2
    - Variation selectors (FE0F/FE0E) are ignored in counting

    Note: This is a best-effort approximation without external deps.
    """
    if not text:
        return 0

    total_length = 0
    i = 0
    n = len(text)

    VARIATION_SELECTORS = {0xFE0F, 0xFE0E}
    ZWJ = 0x200D
    KEYCAP = 0x20E3

    while i < n:
        cp = ord(text[i])

        # Skip standalone variation selectors (should be handled in cluster)
        if cp in VARIATION_SELECTORS:
            i += 1
            continue

        # Begin cluster detection
        j = i
        is_emoji_cluster = False

        while True:
            current_cp = ord(text[j])
            if current_cp in VARIATION_SELECTORS:
                j += 1
                if j >= n:
                    break
                continue

            if _is_emoji_codepoint(current_cp):
                is_emoji_cluster = True

            # Handle keycap sequences: base [0-9#*] + (VS16)? + U+20E3
            if j + 1 < n and ord(text[j + 1]) == KEYCAP:
                is_emoji_cluster = True
                j += 2
                break

            j += 1
            if j >= n:
                break

            # Handle flag sequences: two regional indicators together
            if 0x1F1E6 <= current_cp <= 0x1F1FF and 0x1F1E6 <= ord(text[j]) <= 0x1F1FF:
                is_emoji_cluster = True
                j += 1
                break

            # Handle ZWJ-joined sequences as a single cluster
            if ord(text[j]) == ZWJ:
                j += 1
                if j >= n:
                    break
                continue
            else:
                break

        total_length += 2 if is_emoji_cluster else 1
        i = j

    return total_length