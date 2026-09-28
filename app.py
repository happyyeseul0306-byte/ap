import streamlit as st
import pandas as pd

st.set_page_config(page_title="비행기 티켓 예매", page_icon="✈️", layout="wide")

st.title("✈️ 간편 비행기 티켓 예매 서비스")
st.markdown("원하는 출발지와 도착지를 선택하고 항공권을 검색해 보세요!")

# 사이드바 - 검색 필터
st.sidebar.header("검색 필터")
departure = st.sidebar.selectbox("출발지", ["서울/인천 (ICN)", "부산/김해 (PUS)", "제주 (CJU)"])
arrival = st.sidebar.selectbox("도착지", ["도쿄/나리타 (NRT)", "방콕 (BKK)", "파리 (CDG)", "뉴욕 (JFK)"])
date = st.sidebar.date_input("출발 일자")

# 가상의 항공권 데이터 (실제 서비스에서는 API나 DB와 연동)
data = {
    "항공사": ["대한항공", "아시아나", "제주항공", "진에어"],
    "출발 시간": ["08:00", "11:30", "14:20", "19:00"],
    "도착 시간": ["10:30", "14:00", "17:00", "22:00"],
    "가격 (원)": [350000, 320000, 180000, 195000]
}
df = pd.DataFrame(data)

st.subheader(f"🔍 {departure} ➔ {arrival} 검색 결과 ({date})")
st.dataframe(df, use_container_width=True)

# 예매하기 섹션
st.divider()
st.subheader("🎫 티켓 예매하기")
selected_airline = st.selectbox("탑승할 항공사를 선택하세요", df["항공사"])
passenger_name = st.text_input("탑승객 성함")

if st.button("예매 완료"):
    if passenger_name:
        st.success(f"🎉 {passenger_name}님, {selected_airline} 항공권 예매가 완료되었습니다!")
        st.balloons()
    else:
        st.warning("탑승객 성함을 입력해주세요.")
