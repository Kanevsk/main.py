import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    A frequent criticism of millennials is that they are entitled narcissistic snowflakes 
    who have a profound aversion to adulting. 
    Lazy, delusional, incapable of making a meaningful contribution to society, 
    notorious for their self-centered approach to life – these are the alleged signature traits of millennials. 
    """
    st.info(content)

content2 = """
While this generation is not without its flaws, such a negative take on today’s twenty-somethings could
 present certain difficulties when confronted with the real state of affairs. 
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")