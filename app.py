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
            <div style="background: #ffffff; padding: 35px; border-radius: 12px; box-shadow: 0 6px 20px rgba(0,0,0,0.2); color: #05132d;">
                <div style="text-align: center; margin-bottom: 20px;">
                    <h2 style="color: #05132d; margin:0;">🔐 StarPort 로그인</h2>
                    <p style="color: #64748b; margin-top:5px;">서비스를 이용하려면 로그인해주세요.</p>
                </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            # 이메일 입력창 위에 선명한 텍스트 라벨 추가
            st.markdown('<p style="color: #05132d !important; font-weight: 800 !important; font-size: 1.05rem !important; margin-bottom: 5px;">이메일</p>', unsafe_allow_html=True)
            email_input = st.text_input("이메일", placeholder="example@email.com", label_visibility="collapsed")
            
            st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            
            # 비밀번호 입력창 위에 선명한 텍스트 라벨 추가
            st.markdown('<p style="color: #05132d !important; font-weight: 800 !important; font-size: 1.05rem !important; margin-bottom: 5px;">비밀번호</p>', unsafe_allow_html=True)
            password_input = st.text_input("비밀번호", type="password", placeholder="비밀번호를 입력하세요", label_visibility="collapsed")
            
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
        
        st.markdown("</div>", unsafe_allow_html=True)
