# AIGC 图片生成器

> 基于通义万相大模型的 AI 图片生成应用 | AIGC 实践项目

输入文字描述，AI 自动生成对应图片。支持多种风格（水彩、油画、卡通、赛博朋克、水墨等）和尺寸选择。

### 技术栈

`Python` `Streamlit` `通义万相 API` `DashScope`

### 快速开始

1. 复制配置文件并填入 API Key
```bash
cp config.example.py config.py
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动应用
```bash
streamlit run aigc_app.py
```

### 什么是 AIGC

AIGC（AI Generated Content）指利用人工智能自动生成内容——包括文字、图片、音频、视频等。这个项目演示了 AIGC 中最常见的应用场景：文生图（Text-to-Image）。
