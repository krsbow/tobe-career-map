"""
Home Page View for TO BE Platform.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design (Home.tsx).
Greeting: "{Greeting}, {user_name}, where do you want to go today?"
Quick links: Discover (What to be), Explore (Why to be), My Path (How to be).
"""

import datetime
import streamlit as st
from config import PROJECT_NAME, AI_MENTOR_NAME
from services.auth import auth_service
from services.database import db_service
from services.career_service import career_service
from services.roadmap_service import roadmap_service
from components.career_card import render_career_card
from components.mentor_ui import render_tobe_contextual_card

def render_home_page():
    """Render Figma-styled personal workspace dashboard."""
    user = auth_service.get_current_user()
    user_id = user["id"] if user else "guest"
    user_name = user.get("preferred_name", "Explorer") if user else "Explorer"

    # Dynamic time greeting
    hour = datetime.datetime.now().hour
    greeting = "Good morning" if hour < 12 else ("Good afternoon" if hour < 17 else "Good evening")

    try:
        active_roadmaps = db_service.get_user_roadmaps(user_id)
    except Exception:
        active_roadmaps = []

    # =========================================================================
    # GREETING
    # =========================================================================
    st.markdown(
        f"""
        <div style="margin-bottom: 40px;">
            <p style="font-size: 14px; color: #6B7080; margin-bottom: 6px;">{greeting}</p>
            <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: clamp(32px, 4.5vw, 48px); font-weight: 400; letter-spacing: -0.03em; color: #1A1F2E; line-height: 1.15;">
                {user_name}, where do you want to go today?
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================================================================
    # QUICK NAVIGATION CARDS (Discover, Explore, My Path)
    # =========================================================================
    col_q1, col_q2, col_q3 = st.columns(3)

    with col_q1:
        st.markdown(
            """
            <div class="tobe-card" style="height: 180px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #243760; margin-bottom: 16px;"></div>
                    <div style="font-size: 17px; font-weight: 600; color: #1A1F2E; margin-bottom: 4px;">Discover</div>
                    <div style="font-size: 13px; color: #6B7080;">What to be &mdash; find your match</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Start Discovery", key="home_quick_disc", type="primary", use_container_width=True):
            st.session_state["nav_page"] = "Discover"
            st.rerun()

    with col_q2:
        st.markdown(
            """
            <div class="tobe-card" style="height: 180px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #7A9E8E; margin-bottom: 16px;"></div>
                    <div style="font-size: 17px; font-weight: 600; color: #1A1F2E; margin-bottom: 4px;">Explore</div>
                    <div style="font-size: 13px; color: #6B7080;">Why to be &mdash; understand each path</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Explore Careers", key="home_quick_exp", use_container_width=True):
            st.session_state["nav_page"] = "Explore"
            st.rerun()

    with col_q3:
        st.markdown(
            """
            <div class="tobe-card" style="height: 180px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #5B7FA6; margin-bottom: 16px;"></div>
                    <div style="font-size: 17px; font-weight: 600; color: #1A1F2E; margin-bottom: 4px;">My Path</div>
                    <div style="font-size: 13px; color: #6B7080;">How to be &mdash; your step-by-step plan</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("View My Path", key="home_quick_path", use_container_width=True):
            st.session_state["nav_page"] = "My Path"
            st.rerun()

    st.markdown("<div style='margin-top: 36px;'></div>", unsafe_allow_html=True)

    # =========================================================================
    # ACTIVE PATHWAY & NEXT STEP
    # =========================================================================
    if active_roadmaps:
        latest_roadmap = active_roadmaps[0]
        try:
            next_step = roadmap_service.get_next_recommended_step(latest_roadmap)
            prog = roadmap_service.calculate_progress(latest_roadmap)

            st.markdown(
                f"""
                <div class="tobe-card" style="border-left: 3px solid #243760; padding: 24px;">
                    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                        <span class="tobe-badge tobe-badge-navy">Active Roadmap &bull; {prog['overall_percentage']}% Complete</span>
                    </div>
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 4px;">
                        {latest_roadmap.get('title')}
                    </div>
                    {f'<div style="font-size: 14px; color: #475569; margin-top: 6px;">Next step: <strong>{next_step["item"]["title"]}</strong> ({next_step["phase_title"]})</div>' if next_step else ''}
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception:
            pass

    # =========================================================================
    # CONTEXTUAL TOBE AI ASSISTANT CARD
    # =========================================================================
    render_tobe_contextual_card(
        context_title=f"Thinking through a career question?",
        context_prompt=f"Talk with {AI_MENTOR_NAME} about specific industries, skill priorities, or day-to-day work realities."
    )

    # =========================================================================
    # FEATURED CAREER PATHS
    # =========================================================================
    st.markdown(
        """
        <div style="margin: 36px 0 20px 0;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B7080; margin-bottom: 4px;">
                Curated For You
            </p>
            <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 26px; font-weight: 400; color: #1A1F2E;">
                Featured career paths
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    try:
        featured_careers = career_service.get_all_careers()[:3]
        for c in featured_careers:
            render_career_card(c, key_prefix="home_feat")
    except Exception:
        st.info("Careers loading...")
