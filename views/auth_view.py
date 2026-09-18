"""
Authentication View for TO BE Platform.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design.
"""

import streamlit as st
from config import PROJECT_NAME
from services.auth import auth_service
from components.theme import render_footer

def render_auth_view():
    """Render Figma-styled split/centered authentication view."""
    auth_mode = st.session_state.get("auth_mode", "signup")

    col_back, _ = st.columns([1, 5])
    with col_back:
        if st.button("← Back to Overview", key="auth_back_btn"):
            st.session_state["view_mode"] = "landing"
            st.rerun()

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.2])

    with col_left:
        st.markdown(
            f"""
            <div style="background: #243760; border-radius: 6px; padding: 48px 36px; color: white; height: 100%; min-height: 440px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 24px; font-weight: 500; color: white; margin-bottom: 24px;">
                        {PROJECT_NAME}
                    </div>
                    <p style="font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 12px;">
                        Career Discovery
                    </p>
                    <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 32px; font-weight: 400; color: white; line-height: 1.2; margin-bottom: 20px;">
                        Reflect on who you are.<br />Discover what you could be.
                    </h2>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.75); line-height: 1.6;">
                        Explore careers based on your real strengths, understand the trade-offs, and chart your practical path.
                    </p>
                </div>
                <div style="font-size: 12px; color: rgba(255,255,255,0.4); padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
                    What to be &bull; Why to be &bull; How to be
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_right:
        st.markdown(
            f"""
            <div class="tobe-card" style="padding: 36px 32px; min-height: 440px;">
                <div style="font-family: 'Fraunces', Georgia, serif; font-size: 26px; font-weight: 400; color: #1A1F2E; margin-bottom: 4px;">
                    {"Welcome back" if auth_mode == "login" else "Create your account"}
                </div>
                <div style="font-size: 14px; color: #6B7080; margin-bottom: 24px;">
                    {"Sign in to continue your career discovery." if auth_mode == "login" else "Start charting your personalized career direction."}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if auth_mode == "login":
            email = st.text_input("Email address", key="login_email")
            password = st.text_input("Password", type="password", key="login_pwd")

            if st.button("Sign In", type="primary", use_container_width=True, key="btn_do_login"):
                if not email or not password:
                    st.error("Please enter both email and password.")
                else:
                    success, user_data, err = auth_service.sign_in(email, password)
                    if success:
                        st.session_state["is_authenticated"] = True
                        st.session_state["view_mode"] = "app"
                        st.session_state["nav_page"] = "Home"
                        st.rerun()
                    else:
                        st.error(f"Sign in failed: {err}")

            st.markdown("<div style='margin-top: 16px; text-align: center; font-size: 13px; color: #6B7080;'>Don't have an account?</div>", unsafe_allow_html=True)
            if st.button("Create Account Instead", use_container_width=True, key="btn_sw_signup"):
                st.session_state["auth_mode"] = "signup"
                st.rerun()

        else:
            name = st.text_input("Full Name", key="reg_name")
            email = st.text_input("Email address", key="reg_email")
            password = st.text_input("Password (min 6 characters)", type="password", key="reg_pwd")

            if st.button("Create Account", type="primary", use_container_width=True, key="btn_do_signup"):
                if not email or not password:
                    st.error("Please provide your name, email, and password.")
                else:
                    success, user_data, err = auth_service.sign_up(email, password, preferred_name=name)
                    if success:
                        st.session_state["is_authenticated"] = True
                        st.session_state["view_mode"] = "app"
                        st.session_state["nav_page"] = "Home"
                        st.rerun()
                    else:
                        st.error(f"Account creation failed: {err}")

            st.markdown("<div style='margin-top: 16px; text-align: center; font-size: 13px; color: #6B7080;'>Already have an account?</div>", unsafe_allow_html=True)
            if st.button("Sign In Instead", use_container_width=True, key="btn_sw_login"):
                st.session_state["auth_mode"] = "login"
                st.rerun()

        st.markdown("<div style='margin: 20px 0 10px 0; border-top: 1px solid #E4E2DB;'></div>", unsafe_allow_html=True)
        if st.button("Continue as Guest Explorer", use_container_width=True, key="btn_guest_access"):
            st.session_state["is_authenticated"] = True
            st.session_state["view_mode"] = "app"
            st.session_state["nav_page"] = "Home"
            st.rerun()

    render_footer()
