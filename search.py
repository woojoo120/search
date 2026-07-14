import streamlit as st
import pandas as pd

if "bot_message" not in st.session_state:
    st.session_state.bot_message = "무엇을 도와드릴까요?"

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

#로고

st.logo("인화여고로고.png")

#메인 타이틀

st.markdown("""
<h1 style="text-align:center; margin-bottom:35px;">
인화여고 전자도서관
</h1>
""", unsafe_allow_html=True)

#AI 스마일봇

col1, col2 = st.columns([0.8, 8], vertical_alignment="center")

with col1:
    if st.button("😊", use_container_width=True):
        st.session_state.chat_open = True

with col2:
    st.markdown(f"""
    <style>
    .bubble {{
        position: relative;
        display: inline-block;
        background: #F5F5F5;
        border-radius: 20px;
        padding: 12px 20px;
        font-size: 17px;
        max-width: 600px;
        word-break: break-word;
    }}

    .bubble::before {{
        content: "";
        position: absolute;
        left: -12px;
        top: 18px;
        width: 0;
        height: 0;
        border-top: 10px solid transparent;
        border-bottom: 10px solid transparent;
        border-right: 12px solid #F5F5F5;
    }}
    </style>

    <div class="bubble">
        {st.session_state.bot_message}
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1.2, 4.5, 1.2, 1])  
with col1: advanced = st.toggle("고급검색")
with col2: keyword = st.text_input( "", placeholder="검색어를 입력해주세요", label_visibility="collapsed" ) 

# 검색 기준 

with col3: search_type = st.selectbox( "", ["제목", "저자", "출판사"], label_visibility="collapsed" ) 

# 검색 버튼 

with col4: search = st.button("🔍 검색", use_container_width=True)

#고급 검색

if advanced:

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        category = st.selectbox(
            "주제별 검색",
            [
                "철학",
                "종교",
                "사회과학",
                "자연과학",
                "기술과학",
                "예술",
                "언어",
                "문학",
            ],
        )

    with c2:
        detail_type = st.selectbox(
            "검색 조건",
            [
                "제목",
                "저자",
                "출판사",
            ],
        )