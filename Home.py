import streamlit as st
import pandas

st.set_page_config(layout="wide")

ecol, col1, col2, ecol4 = st.columns([0.1, 0.5, 0.5, 0.2])

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Yohan Vinu")
    content = """Hi, I'm Yohan. I'm a CS major at SRMIST, KTR. 
    Below you can find some of the apps I have built in Python. Feel free to contact me."""
    st.info(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")