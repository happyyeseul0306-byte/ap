import streamlit as st
import pandas as pd
from datetime import date

# 페이지 설정
st.set_page_config(page_title="간편 비행기 티켓 예매", page_icon="✈️", layout="centered")

# 세션 상태 초기화 (페이지 전환 및 데이터 저장을 위해 필요)
if "step" not in st.session_state:
    st.session_state.step = "home"
if "booking_data" not in st.session_state:
    st.session_state.booking_data = {}

# 1. 홈 화면 (예매 시작하기 버튼)
if st.session_state.step == "home":
    st.title("✈️ 간편 비행기 티켓 예매 서비스")
    st.write("원하시는 일정의 항공권을 쉽고 빠르게 예매해 보세요.")
    
    st.markdown("---")
    
    # 중앙 정렬 느낌을 주기 위한 빈 공간 또는 마크다운
    if st.button("🚀 예매 시작하기", type="primary", use_container_width=True):
        st.session_state.step = "search"
        st.rerun()

# 2. 검색 화면 (날짜, 시간, 목적지 선택 후 조회)
elif st.session_state.step == "search":
    st.title("🔍 항공편 검색")
    
    if st.button("⬅️ 처음으로"):
        st.session_state.step = "home"
        st.rerun()
        
    st.markdown("---")
    
    # 검색 조건 입력
    col1, col2 = st.columns(2)
    with col1:
        departure = st.selectbox("출발지", ["서울/인천 (ICN)", "부산/김해 (PUS)", "제주 (CJU)"])
    with col2:
        destination = st.selectbox("도착지", ["도쿄/나리타 (NRT)", "방콕 (BKK)", "파리 (CDG)", "뉴욕 (JFK)"])
        
    col3, col4 = st.columns(2)
    with col3:
        travel_date = st.date_input("출발 연/월/일", min_value=date.today())
    with col4:
        travel_time = st.selectbox("희망 시간대", ["오전 (00:00 ~ 11:59)", "오후 (12:00 ~ 17:59)", "저녁/야간 (18:00 ~ 23:59)"])
        
    if st.button("🔍 항공편 조회하기", type="primary", use_container_width=True):
        # 선택한 정보를 세션에 저장
        st.session_state.booking_data["departure"] = departure
        st.session_state.booking_data["destination"] = destination
        st.session_state.booking_data["date"] = travel_date
        st.session_state.booking_data["time_slot"] = travel_time
        
        st.session_state.step = "select_flight"
        st.rerun()

# 3. 비행기 목록 선택 화면
elif st.session_state.step == "select_flight":
    st.title("🛫 항공편 선택")
    
    if st.button("⬅️ 검색 조건 다시 설정"):
        st.session_state.step = "search"
        st.rerun()
        
    b_data = st.session_state.booking_data
    st.info(f"선택 조건: {b_data['departure']} ➔ {b_data['destination']} ({b_data['date']})")
    
    st.write("원하시는 항공편을 선택해 주세요.")
    
    # 가상의 항공편 리스트 데이터 (시간대별 맞춤)
    flights = [
        {"id": 1, "airline": "대한항공", "flight_no": "KE123", "dep_time": "08:30", "arr_time": "11:00", "price": 380000},
        {"id": 2, "airline": "아시아나항공", "flight_no": "OZ456", "dep_time": "12:15", "arr_time": "14:45", "price": 350000},
        {"id": 3, "airline": "제주항공", "flight_no": "7C789", "dep_time": "15:40", "arr_time": "18:10", "price": 210000},
        {"id": 4, "airline": "진에어", "flight_no": "LJ302", "dep_time": "20:00", "arr_time": "22:30", "price": 190000},
    ]
    
    # 리스트를 반복문으로 예쁘게 표시
    for f in flights:
        with st.container(border=True):
            cols = st.columns([3, 2, 2])
            with cols[0]:
                st.markdown(f"### {f['airline']}")
                st.caption(f"편명: {f['flight_no']}")
            with cols[1]:
                st.write(f"⏱️ **출발:** {f['dep_time']}")
                st.write(f"⏱️ **도착:** {f['arr_time']}")
            with cols[2]:
                st.markdown(f"#### {f['price']:,}원")
                if st.button("선택하기", key=f"select_{f['id']}"):
                    st.session_state.booking_data["airline"] = f["airline"]
                    st.session_state.booking_data["flight_no"] = f["flight_no"]
                    st.session_state.booking_data["dep_time"] = f["dep_time"]
                    st.session_state.booking_data["arr_time"] = f["arr_time"]
                    st.session_state.booking_data["price"] = f["price"]
                    
                    st.session_state.step = "passenger_info"
                    st.rerun()

# 4. 승객 정보 입력 화면
elif st.session_state.step == "passenger_info":
    st.title("👤 탑승객 정보 입력")
    
    if st.button("⬅️ 항공편 다시 선택"):
        st.session_state.step = "select_flight"
        st.rerun()
        
    st.markdown("---")
    
    name = st.text_input("탑승객 성함")
    birthdate = st.date_input("생년월일", min_value=date(1920, 1, 1), max_value=date.today())
    
    if st.button("✅ 예매 확인 및 완료", type="primary"):
        if name:
            st.session_state.booking_data["name"] = name
            st.session_state.booking_data["birthdate"] = birthdate
            
            st.session_state.step = "success"
            st.rerun()
        else:
            st.warning("탑승객 성함을 정확히 입력해주세요.")

# 5. 예매 완료 화면
elif st.session_state.step == "success":
    st.balloons()
    st.title("🎉 예매 성공!")
    st.success("항공권 예매가 성공적으로 완료되었습니다. 아래 예매 내역을 확인해 주세요.")
    
    b = st.session_state.booking_data
    
    with st.container(border=True):
        st.markdown("### 🎫 전자 항공권 (E-Ticket) 내역")
        st.markdown(f"- **탑승객 성함:** {b.get('name')} (생년월일: {b.get('birthdate')})")
        st.markdown(f"- **이용 항공사:** {b.get('airline')} ({b.get('flight_no')})")
        st.markdown(f"- **노선:** {b.get('departure')} ➔ {b.get('destination')}")
        st.markdown(f"- **출발 날짜 및 시간:** {b.get('date')} / {b.get('dep_time')} 출발")
        st.markdown(f"- **결제 금액:** {b.get('price', 0):,}원")
        
    if st.button("🏠 처음으로 돌아가기"):
        # 데이터 초기화 후 홈으로
        st.session_state.booking_state = {}
        st.session_state.step = "home"
        st.rerun()
