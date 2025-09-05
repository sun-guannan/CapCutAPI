import os
import uuid
import subprocess
import json
from typing import Optional, Literal
from typing import Dict, Any

class Crop_settings:
    """素材的裁剪设置, 各属性均在0-1之间, 注意素材的坐标原点在左上角"""

    upper_left_x: float
    upper_left_y: float
    upper_right_x: float
    upper_right_y: float
    lower_left_x: float
    lower_left_y: float
    lower_right_x: float
    lower_right_y: float

    def __init__(self, *, upper_left_x: float = 0.0, upper_left_y: float = 0.0,
                 upper_right_x: float = 1.0, upper_right_y: float = 0.0,
                 lower_left_x: float = 0.0, lower_left_y: float = 1.0,
                 lower_right_x: float = 1.0, lower_right_y: float = 1.0):
        """初始化裁剪设置, 默认参数表示不裁剪"""
        self.upper_left_x = upper_left_x
        self.upper_left_y = upper_left_y
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
        self.lower_left_x = lower_left_x
        self.lower_left_y = lower_left_y
        self.lower_right_x = lower_right_x
        self.lower_right_y = lower_right_y

    def export_json(self) -> Dict[str, Any]:
        return {
            "upper_left_x": self.upper_left_x,
            "upper_left_y": self.upper_left_y,
            "upper_right_x": self.upper_right_x,
            "upper_right_y": self.upper_right_y,
            "lower_left_x": self.lower_left_x,
            "lower_left_y": self.lower_left_y,
            "lower_right_x": self.lower_right_x,
            "lower_right_y": self.lower_right_y
        }

class Video_material:
    """本地视频素材（视频或图片）, 一份素材可以在多个片段中使用"""

    material_id: str
    """素材全局id, 自动生成"""
    local_material_id: str
    """素材本地id, 意义暂不明确"""
    material_name: str
    """素材名称"""
    path: str
    """素材文件路径"""
    remote_url: Optional[str] = None
    """远程URL地址"""
    duration: int
    """素材时长, 单位为微秒"""
    height: int
    """素材高度"""
    width: int
    """素材宽度"""
    crop_settings: Crop_settings
    """素材裁剪设置"""
    material_type: Literal["video", "photo"]
    """素材类型: 视频或图片"""
    replace_path: Optional[str] = None
    """替换路径, 如果设置了这个值, 在导出json时会用这个路径替代原始path"""

    def __init__(self, material_type: Literal["video", "photo"], 
                 path: Optional[str] = None,
                 replace_path: Optional[str] = None, 
                 material_name: Optional[str] = None, 
                 crop_settings: Crop_settings = Crop_settings(), 
                 remote_url: Optional[str] = None,
                 duration: Optional[float] = None,
                 width: Optional[int] = None,
                 height: Optional[int] = None):
        """从指定位置加载视频（或图片）素材

        Args:
            path (`str`, optional): 素材文件路径, 支持mp4, mov, avi等常见视频文件及jpg, jpeg, png等图片文件.
            replace_path (`str`, optional): 替换路径，用于导出JSON时替代原始path.
            material_type (`Literal["video", "photo"]`, optional): 素材类型，如果指定则优先使用该值.
            material_name (`str`, optional): 素材名称, 如果不指定, 默认使用文件名作为素材名称.
            crop_settings (`Crop_settings`, optional): 素材裁剪设置, 默认不裁剪.
            remote_url (`str`, optional): 远程URL地址.
            duration (`float`, optional): 音频时长（秒），如果提供则跳过ffprobe检测.
            width (`int`, optional): 素材宽度, 如果不指定, 则使用ffprobe获取.
            height (`int`, optional): 素材高度, 如果不指定, 则使用ffprobe获取.

        Raises:
            `ValueError`: 不支持的素材文件类型或缺少必要参数.
            `FileNotFoundError`: 素材文件不存在.
        """
        # 确保至少提供了path或remote_url
        if not path and not remote_url:
            raise ValueError("必须提供 path 或 remote_url 中的至少一个参数")
            
        # 处理远程URL情况
        if remote_url:
            if not material_name:
                raise ValueError("使用 remote_url 参数时必须指定 material_name")
            self.remote_url = remote_url
            self.path = ""  # 远程资源没有本地路径
        else:
            # 处理本地文件情况
            path = os.path.abspath(path)
            if not os.path.exists(path):
                raise FileNotFoundError(f"找不到 {path}")
            self.path = path
            self.remote_url = None

        # 设置素材名称
        self.material_name = material_name if material_name else os.path.basename(path)
        self.material_id = uuid.uuid4().hex
        self.replace_path = replace_path
        self.crop_settings = crop_settings
        self.local_material_id = ""
        self.material_type = material_type

        # 如果是photo类型，跳过ffprobe获取媒体信息的逻辑
        if material_type == "photo":
            self.material_type = "photo"
            self.duration = 10800000000  # 静态图片默认3小时
            # 使用imageio获取图片宽高
            try:
                # img = imageio.imread(self.remote_url)
                # self.height, self.width = img.shape[:2]
                # 使用默认宽高，在下载的时候才会获取真实宽高
                self.width = 0
                self.height = 0
            except Exception as e:
                # 如果获取失败，使用默认值
                self.width = 1920
                self.height = 1080
            return


        # 如果外部提供了duration，直接使用，跳过ffprobe检测
        if duration is not None and width is not None and height is not None:
            self.duration = int(float(duration) * 1e6)  # 转换为微秒
            self.width = width
            self.height = height
            return  # 直接返回，跳过后续的ffprobe检测
        
        # 如果没有提供duration，则使用ffprobe获取
        try:
            # 使用ffprobe获取媒体信息
            media_path = self.path if self.path else self.remote_url
            command = [
                'ffprobe',
                '-v', 'error',
                '-select_streams', 'v:0',  # 选择第一个视频流
                '-show_entries', 'stream=width,height,duration,codec_type',  # 添加codec_type
                '-show_entries', 'format=duration,format_name',  # 添加format_name
                '-of', 'json',
                media_path
            ]
            result = subprocess.check_output(command, stderr=subprocess.STDOUT)
            result_str = result.decode('utf-8')
            # 查找JSON开始位置（第一个'{'）
            json_start = result_str.find('{')
            if json_start != -1:
                json_str = result_str[json_start:]
                info = json.loads(json_str)
            else:
                raise ValueError(f"无法在输出中找到JSON数据: {result_str}")
            
            if 'streams' in info and len(info['streams']) > 0:
                stream = info['streams'][0]
                self.width = int(stream.get('width', 0))
                self.height = int(stream.get('height', 0))
                
                # 如果指定了material_type，则优先使用指定的类型
                if material_type is not None:
                    self.material_type = material_type
                else:
                    # 通过format_name和codec_type判断是否是动态视频
                    format_name = info.get('format', {}).get('format_name', '').lower()
                    codec_type = stream.get('codec_type', '').lower()
                    
                    # 检查是否是GIF或其他动态视频
                    if 'gif' in format_name or (codec_type == 'video' and stream.get('duration') is not None):
                        self.material_type = "video"
                    else:
                        self.material_type = "photo"
                
                # 设置持续时间
                if self.material_type == "video":
                    # 优先使用流的duration，如果没有则使用格式的duration
                    duration = stream.get('duration') or info['format'].get('duration', '0')
                    self.duration = int(float(duration) * 1e6)  # 转换为微秒
                else:
                    self.duration = 10800000000  # 静态图片默认3小时
            else:
                raise ValueError(f"无法获取媒体文件 {media_path} 的流信息")
                
        except subprocess.CalledProcessError as e:
            raise ValueError(f"处理文件 {media_path} 时出错: {e.output.decode('utf-8')}")
        except json.JSONDecodeError as e:
            raise ValueError(f"解析媒体信息时出错: {e}")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Video_material":
        """从字典创建视频素材对象
        
        Args:
            data (Dict[str, Any]): 包含素材信息的字典
            
        Returns:
            Video_material: 新创建的视频素材对象
        """
        # 创建实例但不调用__init__
        instance = cls.__new__(cls)
        
        # 设置基本属性
        instance.material_id = data["id"]
        instance.local_material_id = data.get("local_material_id", "")
        instance.material_name = data["material_name"]
        instance.path = data["path"]
        instance.duration = data["duration"]
        instance.height = data["height"]
        instance.width = data["width"]
        instance.material_type = data["type"]
        instance.replace_path = None  # 默认不设置替换路径
        
        # 设置裁剪设置
        crop_data = data.get("crop", {})
        instance.crop_settings = Crop_settings(
            upper_left_x=crop_data.get("upper_left_x", 0.0),
            upper_left_y=crop_data.get("upper_left_y", 0.0),
            upper_right_x=crop_data.get("upper_right_x", 1.0),
            upper_right_y=crop_data.get("upper_right_y", 0.0),
            lower_left_x=crop_data.get("lower_left_x", 0.0),
            lower_left_y=crop_data.get("lower_left_y", 1.0),
            lower_right_x=crop_data.get("lower_right_x", 1.0),
            lower_right_y=crop_data.get("lower_right_y", 1.0)
        )
        
        return instance

    def export_json(self) -> Dict[str, Any]:
        video_material_json = {
            "audio_fade": None,
            "category_id": "",
            "category_name": "local",
            "check_flag": 63487,
            "crop": self.crop_settings.export_json(),
            "crop_ratio": "free",
            "crop_scale": 1.0,
            "duration": self.duration,
            "height": self.height,
            "id": self.material_id,
            "local_material_id": self.local_material_id,
            "material_id": self.material_id,
            "material_name": self.material_name,
            "media_path": "",
            "path": self.replace_path if self.replace_path is not None else self.path,
            "remote_url": self.remote_url,
            "type": self.material_type,
            "width": self.width
        }
        return video_material_json

class Audio_material:
    """本地音频素材"""

    material_id: str
    """素材全局id, 自动生成"""
    material_name: str
    """素材名称"""
    path: str
    """素材文件路径"""
    remote_url: Optional[str] = None
    """远程URL地址"""
    replace_path: Optional[str] = None
    """替换路径, 如果设置了这个值, 在导出json时会用这个路径替代原始path"""

    has_audio_effect: bool = False
    """是否有音频效果"""

    duration: int
    """素材时长, 单位为微秒"""

    def __init__(self, path: Optional[str] = None, replace_path = None, material_name: Optional[str] = None, 
                 remote_url: Optional[str] = None, duration: Optional[float] = None):
        """从指定位置加载音频素材, 注意视频文件不应该作为音频素材使用
    
        Args:
            path (`str`, optional): 素材文件路径, 支持mp3, wav等常见音频文件.
            material_name (`str`, optional): 素材名称, 如果不指定, 默认使用URL中的文件名作为素材名称.
            remote_url (`str`, optional): 远程URL地址.
            duration (`float`, optional): 音频时长（秒），如果提供则跳过ffprobe检测.
    
        Raises:
            `ValueError`: 不支持的素材文件类型或缺少必要参数.
        """
        if not path and not remote_url:
            raise ValueError("必须提供 path 或 remote_url 中的至少一个参数")
    
        if path:
            path = os.path.abspath(path)
            if not os.path.exists(path):
                raise FileNotFoundError(f"找不到 {path}")
    
        # 从URL中获取文件名作为material_name
        if not material_name and remote_url:
            original_filename = os.path.basename(remote_url.split('?')[0])  # 修复：使用remote_url而不是audio_url
            name_without_ext = os.path.splitext(original_filename)[0]  # 获取不带扩展名的文件名
            material_name = f"{name_without_ext}.mp3"  # 使用原始文件名+时间戳+固定mp3扩展名
        
        self.material_name = material_name if material_name else (os.path.basename(path) if path else "unknown")
        self.material_id = uuid.uuid4().hex
        self.path = path if path else ""
        self.replace_path = replace_path
        self.remote_url = remote_url
        
        # 如果外部提供了duration，直接使用，跳过ffprobe检测
        if duration is not None:
            self.duration = int(float(duration) * 1e6)  # 转换为微秒
            return  # 直接返回，跳过后续的ffprobe检测
        
        # 如果没有提供duration，则使用ffprobe获取
        self.duration = 0  # 初始化为0，如果有path则后续会更新
    
        try:
            # 使用ffprobe获取音频信息
            command = [
                'ffprobe',
                '-v', 'error',
                '-select_streams', 'a:0',  # 选择第一个音频流
                '-show_entries', 'stream=duration',
                '-show_entries', 'format=duration',
                '-of', 'json',
                path if path else remote_url
            ]
            result = subprocess.check_output(command, stderr=subprocess.STDOUT)
            result_str = result.decode('utf-8')
            # 查找JSON开始位置（第一个'{'）
            json_start = result_str.find('{')
            if json_start != -1:
                json_str = result_str[json_start:]
                info = json.loads(json_str)
            else:
                raise ValueError(f"无法在输出中找到JSON数据: {result_str}")

            # 检查是否有视频流
            video_command = [
                'ffprobe',
                '-v', 'error',
                '-select_streams', 'v:0',
                '-show_entries', 'stream=codec_type',
                '-of', 'json',
                path if path else remote_url
            ]
            video_result = subprocess.check_output(video_command, stderr=subprocess.STDOUT)
            video_result_str = video_result.decode('utf-8')
            # 查找JSON开始位置（第一个'{'）
            video_json_start = video_result_str.find('{')
            if video_json_start != -1:
                video_json_str = video_result_str[video_json_start:]
                video_info = json.loads(video_json_str)
            else:
                print(f"无法在输出中找到JSON数据: {video_result_str}")
            
            if 'streams' in video_info and len(video_info['streams']) > 0:
                raise ValueError("音频素材不应包含视频轨道")

            # 检查音频流
            if 'streams' in info and len(info['streams']) > 0:
                stream = info['streams'][0]
                # 优先使用流的duration，如果没有则使用格式的duration
                duration_value = stream.get('duration') or info['format'].get('duration', '0')
                self.duration = int(float(duration_value) * 1e6)  # 转换为微秒
            else:
                raise ValueError(f"给定的素材文件 {path} 没有音频轨道")

        except subprocess.CalledProcessError as e:
            raise ValueError(f"处理文件 {path} 时出错: {e.output.decode('utf-8')}")
        except json.JSONDecodeError as e:
            raise ValueError(f"解析媒体信息时出错: {e}")
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Audio_material":
        """从字典创建音频素材对象
        
        Args:
            data (Dict[str, Any]): 包含素材信息的字典
            
        Returns:
            Audio_material: 新创建的音频素材对象
        """
        # 创建实例但不调用__init__
        instance = cls.__new__(cls)
        
        # 设置基本属性
        instance.material_id = data["id"]
        instance.material_name = data["name"]  # 注意这里是name而不是material_name
        instance.path = data["path"]
        instance.duration = data["duration"]
        instance.replace_path = None  # 默认不设置替换路径
        instance.remote_url = data.get("remote_url")
        
        return instance

    def export_json(self) -> Dict[str, Any]:
        return {
            "app_id": 0,
            "category_id": "",
            "category_name": "local",
            "check_flag": 3 if hasattr(self, 'has_audio_effect') and self.has_audio_effect else 1,
            "copyright_limit_type": "none",
            "duration": self.duration,
            "effect_id": "",
            "formula_id": "",
            "id": self.material_id,
            "intensifies_path": "",
            "is_ai_clone_tone": False,
            "is_text_edit_overdub": False,
            "is_ugc": False,
            "local_material_id": self.material_id,
            "music_id": self.material_id,
            "name": self.material_name,
            "path": self.replace_path if self.replace_path is not None else self.path,
            "remote_url": self.remote_url,
            "query": "",
            "request_id": "",
            "resource_id": "",
            "search_id": "",
            "source_from": "",
            "source_platform": 0,
            "team_id": "",
            "text_id": "",
            "tone_category_id": "",
            "tone_category_name": "",
            "tone_effect_id": "",
            "tone_effect_name": "",
            "tone_platform": "",
            "tone_second_category_id": "",
            "tone_second_category_name": "",
            "tone_speaker": "",
            "tone_type": "",
            "type": "extract_music",
            "video_id": "",
            "wave_points": []
        }
