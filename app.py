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
    .img-card {
        background-color: #ffffff;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        text-align: center;
        margin-bottom: 20px;
    }
    .img-card p {
        color: #05132d;
        font-weight: bold;
        padding: 8px 0;
        margin: 0;
        font-size: 0.95rem;
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
        st.markdown(
            "<h2 style='color: white; margin: 0; font-size: 1.5rem;'>🚀 StarPort</h2>",
            unsafe_allow_html=True,
        )
    with nav_col2:
        st.markdown(
            "<p style='color: #94a3b8; margin: 5px 0 0 0;'>전 세계 항공권 비교 및 여행지 가이드</p>",
            unsafe_allow_html=True,
        )
    with nav_col3:
        pass
    with nav_col4:
        if st.session_state.is_logged_in:
            if st.button(
                f"👤 {st.session_state.user_email[:4]}...",
                type="secondary",
                use_container_width=True,
            ):
                st.info(f"현재 접속 계정: {st.session_state.user_email}")
        else:
            if st.button(
                "👤 로그인", type="secondary", use_container_width=True
            ):
                st.session_state.step = "login"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<h1 style='color: white; text-align: center; font-size: 2.2rem; margin-bottom: 5px;'>수백만 개의 항공권, 검색 한 번으로 간단하게.</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #94a3b8; text-align: center; margin-bottom: 25px;'>원하는 일정의 항공편을 실시간으로 비교하고 예매하세요.</p>",
        unsafe_allow_html=True,
    )

    # 🌍 대폭 강화된 인기 해외 국가/도시 목록
    destinations_list = [
        # 일본 (인기 도시)
        "도쿄/나리타 (NRT) - 일본",
        "도쿄/하네다 (HND) - 일본",
        "오사카/간사이 (KIX) - 일본",
        "후쿠오카 (FUK) - 일본",
        "삿포로/신치토세 (CTS) - 일본",
        "오키나와 (OKA) - 일본",
        "나고야 (NGO) - 일본",
        "시즈오카 (FSZ) - 일본",
        # 동남아시아 (인기 휴양지 및 대도시)
        "방콕/수완나품 (BKK) - 태국",
        "치앙마이 (CNX) - 태국",
        "푸켓 (HKT) - 태국",
        "다낭 (DAD) - 베트남",
        "나트랑/캄란 (CXR) - 베트남",
        "호치민 (SGN) - 베트남",
        "하노이 (HAN) - 베트남",
        "푸꾸옥 (PQC) - 베트남",
        "싱가포르 (SIN) - 싱가포르",
        "쿠알라룸푸르 (KUL) - 말레이시아",
        "코타키나발루 (BKI) - 말레이시아",
        "세부 (CEB) - 필리핀",
        "보홀 (TAG) - 필리핀",
        "마닐라 (MNL) - 필리핀",
        "발리/덴파사르 (DPS) - 인도네시아",
        # 동북아 / 중화권 / 중앙아
        "홍콩 (HKG) - 홍콩",
        "마카오 (MFM) - 마카오",
        "타이베이/타오위안 (TPE) - 대만",
        "가오슝 (KHH) - 대만",
        "베이징/서두 (PEK) - 중국",
        "상하이/푸동 (PVG) - 중국",
        "울란바토르 (ULN) - 몽골",
        # 유럽 (주요 명소 국가)
        "파리/샤를드골 (CDG) - 프랑스",
        "런던/히드로 (LHR) - 영국",
        "로마/피우미치노 (FCO) - 이탈리아",
        "바르셀로나 (BCN) - 스페인",
        "프랑크푸르트 (FRA) - 독일",
        "스위스/취리히 (ZRH) - 스위스",
        "체코/프라하 (PRG) - 체코",
        "오스트리아/빈 (VIE) - 오스트리아",
        "튀르키예/이스탄불 (IST) - 튀르키예",
        "네덜란드/암스테르담 (AMS) - 네덜란드",
        # 미주, 대양주, 중동
        "뉴욕/JFK (JFK) - 미국",
        "로스앤젤레스 (LAX) - 미국",
        "샌프란시스코 (SFO) - 미국",
        "하와이/호놀룰루 (HNL) - 미국",
        "밴쿠버 (YVR) - 캐나다",
        "토론토 (YYZ) - 캐나다",
        "시드니 (SYD) - 호주",
        "멜버른 (MEL) - 호주",
        "괌 (GUM) - 괌",
        "두바이 (DXB) - 아랍에미리트",
    ]

    departure_list = [
        "서울/인천 (ICN)",
        "서울/김포 (GMP)",
        "부산/김해 (PUS)",
        "제주 (CJU)",
        "청주 (CJJ)",
        "대구 (TAE)",
        "무안 (MWX)",
    ]

    with st.container():
        st.markdown(
            '<div class="search-box-wrapper">', unsafe_allow_html=True
        )

        sc1, sc2, sc3, sc4, sc5 = st.columns([1.2, 1.5, 1.1, 1.1, 0.9])

        with sc1:
            departure = st.selectbox("🛫 출발지", departure_list)
        with sc2:
            destination = st.selectbox("🛬 도착지", destinations_list)
        with sc3:
            travel_date = st.date_input("📅 가는 날", min_value=date.today())
        with sc4:
            travel_time_range = st.slider(
                "⏰ 출발 시간대",
                value=(time(0, 0), time(23, 59)),
                format="HH:mm",
            )
        with sc5:
            st.markdown(
                "<div style='margin-top: 28px;'></div>", unsafe_allow_html=True
            )
            search_clicked = st.button(
                "검색하기", type="primary", use_container_width=True
            )

        cc1, cc2 = st.columns([1, 5])
        with cc1:
            st.checkbox("직항 항공편", value=False)

        st.markdown("</div>", unsafe_allow_html=True)

        if search_clicked:
            if not st.session_state.is_logged_in:
                st.warning("🔒 로그인이 필요한 서비스입니다. 먼저 로그인해주세요!")
                st.session_state.step = "login"
                st.rerun()
            else:
                st.session_state.booking_data["departure"] = departure
                st.session_state.booking_data["destination"] = destination
                st.session_state.booking_data["date"] = travel_date
                st.session_state.booking_data["time_range"] = travel_time_range
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
          <h2>🗼 도쿄 여행 트렌드</h2>
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
    components.html(carousel_html, height=320)

    st.markdown(
        "<p style='text-align: center; color: #94a3b8; margin-top: 15px;'>👇 아래 추천 도시 버튼을 눌러 상세 가이드를 확인해보세요!</p>",
        unsafe_allow_html=True,
    )

    row1_c1, row1_c2, row1_c3 = st.columns(3)
    with row1_c1:
        if st.button("🗼 도쿄 가이드 보기", use_container_width=True):
            st.session_state.selected_destination_info = "도쿄"
            st.session_state.step = "destination_detail"
            st.rerun()
    with row1_c2:
        if st.button("🏝️ 방콕 가이드 보기", use_container_width=True):
            st.session_state.selected_destination_info = "방콕"
            st.session_state.step = "destination_detail"
            st.rerun()
    with row1_c3:
        if st.button("🥐 파리 가이드 보기", use_container_width=True):
            st.session_state.selected_destination_info = "파리"
            st.session_state.step = "destination_detail"
            st.rerun()

    row2_c1, row2_c2, row2_c3 = st.columns(3)
    with row2_c1:
        if st.button("🗽 뉴욕 가이드 보기", use_container_width=True):
            st.session_state.selected_destination_info = "뉴욕"
            st.session_state.step = "destination_detail"
            st.rerun()
    with row2_c2:
        if st.button("🌊 다낭 가이드 보기", use_container_width=True):
            st.session_state.selected_destination_info = "다낭"
            st.session_state.step = "destination_detail"
            st.rerun()
    with row2_c3:
        if st.button("⛰️ 스위스 가이드 보기", use_container_width=True):
            st.session_state.selected_destination_info = "스위스"
            st.session_state.step = "destination_detail"
            st.rerun()

# ==========================================
# 1-1. 여행지 상세 소개 페이지
# ==========================================
elif st.session_state.step == "destination_detail":
    if st.button("⬅️ 홈으로 돌아가기"):
        st.session_state.step = "home"
        st.rerun()

    dest_name = st.session_state.selected_destination_info

    dest_info_dict = {
        "도쿄": {
            "title": "🗼 일본 도쿄 (Tokyo)",
            "sub": "전통과 미래가 공존하는 매력적인 메가폴리스",
            "gallery": [
                {
                    "title": "🌃 도쿄 타워 야경",
                    "url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26",
                },
                {
                    "title": "⛩️ 전통 아사쿠사 센소지",
                    "url": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9",
                },
                {
                    "title": "🍣 정통 에도마에 초밥",
                    "url": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c",
                },
                {
                    "title": "🚶 시부야 스크램블 교차로",
                    "url": "https://images.unsplash.com/photo-1542051841857-5f90071e7989",
                },
            ],
            "desc": "도쿄는 첨단 기술과 오랜 전통문화가 조화를 이루는 세계적인 대도시입니다. 시부야의 스크램블 교차로, 아사쿠사의 센소지 사원, 그리고 미식가들을 사로잡는 다양한 라멘과 스시 전문점이 여행객을 반깁니다.",
            "best_season": "3~5월 (화사한 벚꽃 시즌) 및 9~11월 (선선한 단풍 시즌)",
            "tip": "도쿄 지하철 이용 시 스마트폰에 'Suica' 또는 'Pasmo' 교통카드를 등록하면 편리합니다.",
            "spots": [
                "시부야 스크램블 교차로 & 스카이트리 전망대",
                "도쿄 디즈니랜드 & 디즈니씨",
                "아사쿠사 센소지 (전통 기념품 거리)",
                "신주쿠 교엔 국립공원 & 메이지 신궁",
            ],
            "foods": [
                "츠키지 시장의 참치 초밥 & 장어덮밥",
                "진한 돈골 육수의 미소/돈코츠 라멘",
                "철판 위에서 바로 볶아 먹는 몬쟈야키",
                "퇴근길 골목길의 숯불 야키토리",
            ],
        },
        "방콕": {
            "title": "🏝 태국 방콕 (Bangkok)",
            "sub": "활기찬 야시장과 찬란한 불교 사원의 도시",
            "gallery": [
                {
                    "title": "🛕 왓 아룬 (새벽 사원)",
                    "url": "https://images.unsplash.com/photo-1508009603885-50cf7c579365",
                },
                {
                    "title": "🛍️ 활기찬 로컬 야시장",
                    "url": "https://images.unsplash.com/photo-1563492065599-3520f775eeed",
                },
                {
                    "title": "🍜 로컬 팟타이 요리",
                    "url": "https://images.unsplash.com/photo-1559847844-5315695dadae",
                },
                {
                    "title": "🛶 수상 시장 풍경",
                    "url": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a",
                },
            ],
            "desc": "방콕은 화려한 왕궁과 웅장한 불교 사원, 그리고 전 세계 배낭여행자들의 성지인 활기찬 야시장이 어우러진 휴양지입니다.",
            "best_season": "11월 ~ 2월 (비가 적고 쾌적한 건기)",
            "tip": "사원 방문 시에는 반바지나 민소매 차림이 제한되므로 가벼운 겉옷을 준비하세요.",
            "spots": [
                "짜오프라야 강변의 왓 아룬 (새벽 사원)",
                "방콕 왕궁 & 왓 포 거대 와불상",
                "짜뚜짝 주말 시장 (쇼핑 & 먹거리)",
                "카오산 로드 (세계 여행자들의 밤문화)",
            ],
            "foods": [
                "매콤 새콤한 새우 스프 똠얌꿍",
                "고소한 볶음 쌀국수 팟타이",
                "달콤한 망고 스티키 라이스",
                "부드러운 게살 푸팟퐁 커리",
            ],
        },
        "파리": {
            "title": "🥐 프랑스 파리 (Paris)",
            "sub": "예술, 낭만, 패션이 숨쉬는 영원한 수도",
            "gallery": [
                {
                    "title": "🗼 낭만의 에펠탑 야경",
                    "url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
                },
                {
                    "title": "🏛️ 루브르 박물관 박공",
                    "url": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f",
                },
                {
                    "title": "☕ 노천 카페 노변",
                    "url": "https://images.unsplash.com/photo-1509439581779-6298f75bf6e5",
                },
                {
                    "title": "🧁 프렌치 디저트 마카롱",
                    "url": "https://images.unsplash.com/photo-1569864358642-9d1684040f43",
                },
            ],
            "desc": "센 강이 유유히 흐르는 파리는 고풍스러운 건축물과 세계적인 미술관, 그리고 고소한 빵 냄새가 번지는 카페가 가득한 낭만의 도시입니다.",
            "best_season": "5~6월 (포근한 봄날) 및 9~10월 (낭만적인 가을)",
            "tip": "루브르 박물관이나 에펠탑 등 주요 인기 명소는 사전에 온라인 타임슬롯 예약을 추천합니다.",
            "spots": [
                "에펠탑 & 트로카데로 광장",
                "루브르 박물관 & 오르세 미술관",
                "몽마르트르 언덕 & 사크레쾨르 대성당",
                "샹젤리제 거리 & 웅장한 개선문",
            ],
            "foods": [
                "갓 구운 크루아상 & 바게트",
                "진한 치즈가 올라간 프렌치 어니언 수프",
                "달콤하고 바삭한 색색의 마카롱",
                "스테이크 프릿 (스테이크와 감자튀김)",
            ],
        },
        "뉴욕": {
            "title": "🗽 미국 뉴욕 (New York)",
            "sub": "잠들지 않는 세계 경제와 문화의 메카",
            "gallery": [
                {
                    "title": "🏙️ 타임스 스퀘어 빌딩숲",
                    "url": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9",
                },
                {
                    "title": "🌳 센트럴 파크 전경",
                    "url": "https://images.unsplash.com/photo-1534430480872-3498386e7856",
                },
                {
                    "title": "🌉 브루클린 브릿지",
                    "url": "https://images.unsplash.com/photo-1499092346589-b9b6be3e94b2",
                },
                {
                    "title": "🍕 뉴욕 스트리트 피자",
                    "url": "https://images.unsplash.com/photo-1513104890138-7c749659a591",
                },
            ],
            "desc": "뉴욕은 자유의 여신상, 브루클린 브릿지, 타임스 스퀘어 등 마천루가 빛나는 거대한 도심입니다.",
            "best_season": "9~11월 (센트럴 파크의 형형색색 단풍 시즌)",
            "tip": "식당 이용 시 식사 금액의 15~20% 팁 문화가 적용됩니다.",
            "spots": [
                "타임스 스퀘어 & 브로드웨이 뮤지컬",
                "센트럴 파크 (도심 속 휴식 공간)",
                "자유의 여신상 페리 투어",
                "엠파이어 스테이트 빌딩 전망대",
            ],
            "foods": [
                "큼직한 한 조각 뉴욕 스타일 화덕피자",
                "푸짐한 패스트라미 샌드위치",
                "쫄깃한 뉴욕 베이글 & 크림치즈",
                "정통 아메리칸 드라이에이징 스테이크",
            ],
        },
        "다낭": {
            "title": "🌊 베트남 다낭 (Da Nang)",
            "sub": "에메랄드빛 미케 해변과 휴양 리조트",
            "gallery": [
                {
                    "title": "🏖️ 에메랄드빛 미케 비치",
                    "url": "https://images.unsplash.com/photo-1559592413-7cec4d0cae2b",
                },
                {
                    "title": "🏮 호이안 올드타운 야경",
                    "url": "https://images.unsplash.com/photo-1528127269322-539801943592",
                },
                {
                    "title": "🌉 바나힐 골든 브릿지",
                    "url": "https://images.unsplash.com/photo-1570339322846-6f387181585f",
                },
                {
                    "title": "🍜 정통 베트남 쌀국수",
                    "url": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43",
                },
            ],
            "desc": "다낭은 끝없이 펼쳐진 미케 해변과 유네스코 세계유산인 호이안 구시가지가 근처에 있어 휴양과 관광을 함께 즐기기에 좋습니다.",
            "best_season": "2월 ~ 8월 (파도가 잔잔하고 맑은 건기)",
            "tip": "이동 시에는 차량 호출 서비스인 Grab을 사용하세요.",
            "spots": [
                "미케 비치 (세계적인 해변)",
                "바나힐 테마파크 & 손모양 골든 브릿지",
                "호이안 올드타운 (야경 명소)",
                "오행산 (마블 마운틴)",
            ],
            "foods": [
                "진한 소고기 육수의 베트남 쌀국수",
                "바삭한 부침개 반쎄오",
                "숯불에 구운 돼지고기 노점 분짜",
                "싱싱하고 저렴한 해산물 요리",
            ],
        },
        "스위스": {
            "title": "⛰️ 스위스 취리히 / 인터라켄 (Switzerland)",
            "sub": "알프스 대자연과 만년설의 동화 마을",
            "gallery": [
                {
                    "title": "🏔️ 알프스 융프라우요흐",
                    "url": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99",
                },
                {
                    "title": "🚂 산악 열차 풍경",
                    "url": "https://images.unsplash.com/photo-1502784444187-359ac186c5bb",
                },
                {
                    "title": "🧀 스위스 치즈 퐁듀",
                    "url": "https://images.unsplash.com/photo-1541529086526-db283c563270",
                },
                {
                    "title": "🪵 체르마트 마테호른 마을",
                    "url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
                },
            ],
            "desc": "스위스는 융프라우와 만년설, 에메랄드빛 청정 호수가 어우러진 알프스의 낙원입니다.",
            "best_season": "6~8월 (하이킹) 또는 12~2월 (겨울 설경)",
            "tip": "스위스 트래블 패스를 미리 준비하면 이동 시 매우 경제적입니다.",
            "spots": [
                "융프라우요흐 (유럽의 지붕)",
                "인터라켄 하더 쿨룸 전망대",
                "루체른 카펠교 & 호수 산책로",
                "체르마트 마테호른 봉우리",
            ],
            "foods": [
                "고소하고 따뜻한 치즈 퐁듀",
                "치즈를 얹은 라클렛",
                "스위스 전통 감자전 뢰스티",
                "프리미엄 스위스 초콜릿",
            ],
        },
    }

    info = dest_info_dict.get(dest_name, dest_info_dict["도쿄"])

    st.markdown(
        f"<h1 style='color: white; margin-bottom: 5px;'>{info['title']}</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='color: #94a3b8; font-size: 1.2rem; margin-bottom: 25px;'>{info['sub']}</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h3 style='color: white; margin-bottom: 15px;'>📸 풍경 & 문화 갤러리</h3>",
        unsafe_allow_html=True,
    )
    g_cols = st.columns(4)
    for idx, item in enumerate(info["gallery"]):
        with g_cols[idx]:
            st.image(item["url"], use_container_width=True)
            st.markdown(
                f"<div class='img-card'><p>{item['title']}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
