import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Yohan Vinu")
    content = """Hi, I'm Yohan. I'll be majoring in Computer Science at SRMIST, KTR."""
    st.info(content)