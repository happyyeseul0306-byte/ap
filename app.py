import streamlit as st
import streamlit.components.v1 as components
from datetime import date

# 1. 페이지 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="SkyScanner - 항공권 예매", 
    page_icon="✈️", 
    layout="wide"
)

# 2. 스카이스캐너 스타일 및 CSS
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
    .eticket-box, .login-box {
        background: #ffffff;
        color: #05132d;
        border: 2px solid #05132d;
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
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

# ==========================================
# 1. 홈 화면 (상단 네비게이션바에 로그인 버튼 포함)
# ==========================================
if st.session_state.step == "home":
    # 상단 네비게이션바 구성 (로고, 부제목, 로그인/마이페이지 버튼)
    nav_col1, nav_col2, nav_col3 = st.columns([2, 5, 1])
    with nav_col1:
        st.markdown("<h2 style='color: white; margin: 0; font-size: 1.5rem;'>✈️ Skyscanner</h2>", unsafe_allow_html=True)
    with nav_col2:
        st.markdown("<p style='color: #94a3b8; margin: 5px 0 0 0;'>전 세계 항공권 비교</p>", unsafe_allow_html=True)
    with nav_col3:
        if st.session_state.is_logged_in:
            if st.button(f"👤 {st.session_state.user_email[:6]}님", use_container_width=True):
                st.success("이미 로그인되어 있습니다!")
        else:
            if st.button("🔐 로그인", type="secondary", use_container_width=True):
                st.session_state.step = "login"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white; text-align: center; font-size: 2.2rem; margin-bottom: 5px;'>수백만 개의 저가 항공권, 검색 한 번으로 간단하게.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; text-align: center; margin-bottom: 25px;'>원하는 일정의 항공편을 실시간으로 비교하고 예매하세요.</p>", unsafe_allow_html=True)
    
    # 🌟 스카이스캐너 스타일의 가로형 검색 바
    with st.container():
        st.markdown('<div class="search-box-wrapper">', unsafe_allow_html=True)
        
        sc1, sc2, sc3, sc4, sc5 = st.columns([1.2, 1.2, 1.2, 1.2, 1])
        
        with sc1:
            departure = st.selectbox("🛫 출발지", ["서울/인천 (ICN)", "부산/김해 (PUS)", "제주 (CJU)"])
        with sc2:
            destination = st.selectbox("🛬 도착지", ["도쿄/나리타 (NRT)", "방콕 (BKK)", "파리 (CDG)", "뉴욕 (JFK)"])
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
            st.session_state.booking_data["departure"] = departure
            st.session_state.booking_data["destination"] = destination
            st.session_state.booking_data["date"] = travel_date
            st.session_state.booking_data["time_slot"] = travel_time
            st.session_state.step = "select_flight"
            st.rerun()

    # 🌟 자동 전환되는 여행지 사진 배너 (캐러셀)
    carousel_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      .slider-container {
        position: relative;
        width: 100%;
        height: 320px;
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
        padding: 40px;
        box-sizing: border-box;
      }
      .slide.active {
        opacity: 1;
      }
      .slide-content {
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
        backdrop-filter: blur(5px);
        width: fit-content;
      }
      h2 { color: white; margin: 0 0 10px 0; font-size: 1.8rem; font-family: sans-serif; }
      p { color: #e2e8f0; margin: 0; font-size: 1rem; font-family: sans-serif; }
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
      <div class="slide" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1508009603885-50cf7c579365');">
        <div class="slide-content">
          <h2>🏝️ 낭만의 방콕 휴가</h2>
          <p>이국적인 사원과 야시장, 가성비 최고의 휴양 도시</p>
        </div>
      </div>
      <div class="slide" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34');">
        <div class="slide-content">
          <h2>🥐 예술의 도시 파리</h2>
          <p>낭만적인 에펠탑과 세계적인 명화가 숨쉬는 곳</p>
        </div>
      </div>
    </div>
    <script>
      let currentSlide = 0;
      const slides = document.querySelectorAll('.slide');
      function nextSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
      }
      setInterval(nextSlide, 3500);
    </script>
    </body>
    </html>
    """
    components.html(carousel_html, height=350)

# ==========================================
# 1-2. 로그인 화면
# ==========================================
elif st.session_state.step == "login":
    if st.button("⬅️ 홈으로 돌아가기"):
        st.session_state.step = "home"
        st.rerun()
        
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <h2 style="color: white;">🔐 Skyscanner 로그인</h2>
                <p style="color: #94a3b8;">로그인하고 더 많은 맞춤 혜택을 받아보세요.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            email_input = st.text_input("이메일 주소")
            password_input = st.text_input("비밀번호", type="password")
            
            st.markdown("<br>", unsafe_allow_html=True)
            login_submitted = st.form_submit_button("로그인하기", type="primary", use_container_width=True)
            
            if login_submitted:
                if email_input and password_input:
                    st.session_state.is_logged_in = True
                    st.session_state.user_email = email_input
                    st.success("로그인 성공! 홈으로 이동합니다.")
                    st.session_state.step = "home"
                    st.rerun()
                else:
                    st.warning("이메일과 비밀번호를 모두 입력해주세요.")

# ==========================================
# 2. 비행기 목록 선택 화면
# ==========================================
elif st.session_state.step == "select_flight":
    if st.button("⬅️ 검색 조건 변경"):
        st.session_state.step = "search"
        st.rerun()
        
    b_data = st.session_state.booking_data
    st.markdown(f"<h2 style='color: white;'>✈️ {b_data['departure']} ➔ {b_data['destination']} 검색 결과</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #94a3b8;'>선택일자: {b_data['date']} | 마음에 드는 항공편을 선택하세요.</p>", unsafe_allow_html=True)
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
                        <h3 style="margin:0; color:#05132d;">{f['airline']} <span style="font-size:0.8rem; color:#6b7270;">({f['flight_no']})</span></h3>
                        <p style="margin: 5px 0 0 0; color: #4b5563;">출발 <b>{f['dep_time']}</b> ➔ 도착 <b>{f['arr_time']}</b> &nbsp;|&nbsp; 좌석: {f['seat']}</p>
                    </div>
                    <div style="text-align: right;">
                        <h2 style="margin:0; color:#0066ff;">{f['price']:,}원</h2>
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
# 3. 승객 정보 입력 화면
# ==========================================
elif st.session_state.step == "passenger_info":
    if st.button("⬅️ 항공편 다시 선택"):
        st.session_state.step = "select_flight"
        st.rerun()
        
    st.markdown("<h2 style='color: white;'>👤 탑승객 정보 입력</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>여권 또는 신분증에 기재된 정보와 일치해야 합니다.</p>", unsafe_allow_html=True)
    
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
# 4. 예매 완료 화면 (E-Ticket 바우처)
# ==========================================
elif st.session_state.step == "success":
    st.balloons()
    
    st.markdown("""
        <div style="text-align: center; margin-bottom: 25px;">
            <h2 style="color: white;">🎉 항공권 예매가 완료되었습니다!</h2>
            <p style="color: #94a3b8;">아래 전자 항공권(E-Ticket) 정보를 확인하세요.</p>
        </div>
    """, unsafe_allow_html=True)
    
    b = st.session_state.booking_data
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
            <div class="eticket-box">
                <h3 style="text-align: center; color: #05132d; margin-top: 0; border-bottom: 2px solid #05132d; padding-bottom: 12px;">
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
