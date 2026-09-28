import streamlit as st
from datetime import date

# 1. 페이지 설정 (넓은 레이아웃 사용)
st.set_page_config(
    page_title="SkyAir - 항공권 예매 시스템", 
    page_icon="✈️", 
    layout="wide"
)

# 2. 실제 항공사 앱 같은 모던하고 깔끔한 UI를 위한 커스텀 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경 톤 조정 */
    .stApp {
        background-color: #f4f6f9;
    }
    
    /* 상단 배너 스타일 */
    .hero-box {
        background: linear-gradient(135deg, #0b2545 0%, #134074 100%);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* 카드 디자인 */
    .flight-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-left: 5px solid #134074;
    }
    
    /* E-Ticket 영수증 스타일 */
    .eticket-box {
        background-color: #ffffff;
        border: 2px dashed #134074;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    </style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = "home"
if "booking_data" not in st.session_state:
    st.session_state.booking_data = {}

# ==========================================
# 1. 홈 화면 (항공사 메인 페이지 느낌)
# ==========================================
if st.session_state.step == "home":
    st.markdown("""
        <div class="hero-box">
            <h1>✈️ SkyAir 프리미엄 항공 예매</h1>
            <p>안전하고 편안한 비행을 위한 가장 빠른 선택</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 실시간 항공권 예매 시작하기", type="primary", use_container_width=True):
            st.session_state.step = "search"
            st.rerun()

# ==========================================
# 2. 검색 화면 (출발지, 도착지, 날짜, 시간대)
# ==========================================
elif st.session_state.step == "search":
    st.markdown("### 🔍 항공편 검색")
    
    if st.button("⬅️ 홈으로 가기"):
        st.session_state.step = "home"
        st.rerun()
        
    with st.container():
        st.markdown("##### 여정 정보를 입력해 주세요")
        col1, col2 = st.columns(2)
        with col1:
            departure = st.selectbox("🛫 출발지", ["서울/인천 (ICN)", "부산/김해 (PUS)", "제주 (CJU)"])
        with col2:
            destination = st.selectbox("🛬 도착지", ["도쿄/나리타 (NRT)", "방콕 (BKK)", "파리 (CDG)", "뉴욕 (JFK)"])
            
        col3, col4 = st.columns(2)
        with col3:
            travel_date = st.date_input("📅 출발 날짜 (년/월/일)", min_value=date.today())
        with col4:
            travel_time = st.selectbox("⏰ 선호 시간대", ["전체 시간", "오전 (00:00 ~ 11:59)", "오후 (12:00 ~ 17:59)", "저녁/야간 (18:00 ~ 23:59)"])
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 맞춤 항공편 조회", type="primary", use_container_width=True):
            st.session_state.booking_data["departure"] = departure
            st.session_state.booking_data["destination"] = destination
            st.session_state.booking_data["date"] = travel_date
            st.session_state.booking_data["time_slot"] = travel_time
            
            st.session_state.step = "select_flight"
            st.rerun()

# ==========================================
# 3. 비행기 목록 선택 화면
# ==========================================
elif st.session_state.step == "select_flight":
    st.markdown("### 🛫 항공편 리스트 선택")
    
    if st.button("⬅️ 검색 조건 변경"):
        st.session_state.step = "search"
        st.rerun()
        
    b_data = st.session_state.booking_data
    st.info(f"📍 검색 경로: **{b_data['departure']} ➔ {b_data['destination']}** ({b_data['date']})")
    
    # 실제 항공사 리스트 데이터
    flights = [
        {"id": 1, "airline": "대한항공 (Korean Air)", "flight_no": "KE001", "dep_time": "09:00", "arr_time": "11:30", "price": 420000, "class": "일반석 (Economy)"},
        {"id": 2, "airline": "아시아나항공 (Asiana Airlines)", "flight_no": "OZ102", "dep_time": "13:30", "arr_time": "16:00", "price": 390000, "class": "일반석 (Economy)"},
        {"id": 3, "airline": "제주항공 (Jeju Air)", "flight_no": "7C504", "dep_time": "16:40", "arr_time": "19:10", "price": 230000, "class": "특가석 (Promo)"},
        {"id": 4, "airline": "진에어 (Jin Air)", "flight_no": "LJ208", "dep_time": "20:10", "arr_time": "22:45", "price": 210000, "class": "일반석 (Economy)"},
    ]
    
    for f in flights:
        with st.container():
            st.markdown(f"""
                <div class="flight-card">
                    <h4>🏢 {f['airline']} <span style="font-size:0.8em; color:gray;">({f['flight_no']})</span></h4>
                    <p style="margin: 5px 0;"><b>출발:</b> {f['dep_time']} &nbsp;|&nbsp; <b>도착:</b> {f['arr_time']} &nbsp;|&nbsp; <b>좌석 등급:</b> {f['class']}</p>
                    <h3 style="color: #0b2545; text-align: right; margin: 0;">{f['price']:,}원</h3>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"선택하기 ({f['airline']})", key=f"sel_{f['id']}"):
                st.session_state.booking_data["airline"] = f["airline"]
                st.session_state.booking_data["flight_no"] = f["flight_no"]
                st.session_state.booking_data["dep_time"] = f["dep_time"]
                st.session_state.booking_data["arr_time"] = f["arr_time"]
                st.session_state.booking_data["price"] = f["price"]
                st.session_state.booking_data["class"] = f["class"]
                
                st.session_state.step = "passenger_info"
                st.rerun()

# ==========================================
# 4. 승객 정보 입력 화면
# ==========================================
elif st.session_state.step == "passenger_info":
    st.markdown("### 👤 탑승객 정보 입력")
    
    if st.button("⬅️ 항공편 다시 고르기"):
        st.session_state.step = "select_flight"
        st.rerun()
        
    with st.form("passenger_form"):
        st.markdown("##### 여권 상의 영문 이름 또는 국문 이름을 정확히 입력해 주세요.")
        name = st.text_input("탑승객 성함 (예: 홍길동 / HONG GILDONG)")
        birthdate = st.date_input("생년월일", min_value=date(1920, 1, 1), max_value=date.today())
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("✅ 결제 및 예매 완료", type="primary")
        
        if submitted:
            if name:
                st.session_state.booking_data["name"] = name
                st.session_state.booking_data["birthdate"] = birthdate
                st.session_state.step = "success"
                st.rerun()
            else:
                st.warning("탑승객 성함을 입력해 주세요.")

# ==========================================
# 5. 예매 완료 화면 (E-Ticket 바우처 스타일)
# ==========================================
elif st.session_state.step == "success":
    st.balloons()
    
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #134074;">🎉 예매가 성공적으로 완료되었습니다!</h1>
            <p>발급된 전자 항공권(E-Ticket) 정보를 확인하세요.</p>
        </div>
    """, unsafe_allow_html=True)
    
    b = st.session_state.booking_data
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
            <div class="eticket-box">
                <h2 style="text-align: center; color: #0b2545; border-bottom: 2px solid #0b2545; padding-bottom: 10px;">✈️ SKYAIR E-TICKET</h2>
                <p><b>[탑승객 정보]</b><br>
                - 성함: {b.get('name')}<br>
                - 생년월일: {b.get('birthdate')}</p>
                <hr>
                <p><b>[항공편 정보]</b><br>
                - 이용 항공사: {b.get('airline')}<br>
                - 편명: {b.get('flight_no')} ({b.get('class')})<br>
                - 노선: {b.get('departure')} ➔ {b.get('destination')}<br>
                - 출발 일자: {b.get('date')}<br>
                - 운항 시간: {b.get('dep_time')} 출발 ~ {b.get('arr_time')} 도착</p>
                <hr>
                <p style="text-align: right; font-size: 1.2em;"><b>총 결제금액: {b.get('price', 0):,}원</b></p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🏠 메인 화면으로 돌아가기", use_container_width=True):
            st.session_state.booking_data = {}
            st.session_state.step = "home"
            st.rerun()
