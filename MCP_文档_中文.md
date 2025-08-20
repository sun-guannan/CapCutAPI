# CapCut API MCP 服务器使用文档

## 概述

CapCut API MCP 服务器是一个基于 Model Context Protocol (MCP) 的视频编辑服务，提供了完整的 CapCut 视频编辑功能接口。通过 MCP 协议，您可以轻松地在各种应用中集成专业级的视频编辑能力。

## 功能特性

### 🎬 核心功能
- **草稿管理**: 创建、保存和管理视频项目
- **多媒体支持**: 视频、音频、图片、文本处理
- **高级效果**: 特效、动画、转场、滤镜
- **精确控制**: 时间轴、关键帧、图层管理

### 🛠️ 可用工具 (11个)

| 工具名称 | 功能描述 | 主要参数 |
|---------|----------|----------|
| `create_draft` | 创建新的视频草稿项目 | width, height |
| `add_text` | 添加文字元素 | text, font_size, color, shadow, background |
| `add_video` | 添加视频轨道 | video_url, start, end, transform, volume |
| `add_audio` | 添加音频轨道 | audio_url, volume, speed, effects |
| `add_image` | 添加图片素材 | image_url, transform, animation, transition |
| `add_subtitle` | 添加字幕文件 | srt_path, font_style, position |
| `add_effect` | 添加视觉特效 | effect_type, parameters, duration |
| `add_sticker` | 添加贴纸元素 | resource_id, position, scale, rotation |
| `add_video_keyframe` | 添加关键帧动画 | property_types, times, values |
| `get_video_duration` | 获取视频时长 | video_url |
| `save_draft` | 保存草稿项目 | draft_id |

## 安装配置

### 环境要求
- Python 3.10+
- CapCut 应用 (macOS/Windows)
- MCP 客户端支持

### 依赖安装
```bash
# 创建虚拟环境
python3.10 -m venv venv-mcp
source venv-mcp/bin/activate  # macOS/Linux
# 或 venv-mcp\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements-mcp.txt
```

### MCP 配置
创建或更新 `mcp_config.json` 文件：

```json
{
  "mcpServers": {
    "capcut-api": {
      "command": "python3.10",
      "args": ["mcp_server.py"],
      "cwd": "/path/to/CapCutAPI-dev",
      "env": {
        "PYTHONPATH": "/path/to/CapCutAPI-dev"
      }
    }
  }
}
```

## 使用指南

### 基础工作流程

#### 1. 创建草稿
```python
# 创建 1080x1920 竖屏项目
result = mcp_client.call_tool("create_draft", {
    "width": 1080,
    "height": 1920
})
draft_id = result["draft_id"]
```

#### 2. 添加内容
```python
# 添加标题文字
mcp_client.call_tool("add_text", {
    "text": "我的视频标题",
    "start": 0,
    "end": 5,
    "draft_id": draft_id,
    "font_size": 48,
    "font_color": "#FFFFFF"
})

# 添加背景视频
mcp_client.call_tool("add_video", {
    "video_url": "https://example.com/video.mp4",
    "draft_id": draft_id,
    "start": 0,
    "end": 10,
    "volume": 0.8
})
```

#### 3. 保存项目
```python
# 保存草稿
result = mcp_client.call_tool("save_draft", {
    "draft_id": draft_id
})
```

### 高级功能示例

#### 文字样式设置
```python
# 带阴影和背景的文字
mcp_client.call_tool("add_text", {
    "text": "高级文字效果",
    "draft_id": draft_id,
    "font_size": 56,
    "font_color": "#FFD700",
    "shadow_enabled": True,
    "shadow_color": "#000000",
    "shadow_alpha": 0.8,
    "background_color": "#1E1E1E",
    "background_alpha": 0.7,
    "background_round_radius": 15
})
```

#### 关键帧动画
```python
# 缩放和透明度动画
mcp_client.call_tool("add_video_keyframe", {
    "draft_id": draft_id,
    "track_name": "video_main",
    "property_types": ["scale_x", "scale_y", "alpha"],
    "times": [0, 2, 4],
    "values": ["1.0", "1.5", "0.5"]
})
```

#### 多样式文本
```python
# 不同颜色的文字段落
mcp_client.call_tool("add_text", {
    "text": "彩色文字效果",
    "draft_id": draft_id,
    "text_styles": [
        {"start": 0, "end": 2, "font_color": "#FF0000"},
        {"start": 2, "end": 4, "font_color": "#00FF00"}
    ]
})
```

## 测试验证

### 使用测试客户端
```bash
# 运行测试客户端
python test_mcp_client.py
```

### 功能验证清单
- [ ] 服务器启动成功
- [ ] 工具列表获取正常
- [ ] 草稿创建功能
- [ ] 文本添加功能
- [ ] 视频/音频/图片添加
- [ ] 特效和动画功能
- [ ] 草稿保存功能

## 故障排除

### 常见问题

#### 1. "CapCut modules not available"
**解决方案**:
- 确认 CapCut 应用已安装
- 检查 Python 路径配置
- 验证依赖包安装

#### 2. 服务器启动失败
**解决方案**:
- 检查虚拟环境激活
- 验证配置文件路径
- 查看错误日志

#### 3. 工具调用错误
**解决方案**:
- 检查参数格式
- 验证媒体文件URL
- 确认时间范围设置

### 调试模式
```bash
# 启用详细日志
export DEBUG=1
python mcp_server.py
```

## 最佳实践

### 性能优化
1. **媒体文件**: 使用压缩格式，避免过大文件
2. **时间管理**: 合理规划元素时间轴，避免重叠
3. **内存使用**: 及时保存草稿，清理临时文件

### 错误处理
1. **参数验证**: 调用前检查必需参数
2. **异常捕获**: 处理网络和文件错误
3. **重试机制**: 对临时失败进行重试

## API 参考

### 通用参数
- `draft_id`: 草稿唯一标识符
- `start/end`: 时间范围（秒）
- `width/height`: 项目尺寸
- `transform_x/y`: 位置坐标
- `scale_x/y`: 缩放比例

### 返回格式
```json
{
  "success": true,
  "result": {
    "draft_id": "kox_jy_xxx",
    "draft_url": "https://..."
  },
  "features_used": {
    "shadow": false,
    "background": false,
    "multi_style": false
  }
}
```

## 更新日志

### v1.0.0
- 初始版本发布
- 支持 11 个核心工具
- 完整的 MCP 协议实现

## 技术支持

如有问题或建议，请通过以下方式联系：
- GitHub Issues
- 技术文档
- 社区论坛

---

*本文档持续更新，请关注最新版本。*