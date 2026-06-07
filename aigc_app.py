# -*- coding: utf-8 -*-
"""
AIGC图片生成器 —— 文生图实践项目
调用通义万相 API，输入文字描述即可生成图片
"""
import streamlit as st
import dashscope
from dashscope import ImageSynthesis
import requests
import datetime

# ---------- 配置 ----------
st.set_page_config(page_title="AIGC图片生成器", page_icon="🎨", layout="centered")

# API Key
from config import DASHSCOPE_API_KEY
dashscope.api_key = DASHSCOPE_API_KEY

# ---------- 界面 ----------
st.title("🎨 AIGC 图片生成器")
st.caption("基于通义万相大模型 | 输入一句话，AI帮你画出来")

with st.sidebar:
    st.markdown("### 生成设置")
    style = st.selectbox(
        "图片风格",
        ["<无特定风格>", "水彩画", "油画", "卡通风格", "赛博朋克", "水墨画", "素描", "复古胶片"]
    )
    st.divider()
    st.markdown("### 关于 AIGC")
    st.caption("AIGC 即 AI 生成内容。这个工具演示了文生图的完整流程——你描述画面，AI 生成图片。")

col1, col2 = st.columns([3, 1])
with col1:
    prompt = st.text_area(
        "描述你想生成的画面",
        placeholder="例如：一只橘猫在图书馆看书，阳光透过窗户照在书页上，温暖治愈的画风",
        height=100
    )
with col2:
    generate_btn = st.button("生成图片", type="primary", use_container_width=True)

st.divider()

# ---------- 图片生成 ----------
if generate_btn:
    if not prompt.strip():
        st.warning("请先输入画面描述再生成～")
    else:
        style_map = {
            "<无特定风格>": "",
            "水彩画": "，水彩画风格，色彩柔和通透",
            "油画": "，油画风格，笔触厚实有质感",
            "卡通风格": "，卡通动漫风格，色彩明快线条清晰",
            "赛博朋克": "，赛博朋克风格，霓虹灯光，科技感",
            "水墨画": "，中国水墨画风格，留白意境",
            "素描": "，素描风格，黑白铅笔线条",
            "复古胶片": "，复古胶片风格，暖色调颗粒感"
        }
        full_prompt = prompt + style_map[style]

        with st.spinner("AI 正在作画，请稍等..."):
            try:
                result = ImageSynthesis.call(
                    model="wanx-v1",
                    prompt=full_prompt,
                    n=1,
                    size="1024*1024"
                )
                if result.status_code == 200 and result.output.results:
                    img_url = result.output.results[0].url
                    img_bytes = requests.get(img_url).content
                    st.success("✅ 生成完成！")
                    st.image(img_bytes, caption=f"你的描述：{prompt[:80]}...", use_container_width=True)
                    st.download_button(
                        label="下载图片",
                        data=img_bytes,
                        file_name=f"aigc_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                        mime="image/png"
                    )
                else:
                    st.error(f"生成失败：{result.message if hasattr(result, 'message') else '请检查 API Key'}")
            except Exception as e:
                st.error(f"请求出错：{str(e)[:100]}")

st.divider()
st.caption("💡 提示：描述越具体效果越好。试试「主体 + 场景 + 氛围 + 风格」的组合。")
