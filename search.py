import streamlit as st
import pandas as pd

# 검색 페이지

st.logo(
    image="C:/Users/user/Desktop/인화여고로고.jpg"
)

st.markdown(
    """
    <h1 style="text-align: center;">
        인화여고 전자 도서관
    </h1>
    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.checkbox("고급검색", [""])


