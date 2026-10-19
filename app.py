import streamlit as st
import streamlit.components.v1 as components
from datetime import date

# 1. 페이지 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="StarPort - 여행지 & 항공권", 
    page_icon="🚀", 
    layout="wide"
)

# 2. 스타일 및 CSS
st.markdown("""
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
    
    /* 로그인 폼 내부 입력창 라벨 색상 고정 (흰색으로 변경하여 남색 배경에서 잘 보이도록 처리) */
    div[data-testid="stForm"] label {
        background-color: transparent !important;
    }
    div[data-testid="stForm"] label p {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    /* 항공편 선택 화면의 셀렉트박스 라벨 색상을 흰색으로 변경 */
    div[data-testid="stSelectbox"] label p {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* 입력창 내부 안내 텍스트(Placeholder) 색상 선명하게 변경 */
    input::placeholder {
        color: #475569 !important;
        opacity: 1 !important;
        font-weight: 600 !important;
    }

    /* 상단 우측 로그인 버튼 컴팩트 스타일 */
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
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = "home"
if "booking_data" not in st.session_state:
    st.session_state.booking_data = {}
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "selected_destination_info" not in st.session_state:
    st.session_state.selected_destination_info = "도쿄"

# ==========================================
# 1. 홈 화면
# ==========================================
if st.session_state.step == "home":
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([2, 4.5, 1, 0.8])
    with nav_col1:
        st.markdown("<h2 style='color: white; margin: 0; font-size: 1.5rem;'>🚀 StarPort</h2>", unsafe_allow_html=True)
    with nav_col2:
        st.markdown("<p style='color: #94a3b8; margin: 5px 0 0 0;'>전 세계 항공권 비교 및 여행지 가이드</p>", unsafe_allow_html=True)
    with nav_col3:
        pass
    with nav_col4:
        if st.session_state.is_logged_in:
            if st.button(f"👤 {st.session_state.user_email[:4]}...", type="secondary", use_container_width=True):
                st.info(f"현재 접속 계정: {st.session_state.user_email}")
        else:
            if st.button("👤 로그인", type="secondary", use_container_width=True):
                st.session_state.step = "login"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white; text-align: center; font-size: 2.2rem; margin-bottom: 5px;'>수백만 개의 항공권, 검색 한 번으로 간단하게.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; text-align: center; margin-bottom: 25px;'>원하는 일정의 항공편을 실시간으로 비교하고 예매하세요.</p>", unsafe_allow_html=True)
    
    destinations_list = [
        # 일본 (8곳)
        "도쿄/나리타 (NRT) - 일본", "도쿄/하네다 (HND) - 일본", "오사카/간사이 (KIX) - 일본", "후쿠오카 (FUK) - 일본",
        "삿포로/신치토세 (CTS) - 일본", "오키나와 (OKA) - 일본", "나고야 (NGO) - 일본", "시즈오카 (FSZ) - 일본",
        # 동남아시아 (15곳)
        "방콕/수완나품 (BKK) - 태국", "치앙마이 (CNX) - 태국", "푸켓 (HKT) - 태국", "다낭 (DAD) - 베트남",
        "나트랑/캄란 (CXR) - 베트남", "호치민 (SGN) - 베트남", "하노이 (HAN) - 베트남", "푸꾸옥 (PQC) - 베트남",
        "싱가포르 (SIN) - 싱가포르", "쿠알라룸푸르 (KUL) - 말레이시아", "코타키나발루 (BKI) - 말레이시아",
        "세부 (CEB) - 필리핀", "보홀 (TAG) - 필리핀", "마닐라 (MNL) - 필리핀", "발리/덴파사르 (DPS) - 인도네시아",
        # 동북아 / 중앙아시아 (7곳)
        "홍콩 (HKG) - 홍콩", "마카오 (MFM) - 마카오", "타이베이/타오위안 (TPE) - 대만", "가오슝 (KHH) - 대만",
        "베이징/서두 (PEK) - 중국", "상하이/푸동 (PVG) - 중국", "울란바토르 (ULN) - 몽골",
        # 유럽 (12곳)
        "파리/샤를드골 (CDG) - 프랑스", "런던/히드로 (LHR) - 영국", "로마/피우미치노 (FCO) - 이탈리아",
        "바르셀로나 (BCN) - 스페인", "프랑크푸르트 (FRA) - 독일", "스위스/취리히 (ZRH) - 스위스",
        "체코/프라하 (PRG) - 체코", "오스트리아/빈 (VIE) - 오스트리아", "튀르키예/이스탄불 (IST) - 튀르키예",
        "네덜란드/암스테르담 (AMS) - 네덜란드", "폴란드/바르샤바 (WAW) - 폴란드", "러시아/모스크바 (SVO) - 러시아",
        # 미주 및 대양주 / 중동 (11곳)
        "뉴욕/JFK (JFK) - 미국", "로스앤젤레스 (LAX) - 미국", "샌프란시스코 (SFO) - 미국", "시애틀 (SEA) - 미국",
        "하와이/호놀룰루 (HNL) - 미국", "밴쿠버 (YVR) - 캐나다", "토론토 (YYZ) - 캐나다",
        "시드니 (SYD) - 호주", "멜버른 (MEL) - 호주", "괌 (GUM) - 괌", "사이판 (SPN) - 사이판", "두바이 (DXB) - 아랍에미리트"
    ]

    departure_list = [
        "서울/인천 (ICN)", "서울/김포 (GMP)", "부산/김해 (PUS)", 
        "제주 (CJU)", "청주 (CJJ)", "대구 (TAE)", "무안 (MWX)"
    ]

    with st.container():
        st.markdown('<div class="search-box-wrapper">', unsafe_allow_html=True)
        
        sc1, sc2, sc3, sc4, sc5 = st.columns([1.2, 1.5, 1.1, 1.1, 0.9])
        
        with sc1:
            departure = st.selectbox("🛫 출발지", departure_list)
        with sc2:
            destination = st.selectbox("🛬 도착지", destinations_list)
        with sc3:
            travel_date = st.date_input("📅 가는 날", min_value=date.today())
        with sc4:
            travel_time = st.selectbox("⏰ 시간대", ["전체", "오전", "오후", "저녁/야간"])
        with sc5:
            st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
            search_clicked = st.button("검색하기", type="primary", use_container_width=True)
            
        cc1, cc2 = st.columns([1, 5])
        with cc1:
            st.checkbox("직항 항공편", value=False)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        if search_clicked:
            if not st.session_state.is_logged_in:
                st.warning("🔒 로그인이 필요한 서비스입니다. 먼저 로그인해주세요!")
                st.session_state.step = "login"
                st.rerun()
            else:
                st.session_state.booking_data["departure"] = departure
                st.session_state.booking_data["destination"] = destination
                st.session_state.booking_data["date"] = travel_date
                st.session_state.booking_data["time_slot"] = travel_time
                st.session_state.step = "select_flight"
                st.rerun()

    # 캐러셀 슬라이더 HTML
    carousel_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      .slider-container {
        position: relative;
        width: 100%;
        height: 300px;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
      }
      .slide {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-size: cover;
        background-position: center;
        opacity: 0;
        transition: opacity 1s ease-in-out;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 30px;
        box-sizing: border-box;
      }
      .slide.active { opacity: 1; }
      .slide-content {
        background: rgba(0, 0, 0, 0.5);
        padding: 15px 20px;
        border-radius: 10px;
        backdrop-filter: blur(5px);
        width: fit-content;
      }
      h2 { color: white; margin: 0 0 5px 0; font-size: 1.6rem; font-family: sans-serif; }
      p { color: #e2e8f0; margin: 0; font-size: 0.95rem; font-family: sans-serif; }
    </style>
    </head>
    <body>
    <div class="slider-container">
      <div class="slide active" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1503899036084-c55cdd92da26');">
        <div class="slide-content">
          <h2>🗼 2026 도쿄 여행 트렌드</h2>
          <p>화려한 도시와 맛있는 음식이 기다리는 가까운 여행지</p>
        </div>
      </div>
      <div class="slide" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('
