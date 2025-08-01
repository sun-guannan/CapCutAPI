# CapCutAPI

轻量、灵活、易上手的剪映/CapCutAPI工具，构建全自动化视频剪辑/混剪流水线。

直接体验：https://www.capcutapi.top

## 效果演示
**通过工具，将AI生成的图片，视频组合起来**

[![Horse](https://img.youtube.com/vi/IF1RDFGOtEU/hqdefault.jpg)](https://www.youtube.com/watch?v=IF1RDFGOtEU)

[![Song](https://img.youtube.com/vi/rGNLE_slAJ8/hqdefault.jpg)](https://www.youtube.com/watch?v=rGNLE_slAJ8)

## 项目功能

本项目是一个基于Python的剪映/CapCut处理工具，提供以下核心功能：

### 核心功能

- **草稿文件管理**：创建、读取、修改和保存剪映/CapCut草稿文件
- **素材处理**：支持视频、音频、图片、文本、贴纸等多种素材的添加和编辑
- **特效应用**：支持添加转场、滤镜、蒙版、动画等多种特效
- **API服务**：提供HTTP API接口，支持远程调用和自动化处理
- **AI集成**：集成多种AI服务，支持智能生成字幕、文本和图像

### 主要API接口

- `/create_draft`创建草稿
- `/add_video`：添加视频素材到草稿
- `/add_audio`：添加音频素材到草稿
- `/add_image`：添加图片素材到草稿
- `/add_text`：添加文本素材到草稿
- `/add_subtitle`：添加字幕到草稿
- `/add_effect`：添加特效到素材
- `/add_sticker`：添加贴纸到草稿
- `/save_draft`：保存草稿文件

## 配置说明

### 配置文件

项目支持通过配置文件进行自定义设置。要使用配置文件：

1. 复制`config.json.example`为`config.json`
2. 根据需要修改配置项

```bash
cp config.json.example config.json
```

### 环境配置

#### ffmpeg

本项目依赖于ffmpeg，您需要确保系统中已安装ffmpeg，并且将其添加到系统的环境变量中。

#### Python 环境

本项目需要 Python 3.8.20 版本，请确保您的系统已安装正确版本的 Python。

#### 安装依赖

安装项目所需的依赖包：

```bash
pip install -r requirements.txt
```

### 运行服务器

完成配置和环境设置后，执行以下命令启动服务器：

```bash
python capcut_server.py
```

服务器启动后，您可以通过 API 接口访问相关功能。

## 使用示例

### 添加视频

```python
import requests

response = requests.post("http://localhost:9001/add_video", json={
    "video_url": "http://example.com/video.mp4",
    "start": 0,
    "end": 10,
    "width": 1080,
    "height": 1920
})

print(response.json())
```

### 添加文本

```python
import requests

response = requests.post("http://localhost:9001/add_text", json={
    "text": "你好，世界！",
    "start": 0,
    "end": 3,
    "font": "思源黑体",
    "font_color": "#FF0000",
    "font_size": 30.0
})

print(response.json())
```

### 保存草稿

```python
import requests

response = requests.post("http://localhost:9001/save_draft", json={
    "draft_id": "123456",
    "draft_folder":"your capcut draft folder"
})

print(response.json())
```
也可以用 REST Client 的 ```rest_client_test.http``` 进行http测试，只需要安装对应的IDE插件

### 复制草稿到剪映/capcut草稿路径
调用`save_draft`会在服务器当前目录下生成一个`dfd_`开头的文件夹，将他复制到剪映/CapCut草稿目录，即可看到生成的草稿


### 更多示例
请参考项目的`example.py`文件，其中包含了更多的使用示例，如添加音频、添加特效等。


## 项目特点

- **跨平台支持**：同时支持剪映和CapCut国际版
- **自动化处理**：支持批量处理和自动化工作流
- **丰富的API**：提供全面的API接口，方便集成到其他系统
- **灵活的配置**：通过配置文件实现灵活的功能定制
- **AI增强**：集成多种AI服务，提升视频制作效率

## 进群交流
![image](https://github.com/user-attachments/assets/2103d43a-bfa4-4739-9c58-82552aa7e92c)

- 反馈问题
- 功能建议
- 最新消息

## 合作
- 你想要利用这个API批量制作**出海**视频吗？
我提供免费的咨询服务，帮助你利用这个API制作。
相应的，我要将工作流代码放到这个项目里公开出来。

- 有兴趣加入我们？
我们的目标是提供稳定可靠的视频剪辑工具，方便融合AI生成的图片/视频/语音。
如果你有兴趣，可以先从将工程里的中文翻译成英文开始！提交pr，我会看到。
更深入的，还有MCP剪辑Agent, web剪辑端，云渲染这三个模块代码还没有开源出来。

- 联系方式
微信：sguann
抖音：剪映草稿助手
