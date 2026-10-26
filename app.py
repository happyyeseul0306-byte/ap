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
        padding: 10px 0;
        margin: 0;
        font-size: 1rem;
    }
    
    /* 검색 및 입력 영역 라벨 글자 선명하게 강조 */
    div[data-testid="stSelectbox"] label p,
    div[data-testid="stDateInput"] label p,
    div[data-testid="stSlider"] label p,
    div[data-testid="stTextInput"] label p {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
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

    destinations_list = [
        "도쿄/나리타 (NRT) - 일본",
        "도쿄/하네다 (HND) - 일본",
        "오사카/간사이 (KIX) - 일본",
        "후쿠오카 (FUK) - 일본",
        "삿포로/신치토세 (CTS) - 일본",
        "방콕/수완나품 (BKK) - 태국",
        "치앙마이 (CNX) - 태국",
        "푸켓 (HKT) - 태국",
        "다낭 (DAD) - 베트남",
        "나트랑/캄란 (CXR) - 베트남",
        "싱가포르 (SIN) - 싱가포르",
        "홍콩 (HKG) - 홍콩",
        "타이베이/타오위안 (TPE) - 대만",
        "파리/샤를드골 (CDG) - 프랑스",
        "런던/히드로 (LHR) - 영국",
        "로마/피우미치노 (FCO) - 이탈리아",
        "스위스/취리히 (ZRH) - 스위스",
        "뉴욕/JFK (JFK) - 미국",
        "로스앤젤레스 (LAX) - 미국",
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
            "img_title": "🗼 도쿄 타워와 도심 전경",
            "img_url": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc",
            "desc": "도쿄는 첨단 기술과 오랜 전통문화가 조화를 이루는 세계적인 대도시입니다. 시부야 스크램블 교차로, 아사쿠사 센소지 사원, 다양한 전통 라멘 및 스시 맛집이 자리 잡고 있습니다.",
            "best_season": "3~5월 (화사한 벚꽃 시즌) 및 9~11월 (선선한 단풍 시즌)",
            "tip": "도쿄 지하철 이용 시 스마트폰 교통카드(Suica 또는 Pasmo)를 등록해 두면 편하게 이동할 수 있습니다.",
            "spots": [
                "시부야 스크램블 교차로 & 스카이트리 전망대",
                "도쿄 디즈니랜드 & 디즈니씨",
                "아사쿠사 센소지 사원",
                "신주쿠 교엔 국립공원 & 메이지 신궁",
            ],
            "foods": [
                "츠키지 시장 참치 초밥 & 장어덮밥",
                "진한 돈골 육수의 미소/돈코츠 라멘",
                "철판 위에서 볶아 먹는 몬쟈야키",
                "숯불 직화 야키토리",
            ],
        },
        "방콕": {
            "title": "🏝 태국 방콕 (Bangkok)",
            "sub": "활기찬 야시장과 찬란한 불교 사원의 도시",
            "img_title": "🛍️ 방콕 야시장",
            "img_url": "https://images.unsplash.com/photo-1508009603885-50cf7c579365",
            "desc": "방콕은 화려한 왕궁과 웅장한 불교 사원, 짜오프라야 강변의 풍경 및 밤문화를 자랑하는 활기 넘치는 세계적인 여행지입니다.",
            "best_season": "11월 ~ 2월 (비가 적고 쾌적한 건기)",
            "tip": "사원 방문 시 반바지나 민소매 차림은 입장이 제한될 수 있으므로 얇은 긴 옷을 준비하세요.",
            "spots": [
                "짜오프라야 강변 왓 아룬 (새벽 사원)",
                "방콕 왕궁 & 왓 포 거대 와불상",
                "짜뚜짝 주말 시장",
                "카오산 로드 (배낭여행자들의 거리)",
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
            "img_title": "🗼 파리 에펠탑과 센 강",
            "img_url": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f",
            "desc": "센 강이 흐르는 파리는 고풍스러운 도로, 세계 명화를 품은 루브르 박물관, 에펠탑, 향긋한 베이커리가 늘어선 노천 카페의 정취를 자랑합니다.",
            "best_season": "5~6월 (봄날) 및 9~10월 (가을)",
            "tip": "에펠탑이나 루브르 박물관 등의 인기 입장권은 출국 전 사전 예약이 필수적입니다.",
            "spots": [
                "에펠탑 & 트로카데로 광장",
                "루브르 박물관 & 오르세 미술관",
                "몽마르트르 언덕 & 사크레쾨르 대성당",
                "샹젤리제 거리 & 개선문",
            ],
            "foods": [
                "갓 구운 바삭한 크루아상 & 바게트",
                "치즈가 올라간 프렌치 어니언 수프",
                "달콤하고 바삭한 색색의 마카롱",
                "스테이크 프릿 (스테이크 & 감자튀김)",
            ],
        },
        "뉴욕": {
            "title": "🗽 미국 뉴욕 (New York)",
            "sub": "잠들지 않는 세계 경제와 문화의 메카",
            "img_title": "🏙️ 뉴욕 센트럴 파크와 맨해튼 빌딩 숲",
            "img_url": "https://images.unsplash.com/photo-1534430480872-3498386e7856",
            "desc": "뉴욕은 자유의 여신상, 브루클린 브릿지, 타임스 스퀘어, 화려한 마천루가 눈을 사로잡는 세계 문화와 예술의 핵심 도시입니다.",
            "best_season": "9~11월 (센트럴 파크 단풍 시즌)",
            "tip": "식당 이용 시 금액의 15~20% 상당의 팁 문화가 일반적입니다.",
            "spots": [
                "타임스 스퀘어 & 브로드웨이 뮤지컬",
                "센트럴 파크",
                "자유의 여신상 페리 투어",
                "엠파이어 스테이트 빌딩 & 톱오브더락 전망대",
            ],
            "foods": [
                "큼직한 한 조각 뉴욕 화덕피자",
                "패스트라미 샌드위치",
                "쫄깃한 뉴욕 베이글 & 크림치즈",
                "정통 드라이에이징 스테이크",
            ],
        },
        "다낭": {
            "title": "🌊 베트남 다낭 (Da Nang)",
            "sub": "에메랄드빛 미케 해변과 휴양 리조트",
            "img_title": "🌉 베트남 다낭 바나힐 골든 브릿지",
            "img_url": "https://images.unsplash.com/photo-1559592413-7cec4d0cae2b",
            "desc": "다낭은 탁 트인 에메랄드빛 미케 해변과 풍등 야경이 매력적인 유네스코 유산 호이안 구시가지가 접해 있어 최고의 휴양지로 사랑받고 있습니다.",
            "best_season": "2월 ~ 8월 (파도가 잔잔한 건기)",
            "tip": "현지 이동 시에는 모바일 차량 호출 앱 'Grab(그랩)'을 이용하시면 안전하고 간편합니다.",
            "spots": [
                "세계적인 해변 미케 비치",
                "바나힐 테마파크 & 골든 브릿지",
                "호이안 올드타운 (풍등 야경)",
                "오행산 (마블 마운틴)",
            ],
            "foods": [
                "진한 육수의 베트남 소고기 쌀국수",
                "바삭한 부침개 반쎄오",
                "숯불 돼지고기 구이 분짜",
                "싱싱한 해산물 구이",
            ],
        },
        "스위스": {
            "title": "⛰️ 스위스 취리히 / 인터라켄 (Switzerland)",
            "sub": "알프스 대자연과 만년설의 동화 마을",
            "img_title": "🏔️ 스위스 체르마트 마테호른과 알프스 마을",
            "img_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
            "desc": "스위스는 융프라우, 알프스 산맥의 만년설, 깨끗하고 투명한 호수가 만들어내는 동화 같은 산악 자경을 품은 대표 힐링 여행지입니다.",
            "best_season": "6~8월 (하이킹) 및 12~2월 (겨울 설경)",
            "tip": "기차와 유람선을 모두 이용할 수 있는 '스위스 트래블 패스'를 이용하는 것이 훨씬 경제적입니다.",
            "spots": [
                "융프라우요흐 (유럽의 지붕 전망대)",
                "인터라켄 하더 쿨룸 전망대",
                "루체른 카펠교 & 호수 산책로",
                "체르마트 마테호른 봉우리",
            ],
            "foods": [
                "고소하고 따뜻한 스위스 치즈 퐁듀",
                "치즈 녹여 얹은 라클렛",
                "감자전 뢰스티",
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
        "<h3 style='color: white; margin-bottom: 15px;'>📸 대표 풍경</h3>",
        unsafe_allow_html=True,
    )
    
    col_l, col_c, col_r = st.columns([1, 2.2, 1])
    with col_c:
        st.image(info["img_url"], use_container_width=True)
        st.markdown(
            f"<div class='img-card'><p>{info['img_title']}</p></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="dest-info-box">
            <h3>📖 상세 가이드 및 정보</h3>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">{info['desc']}</p>
            <hr style="border: 0; border-top: 1px solid #e5e7eb; margin: 15px 0;">
            <p><b>☀️ 추천 여행 시기:</b> {info['best_season']}</p>
            <p><b>💡 현지 이용 팁:</b> {info['tip']}</p>
            <hr style="border: 0; border-top: 1px solid #e5e7eb; margin: 15px 0;">
            <h4>✨ 추천 명소</h4>
            <ul>
                {"".join([f"<li>{s}</li>" for s in info['spots']])}
            </ul>
            <h4>🍲 대표 미식</h4>
            <ul>
                {"".join([f"<li>{f}</li>" for f in info['foods']])}
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button(
        f"✈️ '{dest_name}' 항공권 실시간 시가 검색하러 가기",
        type="primary",
        use_container_width=True,
    ):
        if not st.session_state.is_logged_in:
            st.warning("🔒 로그인이 필요한 서비스입니다! 먼저 로그인해주세요.")
            st.session_state.step = "login"
            st.rerun()
        else:
            matching_dest = "도쿄/나리타 (NRT) - 일본"
            if dest_name == "방콕":
                matching_dest = "방콕/수완나품 (BKK) - 태국"
            elif dest_name == "파리":
                matching_dest = "파리/샤를드골 (CDG) - 프랑스"
            elif dest_name == "뉴욕":
                matching_dest = "뉴욕/JFK (JFK) - 미국"
            elif dest_name == "다낭":
                matching_dest = "다낭 (DAD) - 베트남"
            elif dest_name == "스위스":
                matching_dest = "스위스/취리히 (ZRH) - 스위스"

            st.session_state.booking_data["departure"] = "서울/인천 (ICN)"
