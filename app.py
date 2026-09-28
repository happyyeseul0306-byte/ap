import streamlit as st
import pandas as pd
from datetime import date

# 1. 페이지 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="SkyScanner - 항공권 예매", 
    page_icon="✈️", 
    layout="wide"
)

# 2. 커스텀 CSS 스타일링
st.markdown("""
    <style>
    /* 전체 앱 배경색 */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* 상단 네비게이션바 스타일 */
    .nav-bar {
        background-color: #0b132b;
        padding: 15px 30px;
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        border-radius: 8px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
    }
    
    /* 검색 영역 박스 */
    .search-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #e5e7eb;
    }
    
    /* 항공편 카드 스타일 */
    .flight-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 12px;
        border: 1px solid #e5e7eb;
        transition: transform 0.2s;
    }
    .flight-card:hover {
        border-color: #0066ff;
        box-shadow: 0 4px 12px rgba(0,102,255,0.1);
    }
    
    /* E-티켓 영수증 바우처 */
    .eticket-box {
        background: #ffffff;
        border: 2px solid #0b132b;
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }
    </style>
""", unsafe_allow_html=True)

# 상단 브랜드 네비게이션바
st.markdown('<div class="nav-bar">✈️ SkyFlight 어그리게이터</div>', unsafe_allow_html=True)

# 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = "home"
if "booking_data" not in st.session_state:
    st.session_state.booking_data = {}

# ==========================================
# 1. 홈 화면 (공항/비행기 배경 이미지 적용)
# ==========================================
if st.session_state.step == "home":
    # Unsplash의 고화질 공항/비행기 사진을 배경으로 깔고, 어두운 오버레이를 얹어 텍스트 가독성을 높였습니다.
    st.markdown("""
        <div style="
            background-image: linear-gradient(rgba(11, 19, 43, 0.65), rgba(11, 19, 43, 0.65)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05');
            background-size: cover;
            background-position: center;
            padding: 90px 30px;
            border-radius: 16px;
            color: white;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        ">
            <h1 style="margin-bottom: 15px; font-size: 2.5rem; font-weight: 800; color: white;">수백만 개의 저가 항공권, 검색 한 번으로 간단하게.</h1>
            <p style="color: #e2e8f0; font-size: 1.2rem; margin-bottom: 0;">전 세계 최저가 항공편을 실시간으로 비교하고 예매하세요.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("🚀 항공권 검색 및 예매 시작하기", type="primary", use_container_width=True):
            st.session_state.step = "search"
            st.rerun()

# ==========================================
# 2. 검색 화면 (전문 검색 필터)
# ==========================================
elif st.session_state.step == "search":
    if st.button("⬅️ 메인으로"):
        st.session_state.step = "home"
        st.rerun()
        
    st.markdown("### 🔍 맞춤 항공권 검색")
    
    with st.container():
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            departure = st.selectbox("🛫 출발지", ["서울/인천 (ICN)", "부산/김해 (PUS)", "제주 (CJU)"])
        with col2:
            destination = st.selectbox("🛬 도착지", ["도쿄/나리타 (NRT)", "방콕 (BKK)", "파리 (CDG)", "뉴욕 (JFK)"])
            
        col3, col4 = st.columns(2)
        with col3:
            travel_date = st.date_input("📅 가는 날", min_value=date.today())
        with col4:
            travel_time = st.selectbox("⏰ 희망 시간대", ["전체 시간대", "오전 (00:00 ~ 11:59)", "오후 (12:00 ~ 17:59)", "저녁/야간 (18:00 ~ 23:59)"])
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("검색하기", type="primary", use_container_width=True):
            st.session_state.booking_data["departure"] = departure
            st.session_state.booking_data["destination"] = destination
            st.session_state.booking_data["date"] = travel_date
            st.session_state.booking_data["time_slot"] = travel_time
            
            st.session_state.step = "select_flight"
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 3. 비행기 목록 선택 화면
# ==========================================
elif st.session_state.step == "select_flight":
    if st.button("⬅️ 검색 조건 변경"):
        st.session_state.step = "search"
        st.rerun()
        
    b_data = st.session_state.booking_data
    st.markdown(f"### ✈️ {b_data['departure']} ➔ {b_data['destination']} 검색 결과")
    st.caption(f"선택일자: {b_data['date']} | 조건에 맞는 항공편을 확인하세요.")
    st.markdown("---")
    
    flights = [
        {"id": 1, "airline": "대한항공", "flight_no": "KE123", "dep_time": "08:30", "arr_time": "11:00", "price": 380000, "seat": "일반석"},
        {"id": 2, "airline": "아시아나항공", "flight_no": "OZ456", "dep_time": "12:15", "arr_time": "14:45", "price": 350000, "seat": "일반석"},
        {"id": 3, "airline": "제주항공", "flight_no": "7C789", "dep_time": "15:40", "arr_time": "18:10", "price": 210000, "seat": "특가석"},
        {"id": 4, "airline": "진에어", "flight_no": "LJ302", "dep_time": "20:00", "arr_time": "22:30", "price": 190000, "seat": "일반석"},
    ]
    
    for f in flights:
        st.markdown(f"""
            <div class="flight-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin:0; color:#0b132b;">{f['airline']} <span style="font-size:0.8rem; color:#6b7270;">({f['flight_no']})</span></h4>
                        <p style="margin: 5px 0 0 0; color: #4b5563;">출발 <b>{f['dep_time']}</b> ➔ 도착 <b>{f['arr_time']}</b> &nbsp;|&nbsp; 좌석: {f['seat']}</p>
                    </div>
                    <div style="text-align: right;">
                        <h3 style="margin:0; color:#0066ff;">{f['price']:,}원</h3>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"선택하기 ({f['airline']})", key=f"sel_{f['id']}"):
            st.session_state.booking_data["airline"] = f["airline"]
            st.session_state.booking_data["flight_no"] = f["flight_no"]
            st.session_state.booking_data["dep_time"] = f["dep_time"]
            st.session_state.booking_data["arr_time"] = f["arr_time"]
            st.session_state.booking_data["price"] = f["price"]
            
            st.session_state.step = "passenger_info"
            st.rerun()

# ==========================================
# 4. 승객 정보 입력 화면
# ==========================================
elif st.session_state.step == "passenger_info":
    if st.button("⬅️ 항공편 다시 선택"):
        st.session_state.step = "select_flight"
        st.rerun()
        
    st.markdown("### 👤 탑승객 정보 입력")
    st.info("여권 또는 신분증에 기재된 정보와 일치해야 합니다.")
    
    with st.form("info_form"):
        name = st.text_input("탑승객 성함 (예: 홍길동)")
        birthdate = st.date_input("생년월일", min_value=date(1920, 1, 1), max_value=date.today())
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("✅ 결제 및 예매 확정", type="primary")
        
        if submitted:
            if name:
                st.session_state.booking_data["name"] = name
                st.session_state.booking_data["birthdate"] = birthdate
                st.session_state.step = "success"
                st.rerun()
            else:
                st.warning("성함을 올바르게 입력해주세요.")

# ==========================================
# 5. 예매 완료 화면 (E-Ticket 바우처)
# ==========================================
elif st.session_state.step == "success":
    st.balloons()
    
    st.markdown("""
        <div style="text-align: center; margin-bottom: 25px;">
            <h2 style="color: #0b132b;">🎉 항공권 예매가 완료되었습니다!</h2>
            <p style="color: #6b7270;">아래 전자 항공권(E-Ticket) 정보를 확인 및 보관하세요.</p>
        </div>
    """, unsafe_allow_html=True)
    
    b = st.session_state.booking_data
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
            <div class="eticket-box">
                <h3 style="text-align: center; color: #0b132b; margin-top: 0; border-bottom: 2px solid #0b132b; padding-bottom: 12px;">
                    🎫 E-PASSENGER TICKET
                </h3>
                <p><b>[탑승객]</b> {b.get('name')} ({b.get('birthdate')})</p>
                <hr style="border: 0; border-top: 1px solid #e5e7eb;">
                <p><b>[여정]</b> {b.get('departure')} ➔ {b.get('destination')}</p>
                <p><b>[항공편]</b> {b.get('airline')} ({b.get('flight_no')})</p>
                <p><b>[일시]</b> {b.get('date')} | {b.get('dep_time')} 출발</p>
                <hr style="border: 0; border-top: 1px solid #e5e7eb;">
                <p style="text-align: right; font-size: 1.25rem; color: #0066ff; margin-bottom:0;">
                    <b>총 결제금액: {b.get('price', 0):,}원</b>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🏠 처음으로 돌아가기", use_container_width=True):
            st.session_state.booking_data = {}
            st.session_state.step = "home"
            st.rerun()
