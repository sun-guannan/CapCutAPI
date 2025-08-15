"""与模板模式相关的类及函数等"""

from enum import Enum
from copy import deepcopy

from . import util
from . import exceptions
from .time_util import Timerange
from .segment import Base_segment
from .track import Base_track, Track_type, Track
from .local_materials import Video_material, Audio_material
from .video_segment import Video_segment, Clip_settings
from .audio_segment import Audio_segment
from .keyframe import Keyframe_list, Keyframe_property, Keyframe
from .metadata import AudioSceneEffectType

from typing import List, Dict, Any

class Shrink_mode(Enum):
    """处理替换素材时素材变短情况的方法"""

    cut_head = "cut_head"
    """裁剪头部, 即后移片段起始点"""
    cut_tail = "cut_tail"
    """裁剪尾部, 即前移片段终止点"""

    cut_tail_align = "cut_tail_align"
    """裁剪尾部并消除间隙, 即前移片段终止点, 后续片段也依次前移"""

    shrink = "shrink"
    """保持中间点不变, 两端点向中间靠拢"""

class Extend_mode(Enum):
    """处理替换素材时素材变长情况的方法"""

    cut_material_tail = "cut_material_tail"
    """裁剪素材尾部(覆盖`source_timerange`参数), 使得片段维持原长不变, 此方法总是成功"""

    extend_head = "extend_head"
    """延伸头部, 即尝试前移片段起始点, 与前续片段重合时失败"""
    extend_tail = "extend_tail"
    """延伸尾部, 即尝试后移片段终止点, 与后续片段重合时失败"""

    push_tail = "push_tail"
    """延伸尾部, 若有必要则依次后移后续片段, 此方法总是成功"""

class ImportedSegment(Base_segment):
    """导入的片段"""

    raw_data: Dict[str, Any]
    """原始json数据"""

    __DATA_ATTRS = ["material_id", "target_timerange"]
    def __init__(self, json_data: Dict[str, Any]):
        self.raw_data = deepcopy(json_data)

        util.assign_attr_with_json(self, self.__DATA_ATTRS, json_data)

    def export_json(self) -> Dict[str, Any]:
        json_data = deepcopy(self.raw_data)
        json_data.update(util.export_attr_to_json(self, self.__DATA_ATTRS))
        return json_data

class ImportedMediaSegment(ImportedSegment):
    """导入的视频/音频片段"""

    source_timerange: Timerange
    """片段取用的素材时间范围"""

    __DATA_ATTRS = ["source_timerange"]
    def __init__(self, json_data: Dict[str, Any]):
        super().__init__(json_data)

        util.assign_attr_with_json(self, self.__DATA_ATTRS, json_data)

    def export_json(self) -> Dict[str, Any]:
        json_data = super().export_json()
        json_data.update(util.export_attr_to_json(self, self.__DATA_ATTRS))
        return json_data


class ImportedTrack(Base_track):
    """模板模式下导入的轨道"""

    raw_data: Dict[str, Any]
    """原始轨道数据"""

    def __init__(self, json_data: Dict[str, Any]):
        self.track_type = Track_type.from_name(json_data["type"])
        self.name = json_data["name"]
        self.track_id = json_data["id"]
        self.render_index = max([int(seg["render_index"]) for seg in json_data["segments"]], default=0)

        self.raw_data = deepcopy(json_data)

    def export_json(self) -> Dict[str, Any]:
        ret = deepcopy(self.raw_data)
        ret.update({
            "name": self.name,
            "id": self.track_id
        })
        return ret

class EditableTrack(ImportedTrack):
    """模板模式下导入且可修改的轨道(音视频及文本轨道)"""

    segments: List[ImportedSegment]
    """该轨道包含的片段列表"""

    def __len__(self):
        return len(self.segments)

    @property
    def start_time(self) -> int:
        """轨道起始时间, 微秒"""
        if len(self.segments) == 0:
            return 0
        return self.segments[0].target_timerange.start

    @property
    def end_time(self) -> int:
        """轨道结束时间, 微秒"""
        if len(self.segments) == 0:
            return 0
        return self.segments[-1].target_timerange.end

    def export_json(self) -> Dict[str, Any]:
        ret = super().export_json()
        # 为每个片段写入render_index
        segment_exports = [seg.export_json() for seg in self.segments]
        for seg in segment_exports:
            seg["render_index"] = self.render_index
        ret["segments"] = segment_exports
        return ret

class ImportedTextTrack(EditableTrack):
    """模板模式下导入的文本轨道"""

    def __init__(self, json_data: Dict[str, Any]):
        super().__init__(json_data)
        self.segments = [ImportedSegment(seg) for seg in json_data["segments"]]

class ImportedMediaTrack(EditableTrack):
    """模板模式下导入的音频/视频轨道"""

    segments: List[ImportedMediaSegment]
    """该轨道包含的片段列表"""

    def __init__(self, json_data: Dict[str, Any]):
        super().__init__(json_data)
        self.segments = [ImportedMediaSegment(seg) for seg in json_data["segments"]]

    def check_material_type(self, material: object) -> bool:
        """检查素材类型是否与轨道类型匹配"""
        if self.track_type == Track_type.video and isinstance(material, Video_material):
            return True
        if self.track_type == Track_type.audio and isinstance(material, Audio_material):
            return True
        return False

    def process_timerange(self, seg_index: int, src_timerange: Timerange,
                          shrink: Shrink_mode, extend: List[Extend_mode]) -> None:
        """处理素材替换的时间范围变更"""
        seg = self.segments[seg_index]
        new_duration = src_timerange.duration

        # 时长变短
        delta_duration = abs(new_duration - seg.duration)
        if new_duration < seg.duration:
            if shrink == Shrink_mode.cut_head:
                seg.start += delta_duration
            elif shrink == Shrink_mode.cut_tail:
                seg.duration -= delta_duration
            elif shrink == Shrink_mode.cut_tail_align:
                seg.duration -= delta_duration
                for i in range(seg_index+1, len(self.segments)):  # 后续片段也依次前移相应值（保持间隙）
                    self.segments[i].start -= delta_duration
            elif shrink == Shrink_mode.shrink:
                seg.duration -= delta_duration
                seg.start += delta_duration // 2
            else:
                raise ValueError(f"Unsupported shrink mode: {shrink}")
        # 时长变长
        elif new_duration > seg.duration:
            success_flag = False
            prev_seg_end = int(0) if seg_index == 0 else self.segments[seg_index-1].target_timerange.end
            next_seg_start = int(1e15) if seg_index == len(self.segments)-1 else self.segments[seg_index+1].start
            for mode in extend:
                if mode == Extend_mode.extend_head:
                    if seg.start - delta_duration >= prev_seg_end:
                        seg.start -= delta_duration
                        success_flag = True
                elif mode == Extend_mode.extend_tail:
                    if seg.target_timerange.end + delta_duration <= next_seg_start:
                        seg.duration += delta_duration
                        success_flag = True
                elif mode == Extend_mode.push_tail:
                    shift_duration = max(0, seg.target_timerange.end + delta_duration - next_seg_start)
                    seg.duration += delta_duration
                    if shift_duration > 0:  # 有必要时后移后续片段
                        for i in range(seg_index+1, len(self.segments)):
                            self.segments[i].start += shift_duration
                    success_flag = True
                elif mode == Extend_mode.cut_material_tail:
                    src_timerange.duration = seg.duration
                    success_flag = True
                else:
                    raise ValueError(f"Unsupported extend mode: {mode}")

                if success_flag:
                    break
            if not success_flag:
                raise exceptions.ExtensionFailed(f"未能将片段延长至 {new_duration}μs, 尝试过以下方法: {extend}")

        # 写入素材时间范围
        seg.source_timerange = src_timerange

def import_track(json_data: Dict[str, Any], imported_materials: Dict[str, Any] = None) -> Track:
    """导入轨道
    :param json_data: 轨道数据
    :param imported_materials: 已导入的素材数据，用于创建片段的material实例
    """
    track_type = Track_type.from_name(json_data["type"])
    # 创建新的Track实例，保留所有原始属性
    track = Track(
        track_type=track_type,
        name=json_data["name"],
        render_index=max([int(seg.get("render_index", 0)) for seg in json_data.get("segments", [])], default=0),
        mute=bool(json_data.get("attribute", 0))
    )
    
    # 设置track_id，使用原始ID
    track.track_id = json_data.get("id")
    
    # 如果轨道类型允许修改，导入所有片段
    if track_type.value.allow_modify and imported_materials:
        for segment_data in json_data.get("segments", []):
            material_id = segment_data.get("material_id")
            material = None
            
            # 处理关键帧信息
            common_keyframes = []
            for kf_list_data in segment_data.get("common_keyframes", []):
                # 创建关键帧列表
                kf_list = Keyframe_list(Keyframe_property(kf_list_data["property_type"]))
                kf_list.list_id = kf_list_data["id"]
                
                # 添加关键帧
                for kf_data in kf_list_data["keyframe_list"]:
                    keyframe = Keyframe(kf_data["time_offset"], kf_data["values"][0])
                    keyframe.kf_id = kf_data["id"]
                    keyframe.values = kf_data["values"]
                    kf_list.keyframes.append(keyframe)
                
                common_keyframes.append(kf_list)
            
            # 根据轨道类型查找对应的素材
            if track_type == Track_type.video:
                # 从imported_materials中查找视频素材
                for video_material in imported_materials.get("videos", []):
                    if video_material["id"] == material_id:
                        material = Video_material.from_dict(video_material)
                        break
                
                if material:
                    # 创建视频片段
                    segment = Video_segment(
                        material=material,
                        target_timerange=Timerange(
                            start=segment_data["target_timerange"]["start"],
                            duration=segment_data["target_timerange"]["duration"]
                        ),
                        source_timerange=Timerange(
                            start=segment_data["source_timerange"]["start"],
                            duration=segment_data["source_timerange"]["duration"]
                        ),
                        speed=segment_data.get("speed", 1.0),
                        clip_settings=Clip_settings(
                            transform_x=segment_data["clip"]["transform"]["x"],
                            transform_y=segment_data["clip"]["transform"]["y"],
                            scale_x=segment_data["clip"]["scale"]["x"],
                            scale_y=segment_data["clip"]["scale"]["y"]
                        )
                    )
                    segment.volume = segment_data.get("volume", 1.0)
                    segment.visible = segment_data.get("visible", True)
                    segment.common_keyframes = common_keyframes
                    track.segments.append(segment)
                
            elif track_type == Track_type.audio:
                # 从imported_materials中查找音频素材
                for audio_material in imported_materials.get("audios", []):
                    if audio_material["id"] == material_id:
                        material = Audio_material.from_dict(audio_material)
                        break
                
                if material:
                    # 创建音频片段
                    segment = Audio_segment(
                        material=material,
                        target_timerange=Timerange(
                            start=segment_data["target_timerange"]["start"],
                            duration=segment_data["target_timerange"]["duration"]
                        ),
                        volume=segment_data.get("volume", 1.0)
                    )
                    # 添加音频效果
                    if "audio_effects" in imported_materials and imported_materials["audio_effects"]:
                        effect_data = imported_materials["audio_effects"][0]
                        # 根据资源ID查找对应的效果类型
                        for effect_type in AudioSceneEffectType:
                            if effect_type.value.resource_id == effect_data["resource_id"]:
                                # 将参数值从0-1映射到0-100
                                params = []
                                for param in effect_data["audio_adjust_params"]:
                                    params.append(param["value"] * 100)
                                segment.add_effect(effect_type, params,effect_id=effect_data["id"])
                                break
                    segment.common_keyframes = common_keyframes
                    track.segments.append(segment)
            else:
                # 其他类型片段保持原样
                segment = ImportedSegment(segment_data)
                segment.common_keyframes = common_keyframes
                track.segments.append(segment)
    
    return track
