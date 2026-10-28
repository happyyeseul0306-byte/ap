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
    .search-box-wrapper {
        background-color: transparent !important;
        padding: 0px !important;
        box-shadow: none !important;
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

    /* 배너 카드형 버튼 스타일 */
    .banner-card-btn {
        background-size: cover;
        background-position: center;
        border-radius: 16px;
        padding: 30px;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 5px;
    }
    .banner-card-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.4);
    }

    /* 🎫 이미지 스타일실제 실물 보딩패스 티켓 디자인 */
    .boarding-pass {
        width: 100%;
        max-width: 580px;
        margin: 0 auto;
        background-color: #e5e7eb;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
        font-family: 'Arial', sans-serif;
        color: #1e293b;
    }
    .bp-header {
        background-color: #e2e8f0;
        padding: 16px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #cbd5e1;
    }
    .bp-header .pass-title {
        font-size: 0.75rem;
        font-weight: 700;
        color: #0284c7;
        letter-spacing: 1px;
    }
    .bp-header .passenger-name {
        font-size: 1.4rem;
        font-weight: 900;
        color: #0f172a;
        margin: 2px 0 0 0;
    }
    .bp-barcode {
        height: 38px;
        letter-spacing: 2px;
        font-family: 'Libre Barcode 128', 'Courier New', monospace;
        font-size: 32px;
        color: #0f172a;
        user-select: none;
    }
    .bp-body {
        background-color: #0284c7;
        color: white;
        padding: 24px;
        text-align: center;
    }
    .bp-route {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 12px;
    }
    .bp-loc-code {
        font-size: 2.3rem;
        font-weight: 900;
        letter-spacing: 1px;
    }
    .bp-loc-sub {
        font-size: 0.85rem;
        color: #e0f2fe;
        margin-top: -2px;
    }
    .bp-plane-icon {
        font-size: 2rem;
        transform: rotate(45deg);
    }
    .bp-divider {
        border: 0;
        border-top: 1px solid rgba(255, 255, 255, 0.4);
        margin: 16px 0;
    }
    .bp-times {
        display: flex;
        justify-content: space-around;
        font-size: 0.85rem;
    }
    .bp-time-title {
        font-size: 0.7rem;
        color: #e0f2fe;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 3px;
    }
    .bp-time-val {
        font-size: 1rem;
        font-weight: 700;
    }
    .bp-footer {
        background-color: #e2e8f0;
        padding: 16px 24px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        text-align: center;
    }
    .bp-foot-item .label {
        font-size: 0.7rem;
        font-weight: 700;
        color: #64748b;
        letter-spacing: 0.5px;
    }
    .bp-foot-item .value {
        font-size: 1.25rem;
        font-weight: 900;
        color: #0f172a;
        margin-top: 2px;
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

    ranking_ticker_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      .ticker-box {
        display: flex;
        align-items: center;
        background: #ffffff;
        padding: 12px 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        font-family: sans-serif;
      }
      .ticker-badge {
        background-color: #2563eb;
        color: white;
        font-weight: 700;
        font-size: 0.9rem;
        padding: 6px 14px;
        border-radius: 20px;
        margin-right: 15px;
        white-space: nowrap;
      }
      .ticker-content {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1e293b;
        transition: opacity 0.4s ease-in-out, transform 0.4s ease-in-out;
      }
    </style>
    </head>
    <body style="margin:0; padding:0; background:transparent;">
      <div class="ticker-box">
        <div class="ticker-badge">🔥 실시간 인기 여행지 순위</div>
        <div id="rank-text" class="ticker-content">1위 🗼 일본 도쿄 (최고 인기 메가폴리스)</div>
      </div>
      <script>
        const ranks = [
          "1위 🗼 일본 도쿄 (최고 인기 메가폴리스)",
          "2위 🛍️ 태국 방콕 (활기찬 야시장과 사원)",
          "3위 🌊 베트남 다낭 (에메랄드빛 미케 해변)",
          "4위 🏙️ 미국 뉴욕 (맨해튼 빌딩 숲과 센트럴 파크)",
          "5위 🥐 프랑스 파리 (낭만의 에펠탑과 센 강)",
          "6위 🏔️ 스위스 (체르마트 마테호른 & 알프스)",
          "7위 🧋 대만 타이베이 (식도락과 야시장 여행)"
        ];
        let idx = 0;
        const textElement = document.getElementById('rank-text');
        
        setInterval(() => {
          textElement.style.opacity = 0;
          textElement.style.transform = "translateY(8px)";
          setTimeout(() => {
            idx = (idx + 1) % ranks.length;
            textElement.innerText = ranks[idx];
            textElement.style.opacity = 1;
            textElement.style.transform = "translateY(0px)";
          }, 400);
        }, 3000);
      </script>
    </body>
    </html>
    """
    components.html(ranking_ticker_html, height=65)

    with st.container():
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

    st.markdown(
        "<h3 style='color: white; margin-top: 30px; margin-bottom: 15px;'>🔥 주요 인기 추천 여행지</h3>",
        unsafe_allow_html=True,
    )

    r1_c1, r1_c2, r1_c3 = st.columns(3)

    with r1_c1:
        st.markdown(
            """
            <div class="banner-card-btn" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1503899036084-c55cdd92da26');">
                <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; backdrop-filter: blur(4px);">
                    <h3 style="color:white; margin:0; font-size: 1.2rem;">🗼 도쿄 여행 트렌드</h3>
                    <p style="color:#e2e8f0; margin:4px 0 0 0; font-size:0.85rem;">화려한 도시와 다양한 식도락</p>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button(
            "👉 '도쿄' 상세 가이드", key="btn_tokyo", use_container_width=True
        ):
            st.session_state.selected_destination_info = "도쿄"
            st.session_state.step = "destination_detail"
            st.rerun()

    with r1_c2:
        st.markdown(
            """
            <div class="banner-card-btn" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1508009603885-50cf7c579365');">
                <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; backdrop-filter: blur(4px);">
                    <h3 style="color:white; margin:0; font-size: 1.2rem;">🏝️ 낭만의 방콕 휴가</h3>
                    <p style="color:#e2e8f0; margin:4px 0 0 0; font-size:0.85rem;">이국적인 사원과 야시장</p>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button(
            "👉 '방콕' 상세 가이드", key="btn_bangkok", use_container_width=True
        ):
            st.session_state.selected_destination_info = "방콕"
            st.session_state.step = "destination_detail"
            st.rerun()

    with r1_c3:
        st.markdown(
            """
            <div class="banner-card-btn" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34');">
                <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; backdrop-filter: blur(4px);">
                    <h3 style="color:white; margin:0; font-size: 1.2rem;">🥐 예술의 도시 파리</h3>
                    <p style="color:#e2e8f0; margin:4px 0 0 0; font-size:0.85rem;">낭만적인 에펠탑과 센 강</p>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button(
            "👉 '파리' 상세 가이드", key="btn_paris", use_container_width=True
        ):
            st.session_state.selected_destination_info = "파리"
            st.session_state.step = "destination_detail"
            st.rerun()

    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

    r2_c1, r2_c2, r2_c3 = st.columns(3)

    with r2_c1:
        st.markdown(
            """
            <div class="banner-card-btn" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1534430480872-3498386e7856');">
                <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; backdrop-filter: blur(4px);">
                    <h3 style="color:white; margin:0; font-size: 1.2rem;">🗽 미국 뉴욕</h3>
                    <p style="color:#e2e8f0; margin:4px 0 0 0; font-size:0.85rem;">맨해튼 빌딩 숲과 센트럴 파크</p>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button(
            "👉 '뉴욕' 상세 가이드", key="btn_newyork", use_container_width=True
        ):
            st.session_state.selected_destination_info = "뉴욕"
            st.session_state.step = "destination_detail"
            st.rerun()

    with r2_c2:
        st.markdown(
            """
            <div class="banner-card-btn" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1559592413-7cec4d0cae2b');">
                <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; backdrop-filter: blur(4px);">
                    <h3 style="color:white; margin:0; font-size: 1.2rem;">🌊 베트남 다낭</h3>
                    <p style="color:#e2e8f0; margin:4px 0 0 0; font-size:0.85rem;">에메랄드빛 미케 해변과 휴양</p>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button(
            "👉 '다낭' 상세 가이드", key="btn_danang", use_container_width=True
        ):
            st.session_state.selected_destination_info = "다낭"
            st.session_state.step = "destination_detail"
            st.rerun()

    with r2_c3:
        st.markdown(
            """
            <div class="banner-card-btn" style="background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b');">
                <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; backdrop-filter: blur(4px);">
                    <h3 style="color:white; margin:0; font-size: 1.2rem;">⛰️ 스위스 알프스</h3>
                    <p style="color:#e2e8f0; margin:4px 0 0 0; font-size:0.85rem;">만년설과 동화 같은 산악 마을</p>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button(
            "👉 '스위스' 상세 가이드", key="btn_swiss", use_container_width=True
        ):
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
            st.session_state.booking_data["destination"] = matching_dest
            st.session_state.booking_data["date"] = date.today()
            st.session_state.booking_data["time_range"] = (
                time(0, 0),
                time(23, 59),
            )
            st.session_state.step = "select_flight"
            st.rerun()

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
        st.markdown(
            """
            <div style="background: #ffffff; padding: 35px; border-radius: 12px; box-shadow: 0 6px 20px rgba(0,0,0,0.2); color: #05132d;">
                <div style="text-align: center; margin-bottom: 20px;">
                    <h2 style="color: #05132d; margin:0;">🔐 StarPort 로그인</h2>
                    <p style="color: #64748b; margin-top:5px;">서비스를 이용하려면 로그인해주세요.</p>
                </div>
        """,
            unsafe_allow_html=True,
        )

        with st.form("login_form"):
            st.markdown(
                '<p style="color: #05132d !important; font-weight: 800 !important; font-size: 1.05rem !important; margin-bottom: 5px;">이메일</p>',
                unsafe_allow_html=True,
            )
            email_input = st.text_input(
                "이메일", placeholder="example@email.com", label_visibility="collapsed"
            )

            st.markdown(
                "<div style='margin-top: 15px;'></div>", unsafe_allow_html=True
            )

            st.markdown(
                '<p style="color: #05132d !important; font-weight: 800 !important; font-size: 1.05rem !important; margin-bottom: 5px;">비밀번호</p>',
                unsafe_allow_html=True,
            )
            password_input = st.text_input(
                "비밀번호",
                type="password",
                placeholder="비밀번호를 입력하세요",
                label_visibility="collapsed",
            )

            st.markdown("<br>", unsafe_allow_html=True)
            login_submitted = st.form_submit_button(
                "로그인하기", type="primary", use_container_width=True
            )

            if login_submitted:
                if email_input and password_input:
                    st.session_state.is_logged_in = True
                    st.session_state.user_email = email_input
                    st.success("로그인 성공! 홈으로 이동합니다.")
                    st.session_state.step = "home"
                    st.rerun()
                else:
                    st.warning("이메일과 비밀번호를 모두 입력해주세요.")

        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 2. 비행기 목록 선택 화면
# ==========================================
elif st.session_state.step == "select_flight":
    if not st.session_state.is_logged_in:
        st.session_state.step = "login"
        st.rerun()

    if st.button("⬅️ 검색 조건 변경"):
        st.session_state.step = "home"
        st.rerun()

    b_data = st.session_state.booking_data
    dest_str = b_data["destination"]

    if any(
        k in dest_str
        for k in ["일본", "홍콩", "마카오", "대만", "중국", "몽골", "베트남"]
    ):
        flights = [
            {
                "id": 1,
                "airline": "대한항공",
                "flight_no": "KE101",
                "dep_time": "06:30",
                "arr_time": "09:00",
                "classes": [
                    {"seat": "일반석", "price": 580000},
                    {"seat": "비즈니스석", "price": 1250000},
                ],
            },
            {
                "id": 2,
                "airline": "아시아나항공",
                "flight_no": "OZ202",
                "dep_time": "08:15",
                "arr_time": "10:45",
                "classes": [
                    {"seat": "일반석", "price": 550000},
                    {"seat": "비즈니스석", "price": 1180000},
                ],
            },
            {
                "id": 3,
                "airline": "제주항공",
                "flight_no": "7C303",
                "dep_time": "09:40",
                "arr_time": "12:10",
                "classes": [
                    {"seat": "특가석", "price": 320000},
                    {"seat": "일반석", "price": 410000},
                ],
            },
            {
                "id": 4,
                "airline": "진에어",
                "flight_no": "LJ404",
                "dep_time": "11:00",
                "arr_time": "13:30",
                "classes": [
                    {"seat": "특가석", "price": 340000},
                    {"seat": "일반석", "price": 430000},
                ],
            },
            {
                "id": 5,
                "airline": "티웨이항공",
                "flight_no": "TW505",
                "dep_time": "12:30",
                "arr_time": "15:00",
                "classes": [
                    {"seat": "특가석", "price": 310000},
                    {"seat": "일반석", "price": 390000},
                ],
            },
        ]
    elif any(
        k in dest_str
        for k in [
            "프랑스",
            "영국",
            "이탈리아",
            "스페인",
            "독일",
            "스위스",
            "체코",
            "오스트리아",
            "튀르키예",
            "네덜란드",
        ]
    ):
        flights = [
            {
                "id": 1,
                "airline": "대한항공",
                "flight_no": "KE101",
                "dep_time": "10:30",
                "arr_time": "18:00",
                "classes": [
                    {"seat": "일반석", "price": 1580000},
                    {"seat": "비즈니스석", "price": 3850000},
                ],
            },
            {
                "id": 2,
                "airline": "아시아나항공",
                "flight_no": "OZ202",
                "dep_time": "11:15",
                "arr_time": "19:00",
                "classes": [
                    {"seat": "일반석", "price": 1490000},
                    {"seat": "비즈니스석", "price": 3650000},
                ],
            },
            {
                "id": 3,
                "airline": "폴란드항공",
                "flight_no": "LO303",
                "dep_time": "12:40",
                "arr_time": "20:10",
                "classes": [
                    {"seat": "특가석", "price": 1150000},
                    {"seat": "일반석", "price": 1320000},
                ],
            },
        ]
    else:
        flights = [
            {
                "id": 1,
                "airline": "대한항공",
                "flight_no": "KE101",
                "dep_time": "07:30",
                "arr_time": "13:00",
                "classes": [
                    {"seat": "일반석", "price": 980000},
                    {"seat": "비즈니스석", "price": 2400000},
                ],
            },
            {
                "id": 2,
                "airline": "아시아나항공",
                "flight_no": "OZ202",
                "dep_time": "09:15",
                "arr_time": "14:45",
                "classes": [
                    {"seat": "일반석", "price": 920000},
                    {"seat": "비즈니스석", "price": 2250000},
                ],
            },
            {
                "id": 3,
                "airline": "싱가포르항공",
                "flight_no": "SQ303",
                "dep_time": "10:40",
                "arr_time": "16:10",
                "classes": [
                    {"seat": "특가석", "price": 750000},
                    {"seat": "일반석", "price": 890000},
                ],
            },
        ]

    st.markdown(
        f"<h2 style='color: white;'>✈ {b_data['departure']} ➔ {b_data['destination']} 검색 결과</h2>",
        unsafe_allow_html=True,
    )
    t_start, t_end = b_data.get(
        "time_range", (time(0, 0), time(23, 59))
    )
    st.markdown(
        f"<p style='color: #94a3b8;'>선택일자: {b_data['date']} | 시간대: {t_start.strftime('%H:%M')} ~ {t_end.strftime('%H:%M')}</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    for f in flights:
        class_options = [
            f"{c['seat']} - {c['price']:,}원" for c in f["classes"]
        ]

        st.markdown(
            f"""
            <div class="flight-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                    <div>
                        <h3 style="margin:0; color:#05132d;">{f['airline']} <span style="font-size:0.8rem; color:#6b7270;">({f['flight_no']})</span></h3>
                        <p style="margin: 5px 0 0 0; color: #4b5563;">출발 <b>{f['dep_time']}</b> ➔ 도착 <b>{f['arr_time']}</b></p>
                    </div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

        col_c1, col_c2 = st.columns([2, 1])
        with col_c1:
            selected_class_str = st.selectbox(
                f"[{f['airline']} {f['flight_no']}] 좌석 등급 선택",
                class_options,
                key=f"class_sel_{f['id']}",
            )
        with col_c2:
            st.markdown(
                "<div style='margin-top: 28px;'></div>", unsafe_allow_html=True
            )
            if st.button(
                "이 항공편 예매하기", key=f"btn_sel_{f['id']}"
            ):
                chosen_idx = class_options.index(selected_class_str)
                chosen_seat_info = f["classes"][chosen_idx]

                st.session_state.booking_data["airline"] = f["airline"]
                st.session_state.booking_data["flight_no"] = f["flight_no"]
                st.session_state.booking_data["dep_time"] = f["dep_time"]
                st.session_state.booking_data["arr_time"] = f["arr_time"]
                st.session_state.booking_data["seat"] = chosen_seat_info["seat"]
                st.session_state.booking_data["price"] = chosen_seat_info["price"]

                st.session_state.step = "passenger_info"
                st.rerun()
        st.markdown(
            "<hr style='border: 0; border-top: 1px dashed rgba(255,255,255,0.2);'>",
            unsafe_allow_html=True,
        )

# ==========================================
# 3. 승객 정보 입력 화면
# ==========================================
elif st.session_state.step == "passenger_info":
    if not st.session_state.is_logged_in:
        st.session_state.step = "login"
        st.rerun()

    if st.button("⬅ 항공편 다시 선택"):
        st.session_state.step = "select_flight"
        st.rerun()

    st.markdown(
        "<h2 style='color: white;'>👤 탑승객 정보 입력</h2>",
        unsafe_allow_html=True,
    )

    with st.form("info_form"):
        name = st.text_input("탑승객 성함 (예: 홍길동)")
        birthdate = st.date_input(
            "생년월일", min_value=date(1920, 1, 1), max_value=date.today()
        )

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button(
            "✅ 결제 및 예매 확정", type="primary"
        )

        if submitted:
            if name:
                st.session_state.booking_data["name"] = name
                st.session_state.booking_data["birthdate"] = birthdate
                st.session_state.step = "success"
                st.rerun()
            else:
                st.warning("성함을 올바르게 입력해주세요.")

# ==========================================
# 4. 예매 완료 화면 (이미지 실물 보딩패스 완벽 재현)
# ==========================================
elif st.session_state.step == "success":
    if not st.session_state.is_logged_in:
        st.session_state.step = "login"
        st.rerun()

    st.balloons()

    st.markdown(
        "<h2 style='text-align: center; color: white;'>🎉 항공권 예매가 완료되었습니다!</h2>",
        unsafe_allow_html=True,
    )
    b = st.session_state.booking_data

    # 공항 코드 및 도시명 추출 파싱
    dep_full = b.get("departure", "서울/인천 (ICN)")
    dest_full = b.get("destination", "도쿄/나리타 (NRT) - 일본")

    dep_code = "ICN"
    if "(" in dep_full and ")" in dep_full:
        dep_code = dep_full.split("(")[1].split(")")[0]
    dep_city = dep_full.split("/")[0] if "/" in dep_full else "Incheon"

    dest_code = "NRT"
    if "(" in dest_full and ")" in dest_full:
        dest_code = dest_full.split("(")[1].split(")")[0]
    dest_city = dest_full.split("/")[0] if "/" in dest_full else "Tokyo"

    passenger_name = b.get("name", "PASSENGER").upper()
    flight_no = b.get("flight_no", "SP101")
    dep_time_str = f"{b.get('dep_time', '09:00')} {b.get('date', date.today()).strftime('%b %d %Y').upper()}"
    arr_time_str = f"{b.get('arr_time', '12:00')} {b.get('date', date.today()).strftime('%b %d %Y').upper()}"
    seat_type = b.get("seat", "일반석")

    col1, col2, col3 = st.columns([1, 2.5, 1])
    with col2:
        st.markdown(
            f"""
            <div class="boarding-pass">
                <!-- 상단 헤더 & 바코드 -->
                <div class="bp-header">
                    <div>
                        <div class="pass-title">BOARDING PASS</div>
                        <div class="passenger-name">{passenger_name}</div>
                    </div>
                    <div style="text-align: right;">
                        <div class="bp-barcode">||||||| | ||||| |||||||</div>
                    </div>
                </div>
                
                <!-- 중단 메인 여정 세션 (블루) -->
                <div class="bp-body">
                    <div class="bp-route">
                        <div>
                            <div class="bp-loc-code">{dep_code}</div>
                            <div class="bp-loc-sub">{dep_city}</div>
                        </div>
                        <div class="bp-plane-icon">✈</div>
                        <div>
                            <div class="bp-loc-code">{dest_code}</div>
                            <div class="bp-loc-sub">{dest_city}</div>
                        </div>
                    </div>
                    <hr class="bp-divider">
                    <div class="bp-times">
                        <div>
                            <div class="bp-time-title">BOARDING TIME</div>
                            <div class="bp-time-val">{dep_time_str}</div>
                        </div>
                        <div>
                            <div class="bp-time-title">DEPARTURE TIME</div>
                            <div class="bp-time-val">{arr_time_str}</div>
                        </div>
                    </div>
                </div>

                <!-- 하단 탑승 정보 (FLIGHT / GATE / SEAT) -->
                <div class="bp-footer">
                    <div class="bp-foot-item">
                        <div class="label">FLIGHT</div>
                        <div class="value">{flight_no}</div>
                    </div>
                    <div style="border-left: 2px solid #cbd5e1; height: 35px;"></div>
                    <div class="bp-foot-item">
                        <div class="label">GATE</div>
                        <div class="value">41A</div>
                    </div>
                    <div style="border-left: 2px solid #cbd5e1; height: 35px;"></div>
                    <div class="bp-foot-item">
                        <div class="label">SEAT NO.</div>
                        <div class="value">10C</div>
                    </div>
                    <div style="border-left: 2px solid #cbd5e1; height: 35px;"></div>
                    <div class="bp-foot-item">
                        <div class="label">CLASS</div>
                        <div class="value" style="font-size:0.95rem; font-weight:800; color:#0284c7;">{seat_type}</div>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 15px; color: #38bdf8; font-size: 1.15rem; font-weight: bold;">
                💳 결제 완료 금액: {b.get('price', 0):,}원
            </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🏠 처음으로 돌아가기", use_container_width=True):
            st.session_state.booking_data = {}
            st.session_state.step = "home"
            st.rerun()
