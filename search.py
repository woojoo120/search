import streamlit as st
import pandas as pd

# 세션 상태 초기화
if "bot_message" not in st.session_state:
    st.session_state.bot_message = "무엇을 도와드릴까요?"

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# 로고
st.logo("인화여고로고.png")

# 메인 타이틀
st.markdown("""
<div style="text-align:center; margin-bottom:35px; font-family: sans-serif;">
    <h1 style="margin:0; padding:0; font-size: 2.5rem; font-weight: bold; word-break: keep-all;">
        인화여고 전자도서관
    </h1>
    <div style="font-size: 0.9rem; color: #888888; font-weight: 500; letter-spacing: 0.12em; margin-top: 7px; text-transform: uppercase;">
        Inhwa Girl's High School Library
    </div>
</div>
""", unsafe_allow_html=True)
st.divider()

st.markdown("""
<style>

    div[data-testid="stChatMessageAvatar"],
    .st-emotion-cache-12w0qpk, 
    .st-emotion-cache-p4m61c {
        display: none !important;
        width: 0px !important;
        height: 0px !important;
    }
    
    div[data-testid="stChatMessageContent"] {
        margin-left: 0 !important;
        padding: 0 !important;
    }
    
    div[data-testid="stChatMessage"] {
        padding: 8px 14px !important;
        background-color: #f0f2f6 !important;
        border-radius: 8px !important;
        min-height: 38px !important;
        display: flex !important;
        align-items: center !important;
    }

    div[data-testid="stChatMessageContent"] p {
        font-size: 14px !important;
        margin: 0 !important;
        line-height: 1.2 !important;
        color: #333333;
    }
            
    div[data-testid="stHorizontalBlock"] button {
        padding: 0 !important;
        font-size: 18px !important;
        height: 38px !important;
    }
</style>
""", unsafe_allow_html=True)

col_btn, col_msg, col_empty = st.columns([0.5, 3.5, 4])

with col_btn:
    if st.button("😊", use_container_width=True):
        st.session_state.chat_open = not st.session_state.chat_open
# 버튼 누를 떄
with col_msg:
    if st.session_state.chat_open:
        with st.chat_message("assistant", avatar=None):
            st.write(st.session_state.bot_message)


st.write("")


col1, col2, col3, col4 = st.columns([1.2, 4.5, 1.2, 1])  
with col1: 
    advanced = st.toggle("고급검색")
with col2: 
    keyword = st.text_input("", placeholder="검색어를 입력해주세요", label_visibility="collapsed") 

# 검색 기준 
with col3: 
    search_type = st.selectbox("", ["제목", "저자", "출판사"], label_visibility="collapsed") 

# 검색 버튼 
with col4: 
    search = st.button("🔍 검색", use_container_width=True)

# 고급 검색
if advanced:
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        category = st.selectbox(
            "주제별 검색",
            ["철학", "종교", "사회과학", "자연과학", "기술과학", "예술", "언어", "문학"],
        )
    with c2:
        detail_type = st.selectbox(
            "검색 조건",
            ["제목", "저자", "출판사"],
        )