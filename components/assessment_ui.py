"""
Assessment Wizard UI Component for TO BE.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design (Discover.tsx).
"""

from typing import Dict, Any, List, Optional
import streamlit as st
from data.assessment_questions import ASSESSMENT_QUESTIONS, SKILL_CATEGORIES
from services.assessment import assessment_service
from services.career_matching import matching_engine
from services.database import db_service
from services.auth import auth_service
from components.career_card import render_career_card
from components.career_profile import render_career_profile
from components.mentor_ui import render_tobe_contextual_card

def render_assessment_wizard() -> None:
    """Render Figma-styled assessment wizard."""
    if "assessment_step" not in st.session_state:
        st.session_state["assessment_step"] = 0
    if "assessment_answers" not in st.session_state:
        st.session_state["assessment_answers"] = {}
    if "user_selected_skills" not in st.session_state:
        st.session_state["user_selected_skills"] = []
    if "assessment_completed" not in st.session_state:
        st.session_state["assessment_completed"] = False

    if st.session_state.get("assessment_completed"):
        render_assessment_results()
        return

    questions = assessment_service.get_questions()
    total_steps = len(questions) + 1  # +1 for technical skills step
    current_step = st.session_state["assessment_step"]

    # Header and Progress
    progress_val = min(1.0, max(0.0, (current_step) / total_steps))

    st.markdown(
        f"""
        <div style="margin-bottom: 24px;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B7080; margin-bottom: 8px;">
                Discovery
            </p>
            <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: 36px; font-weight: 400; letter-spacing: -0.025em; color: #1A1F2E; margin-bottom: 20px;">
                Let's learn what drives you.
            </h1>
            
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                <span style="font-size: 13px; color: #6B7080;">Step {current_step + 1} of {total_steps}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.progress(progress_val)

    # =========================================================================
    # QUESTION STEPS
    # =========================================================================
    if current_step < len(questions):
        q = questions[current_step]
        q_id = q["id"]
        q_type = q.get("type", "single_choice")
        dimension = q.get("dimension", "Career Discovery")

        st.markdown(
            f"""
            <div class="tobe-card" style="margin-top: 16px;">
                <span class="tobe-badge tobe-badge-navy" style="margin-bottom: 12px;">{dimension}</span>
                <div style="font-family: 'Fraunces', Georgia, serif; font-size: 22px; font-weight: 400; color: #1A1F2E; margin-bottom: 4px;">
                    {q["title"]}
                </div>
                {f'<div style="font-size: 14px; color: #6B7080; margin-bottom: 16px;">{q.get("subtitle")}</div>' if "subtitle" in q else ''}
            </div>
            """,
            unsafe_allow_html=True
        )

        options = q["options"]
        
        if q_type == "single_choice":
            opt_labels = [opt["text"] for opt in options]
            saved_id = st.session_state["assessment_answers"].get(q_id)
            default_index = 0
            if saved_id:
                for idx, opt in enumerate(options):
                    if opt["id"] == saved_id:
                        default_index = idx
                        break

            chosen_label = st.radio(
                "Select what feels most accurate to you:",
                opt_labels,
                index=default_index,
                key=f"radio_{q_id}"
            )
            for opt in options:
                if opt["text"] == chosen_label:
                    st.session_state["assessment_answers"][q_id] = opt["id"]
                    break

        elif q_type == "multi_select":
            max_sel = q.get("max_select", 3)
            saved_ids = st.session_state["assessment_answers"].get(q_id, [])
            selected_ids = []
            
            st.caption(f"Select up to {max_sel} choices:")
            for opt in options:
                is_checked = opt["id"] in saved_ids
                checked = st.checkbox(opt["text"], value=is_checked, key=f"chk_{q_id}_{opt['id']}")
                if checked:
                    selected_ids.append(opt["id"])

            st.session_state["assessment_answers"][q_id] = selected_ids[:max_sel]

    # =========================================================================
    # SKILLS STEP
    # =========================================================================
    else:
        st.markdown(
            """
            <div class="tobe-card" style="margin-top: 16px;">
                <span class="tobe-badge tobe-badge-slate" style="margin-bottom: 12px;">Prior Experience</span>
                <div style="font-family: 'Fraunces', Georgia, serif; font-size: 22px; font-weight: 400; color: #1A1F2E; margin-bottom: 4px;">
                    Do you have any existing technical tools or skills?
                </div>
                <div style="font-size: 14px; color: #6B7080;">
                    Select what you already know. <em>(Having no prior technical tools is completely fine—all roadmaps begin from ground zero.)</em>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        all_skills = list(st.session_state["user_selected_skills"])

        for category, skills_list in SKILL_CATEGORIES.items():
            with st.expander(category, expanded=(category == "Web & Frontend")):
                cols = st.columns(3)
                for idx, skill in enumerate(skills_list):
                    col = cols[idx % 3]
                    is_active = skill in all_skills
                    with col:
                        if st.checkbox(skill, value=is_active, key=f"sk_{category}_{skill}"):
                            if skill not in all_skills:
                                all_skills.append(skill)
                        else:
                            if skill in all_skills:
                                all_skills.remove(skill)

        st.session_state["user_selected_skills"] = all_skills

    # Navigation buttons
    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    btn_col1, btn_col2 = st.columns([1, 1])

    with btn_col1:
        if current_step > 0:
            if st.button("Previous Question", use_container_width=True):
                st.session_state["assessment_step"] -= 1
                st.rerun()

    with btn_col2:
        if current_step < total_steps - 1:
            if st.button("Continue", type="primary", use_container_width=True):
                st.session_state["assessment_step"] += 1
                st.rerun()
        else:
            if st.button("Complete Assessment", type="primary", use_container_width=True):
                try:
                    profile_result = assessment_service.process_answers(
                        st.session_state["assessment_answers"],
                        st.session_state["user_selected_skills"]
                    )
                    user = auth_service.get_current_user()
                    user_id = user["id"] if user else "guest"
                    db_service.save_assessment_result(user_id, profile_result)
                    st.session_state["latest_profile"] = profile_result
                    st.session_state["assessment_completed"] = True
                    st.rerun()
                except Exception as e:
                    st.error("Error processing assessment results. Please retry.")

def render_assessment_results():
    """Render Figma-styled assessment results."""
    user = auth_service.get_current_user()
    user_id = user["id"] if user else "guest"
    profile_data = st.session_state.get("latest_profile")
    if not profile_data:
        profile_data = db_service.get_latest_assessment(user_id)

    st.markdown(
        """
        <div class="tobe-hero-card" style="text-align: center;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #7A9E8E; margin-bottom: 6px;">
                Assessment Complete
            </p>
            <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: 36px; font-weight: 400; color: #1A1F2E; margin-bottom: 8px;">
                Your Career Matches
            </h1>
            <p style="font-size: 15px; color: #6B7080; max-width: 540px; margin: 0 auto;">
                Based on your interests, work styles, and preferences, here are paths aligned with your profile.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    r_col1, r_col2 = st.columns([3, 1])
    with r_col2:
        if st.button("Retake Assessment", use_container_width=True):
            st.session_state["assessment_step"] = 0
            st.session_state["assessment_answers"] = {}
            st.session_state["assessment_completed"] = False
            st.rerun()

    # Contextual TOBE prompt
    render_tobe_contextual_card(
        context_title="Want help interpreting these results?",
        context_prompt="Ask TOBE why these careers were recommended for you and how to weigh the trade-offs between them."
    )

    tab1, tab2 = st.tabs(["Recommended Careers", "RIASEC Dimension Breakdown"])

    with tab1:
        matches = matching_engine.get_matches(profile_data, limit=6)
        if matches:
            for career in matches:
                render_career_card(career, show_matching_reasons=True, key_prefix="res")
        else:
            st.info("Explore the Career Catalog to browse all paths.")

    with tab2:
        if profile_data:
            render_career_profile(profile_data)
