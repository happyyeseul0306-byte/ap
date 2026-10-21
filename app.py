from datetime import date, time
import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="StarPort - 여행지 & 항공권", page_icon="🚀", layout="wide"
)

# 2. 스타일 및 CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #05132d;
        color: white;
    }
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        margin-bottom: 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .search-box-wrapper {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        margin-top: 15px;
        margin-bottom: 40px;
    }
    .flight-card {
        background-color: #ffffff;
        color: #05132d;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        border: 1px solid #e5e7eb;
    }
    .eticket-box {
        background: #ffffff;
        color: #05132d;
        border: 2px solid #05132d;
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    }
    .dest-info-box {
        background-color: #ffffff;
        color: #05132d;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }
    
    /* 검색 영역 라벨 색상 */
    div[data-testid="stSelectbox"] label p,
    div[data-testid="stDateInput"] label p,
    div[data-testid="stSlider"] label p {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }

    /* 입력창 Placeholder 스타일 */
    input::placeholder {
        color: #475569 !important;
        opacity: 1 !important;
        font-weight: 600 !important;
    }

    /* 상단 우측 로그인 버튼 */
    .stButton button[kind="secondary"] {
        background-color: transparent;
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.9rem;
    }
    .stButton button[kind="secondary"]:hover {
        background-color: rgba(255, 255, 255, 0.1);
        border-color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 세션 상태 초기화
if "step" not in st
