# CapCutAPI

Open source CapCut API tool.

Try It: https://www.capcutapi.top

[中文说明](https://github.com/sun-guannan/CapCutAPI/blob/main/README-zh.md)

## Gallery

**Connect AI generated via CapCutAPI**

[![Horse](https://img.youtube.com/vi/IF1RDFGOtEU/hqdefault.jpg)](https://www.youtube.com/watch?v=IF1RDFGOtEU)

[![Song](https://img.youtube.com/vi/rGNLE_slAJ8/hqdefault.jpg)](https://www.youtube.com/watch?v=rGNLE_slAJ8)

## Project Features

This project is a Python-based CapCut processing tool that offers the following core functionalities:

### Core Features

- **Draft File Management**: Create, read, modify, and save CapCut draft files
- **Material Processing**: Support adding and editing various materials such as videos, audios, images, texts, stickers, etc.
- **Effect Application**: Support adding multiple effects like transitions, filters, masks, animations, etc.
- **API Service**: Provide HTTP API interfaces to support remote calls and automated processing
- **AI Integration**: Integrate multiple AI services to support intelligent generation of subtitles, texts, and images

### Main API Interfaces

- `/create_draft`: Create a draft
- `/add_video`: Add video material to the draft
- `/add_audio`: Add audio material to the draft
- `/add_image`: Add image material to the draft
- `/add_text`: Add text material to the draft
- `/add_subtitle`: Add subtitles to the draft
- `/add_effect`: Add effects to materials
- `/add_sticker`: Add stickers to the draft
- `/save_draft`: Save the draft file

## Configuration Instructions

### Configuration File

The project supports custom settings through a configuration file. To use the configuration file:

1. Copy `config.json.example` to `config.json`
2. Modify the configuration items as needed

```bash
cp config.json.example config.json
```

### Environment Configuration

#### ffmpeg

This project depends on ffmpeg. You need to ensure that ffmpeg is installed on your system and added to the system's environment variables.

#### Python Environment

This project requires Python version 3.8.20. Please ensure that the correct version of Python is installed on your system.

#### Install Dependencies

Install the required dependency packages for the project:

```bash
pip install -r requirements.txt
```

### Run the Server

After completing the configuration and environment setup, execute the following command to start the server:

```bash
python capcut_server.py
```

Once the server is started, you can access the related functions through the API interfaces.

## Usage Examples

### Adding a Video

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

### Adding Text

```python
import requests

response = requests.post("http://localhost:9001/add_text", json={
    "text": "Hello, World!",
    "start": 0,
    "end": 3,
    "font": "ZY_Courage",
    "font_color": "#FF0000",
    "font_size": 30.0
})

print(response.json())
```

### Saving a Draft

```python
import requests

response = requests.post("http://localhost:9001/save_draft", json={
    "draft_id": "123456",
    "draft_folder": "your capcut draft folder"
})

print(response.json())
```
You can also use the ```rest_client_test.http``` file of the REST Client for HTTP testing. Just need to install the corresponding IDE plugin

### Copying the Draft to CapCut Draft Path

Calling `save_draft` will generate a folder starting with `dfd_` in the current directory of the server. Copy this folder to the CapCut draft directory, and you will be able to see the generated draft.

### More Examples

Please refer to the `example.py` file in the project, which contains more usage examples such as adding audio and effects.

## Project Features

- **Cross-platform Support**: Supports both CapCut China version and CapCut International version
- **Automated Processing**: Supports batch processing and automated workflows
- **Rich APIs**: Provides comprehensive API interfaces for easy integration into other systems
- **Flexible Configuration**: Achieve flexible function customization through configuration files
- **AI Enhancement**: Integrate multiple AI services to improve video production efficiency
