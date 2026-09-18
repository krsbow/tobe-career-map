"""
Profile Page View for TO BE Platform.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design.
"""

import streamlit as st
from services.auth import auth_service
from services.database import db_service
from components.career_profile import render_career_profile

def render_profile_page():
    """Render Figma-styled user profile and RIASEC history."""
    user = auth_service.get_current_user()
    user_id = user["id"] if user else "guest"
    user_name = user.get("preferred_name", "Explorer") if user else "Explorer"
    user_email = user.get("email", "guest@tobe.app") if user else "guest@tobe.app"

    st.markdown(
        f"""
        <div style="margin-bottom: 32px;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B7080; margin-bottom: 8px;">
                Account
            </p>
            <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: 36px; font-weight: 400; color: #1A1F2E; margin-bottom: 6px;">
                Profile & Discovery History
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Basic Details
    st.markdown(
        f"""
        <div class="tobe-card">
            <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 12px;">
                Account Information
            </div>
            <div style="font-size: 14px; color: #1A1F2E; margin-bottom: 6px;">
                <strong>Name:</strong> {user_name}
            </div>
            <div style="font-size: 14px; color: #1A1F2E; margin-bottom: 6px;">
                <strong>Email:</strong> {user_email}
            </div>
            <div style="font-size: 14px; color: #6B7080;">
                <strong>Mode:</strong> Local Session &bull; Cloud Ready
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Assessment Breakdown
    latest_assessment = db_service.get_latest_assessment(user_id)
    if latest_assessment:
        render_career_profile(latest_assessment)
    else:
        st.markdown(
            """
            <div class="tobe-card" style="text-align: center; padding: 36px;">
                <div style="font-family: 'Fraunces', Georgia, serif; font-size: 22px; font-weight: 400; color: #1A1F2E; margin-bottom: 6px;">
                    No Assessment Completed Yet
                </div>
                <div style="font-size: 14px; color: #6B7080; margin-bottom: 18px;">
                    Take the 5-minute career discovery assessment to unlock your RIASEC interest breakdown and personalized matches.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Take Discovery Assessment", type="primary"):
            st.session_state["nav_page"] = "Discover"
            st.rerun()

    # Active Roadmaps list
    roadmaps = db_service.get_user_roadmaps(user_id)
    if roadmaps:
        st.markdown(
            """
            <div style="margin: 32px 0 16px 0;">
                <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 24px; font-weight: 400; color: #1A1F2E;">
                    Active Roadmaps
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        for r in roadmaps:
            st.markdown(
                f"""
                <div class="tobe-card" style="padding: 18px 20px;">
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 18px; font-weight: 500; color: #1A1F2E;">{r.get('title')}</div>
                    <div style="font-size: 13px; color: #6B7080; margin-top: 4px;">{r.get('description', '')}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
