# app/main.py
import streamlit as st
from ai_handler import generate_structured_text
from word_generator import generate_word_file

st.set_page_config(page_title="红头文生成 Demo", page_icon="📝")

st.title("🟥 红头文件生成系统 Demo")
st.write("输入一段自由文本，生成结构化红头文案。")

raw_text = st.text_area("请输入原始文稿：", height=240, placeholder="例如：我们计划在下月启动……")

if st.button("生成红头 Word 文件"):
    with st.spinner("AI 正在结构化并生成 Word……"):
        data = generate_structured_text(raw_text)
        st.subheader("🔎 结构化结果")
        st.json(data)
        output_path = generate_word_file(data)
        st.success("✅ 生成成功！")
        with open(output_path, "rb") as f:
            st.download_button("📥 下载红头文件", f, file_name=output_path, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
