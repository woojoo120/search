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


# 🎨 UI를 깔끔하게 다듬는 CSS (주황색 아이콘 제거, 텍스트 수직 정렬, 이모지 버튼 크기 정렬)
st.markdown("""
<style>
    /* 1. 주황색 아이콘 및 챗봇 원형 배경 강제 숨기기 */
    div[data-testid="stChatMessageAvatar"],
    .st-emotion-cache-12w0qpk, 
    .st-emotion-cache-p4m61c {
        display: none !important;
        width: 0px !important;
        height: 0px !important;
    }
    
    /* 2. 아이콘이 사라진 말풍선 여백 밀착 조절 */
    div[data-testid="stChatMessageContent"] {
        margin-left: 0 !important;
        padding: 0 !important;
    }
    
    /* 3. 말풍선 패딩 및 높이 최적화 (검색 버튼 높이와 정렬) */
    div[data-testid="stChatMessage"] {
        padding: 8px 14px !important;
        background-color: #f0f2f6 !important;
        border-radius: 8px !important;
        min-height: 38px !important;
        display: flex !important;
        align-items: center !important; /* 세로 중앙 정렬 */
    }

    /* 4. 말풍선 내 글자가 아래로 쏠리지 않게 정렬 */
    div[data-testid="stChatMessageContent"] p {
        font-size: 14px !important;
        margin: 0 !important;
        line-height: 1.2 !important; /* 높이 쏠림 해결 */
        color: #333333;
    }
    
    /* 5. 스마일 버튼 내 이모지 크기가 삐져나오지 않게 패딩 조절 */
    div[data-testid="stHorizontalBlock"] button {
        padding: 0 !important;
        font-size: 18px !important;
        height: 38px !important; /* 말풍선 높이와 통일 */
    }
</style>
""", unsafe_allow_html=True)


# 💡 스마일 버튼과 말풍선 배치 레이아웃
col_btn, col_msg, col_empty = st.columns([0.5, 3.5, 4])

with col_btn:
    # 버튼을 누르면 세션 상태를 True로 변경하여 말풍선이 뜨게 유도합니다.
    if st.button("😊", use_container_width=True):
        st.session_state.chat_open = not st.session_state.chat_open  # 클릭 시 켜고 끄기 토글

with col_msg:
    # 버튼이 눌려 활성화 상태일 때만 말풍선을 노출합니다.
    if st.session_state.chat_open:
        with st.chat_message("assistant", avatar=None):
            st.write(st.session_state.bot_message)


# 검색창과의 사이 간격을 위한 여백
st.write("")

# 검색 영역 레이아웃
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