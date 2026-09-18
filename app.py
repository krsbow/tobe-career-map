"""
TO BE: AI Career Discovery & Roadmap Platform
Main Application Entry Point & Navigation Controller
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design.
Strict Navigation: TO BE | Home | Discover | Explore | My Path | Profile.
Zero duplicate navigation, zero emojis, contextual TOBE AI integration.
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TO BE — Explore what could be next",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from config import PROJECT_NAME, PROJECT_TAGLINE, AI_MENTOR_NAME
from components.theme import inject_global_theme, render_footer
from components.navbar import render_navbar
from services.auth import auth_service
from services.database import db_service

# Import views
from views import (
    render_landing_page,
    render_auth_view,
    render_home_page,
    render_discover_page,
    render_explore_page,
    render_my_path_page,
    render_profile_page
)

def main():
    # Inject Figma-accurate global theme & hide default Streamlit sidebar
    inject_global_theme()

    # Master state initialization
    if "view_mode" not in st.session_state:
        st.session_state["view_mode"] = "landing"
    if "is_authenticated" not in st.session_state:
        st.session_state["is_authenticated"] = False
    if "nav_page" not in st.session_state:
        st.session_state["nav_page"] = "Home"

    view_mode = st.session_state.get("view_mode", "landing")

    # =========================================================================
    # 1. UNAUTHENTICATED LANDING PAGE
    # =========================================================================
    if view_mode == "landing":
        render_landing_page()
        return

    # =========================================================================
    # 2. AUTHENTICATION VIEW
    # =========================================================================
    elif view_mode == "auth":
        render_auth_view()
        return

    # =========================================================================
    # 3. AUTHENTICATED WORKSPACE
    # =========================================================================
    elif view_mode == "app":
        # Render top header (Logo on left, user on right)
        render_navbar()

        # Strict Figma Navigation: Home | Discover | Explore | My Path | Profile
        nav_tabs = [
            "Home",
            "Discover",
            "Explore",
            "My Path",
            "Profile"
        ]

        try:
            current_idx = nav_tabs.index(st.session_state["nav_page"])
        except ValueError:
            current_idx = 0

        selected_nav = st.radio(
            "Navigation",
            nav_tabs,
            index=current_idx,
            horizontal=True,
            label_visibility="collapsed",
            key="main_top_nav"
        )

        if selected_nav != st.session_state["nav_page"]:
            st.session_state["nav_page"] = selected_nav
            st.rerun()

        current_page = st.session_state["nav_page"]

        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

        # Route cleanly to the selected view
        try:
            if current_page == "Home":
                render_home_page()
            elif current_page == "Discover":
                render_discover_page()
            elif current_page == "Explore":
                render_explore_page()
            elif current_page == "My Path":
                render_my_path_page()
            elif current_page == "Profile":
                render_profile_page()
        except Exception as e:
            st.error("Something went wrong while loading this page. Please refresh.")
            if st.button("Reload Page"):
                st.rerun()

        # Render footer with attribution "created by krsbow"
        render_footer()

if __name__ == "__main__":
    main()
