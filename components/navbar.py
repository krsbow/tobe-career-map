"""
Top Navigation Header for TO BE Platform (Figma Design).
Header: TO BE Logo + User Profile / Log Out on the right. Zero emojis.
"""

import streamlit as st
from config import PROJECT_NAME
from services.auth import auth_service

def render_navbar():
    """Render top brand header with user session controls."""
    user = auth_service.get_current_user()
    user_name = user.get("preferred_name", "Explorer") if user else "Explorer"
    
    col_logo, col_space, col_user = st.columns([2, 3, 2])

    with col_logo:
        st.markdown(
            f"""
            <div style="font-family: 'Fraunces', Georgia, serif; font-size: 1.4rem; font-weight: 500; letter-spacing: -0.03em; color: #243760; padding-top: 4px;">
                {PROJECT_NAME}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_user:
        c_u1, c_u2 = st.columns([1.5, 1])
        with c_u1:
            st.markdown(
                f"""
                <div style="text-align: right; padding-top: 8px; font-size: 0.88rem; font-weight: 500; color: #1A1F2E;">
                    {user_name}
                </div>
                """,
                unsafe_allow_html=True
            )
        with c_u2:
            if st.button("Log Out", key="top_logout_btn"):
                auth_service.sign_out()
                st.session_state["is_authenticated"] = False
                st.session_state["view_mode"] = "landing"
                st.session_state["nav_page"] = "Home"
                st.rerun()
