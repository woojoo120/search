import streamlit as st
import pandas as pd

if "bot_message" not in st.session_state:
    st.session_state.bot_message = "무엇을 도와드릴까요?"

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# 로고
st.logo("인화여고로고.png", size="large")

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

# 챗봇 아이콘
st.markdown(f"""
<style>
    div.st-key-chat_toggle_btn {{
        position: relative;
        width: 46px;
    }}
    div.st-key-chat_toggle_btn button {{
        border-radius: 50% !important;
        width: 46px !important;
        height: 46px !important;
        font-size: 22px !important;
        padding: 0 !important;
        border: 1px solid #e5e5e5 !important;
        background-color: #ffffff !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }}
    # 챗봇 말풍선 스타일
    .chat-bubble {{
        position: relative;
        background-color: #f0f2f6;
        border: 1px solid #e5e5e5;
        border-radius: 18px;
        padding: 10px 16px;
        font-size: 14px;
        color: #333333;
        margin-top: 12px;
        width: fit-content;
        white-space: nowrap;
    }}
    .chat-bubble::before {{
        content: "";
        position: absolute;
        top: -9px;
        left: 20px;
        width: 0;
        height: 0;
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        border-bottom: 9px solid #f0f2f6;
    }}
    .chat-bubble::after {{
        content: "";
        position: absolute;
        top: -10.5px;
        left: 19px;
        width: 0;
        height: 0;
        border-left: 9px solid transparent;
        border-right: 9px solid transparent;
        border-bottom: 10px solid #e5e5e5;
        z-index: -1;
    }}
</style>
""", unsafe_allow_html=True)

# 챗봇
col_widget, col_empty = st.columns([2, 6])
with col_widget:
    if st.button("🙂", key="chat_toggle_btn", help="챗봇 열기/닫기"):
        st.session_state.chat_open = not st.session_state.chat_open


# 대화 기록
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("assistant", "안녕하세요 🙂\n인화여고 전자도서관 AI입니다.\n무엇을 도와드릴까요?")
    ]

if st.session_state.chat_open:

    with st.container(border=True):
        st.markdown("### 🙂 인화여고 전자 도서관 인공지능")
        for role, message in st.session_state.chat_history:
            with st.chat_message(role):
                st.write(message)

    user_input = st.chat_input("도서 추천이나 문의를 입력하세요.")
    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        answer = "AI의 답변이 여기에 표시됩니다."
        st.session_state.chat_history.append(("assistant", answer))
        st.rerun()

st.markdown("<div style='margin-bottom:20px;'></div>", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns([1.6, 4.4, 1.6, 1])  
with col1: 
    advanced = st.toggle("고급검색")
with col2: 
    keyword = st.text_input("", placeholder="검색어를 입력해주세요", label_visibility="collapsed") 

# 검색 기준 
with col3: 
    search_type = st.selectbox("", ["제목", "저자", "출판사"], label_visibility="collapsed") 

# 검색 버튼 
with col4: 
    search = st.button("검색", use_container_width=True)

# 고급 검색
if advanced:
    st.markdown("---")
    c1, c2, c3 = st.columns([2, 7, 1])
    with c1:
        category = st.selectbox(
            "주제별 검색",
            ["철학", "종교", "사회과학", "자연과학", "기술과학", "예술", "언어", "문학"],
        )
    with c2:
        Search_query = st.text_input(
            "주제어 입력"
        )
    with c3:
        st.html("<div style='margin-top: 12px;'></div>")
        search_advanced = st.button("🔍", use_container_width=True
        )
