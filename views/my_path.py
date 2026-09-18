"""
My Path Page View for TO BE Platform.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design (MyPath.tsx).
"""

import streamlit as st
from services.auth import auth_service
from services.database import db_service
from services.career_service import career_service
from services.roadmap_service import roadmap_service
from components.roadmap_ui import render_interactive_roadmap
from components.mentor_ui import render_tobe_contextual_card

def render_my_path_page():
    """Render Figma-styled milestone roadmap and pathway tracker."""
    user = auth_service.get_current_user()
    user_id = user["id"] if user else "guest"

    target_career_id = st.session_state.get("target_career_id")
    roadmaps = db_service.get_user_roadmaps(user_id)

    if target_career_id:
        existing = next((r for r in roadmaps if r.get("career_id") == target_career_id), None)
        if not existing:
            with st.spinner("Building your personalized roadmap..."):
                new_roadmap = roadmap_service.generate_roadmap(user_id=user_id, career_id=target_career_id)
                db_service.save_roadmap(user_id, new_roadmap)
                active_roadmap = new_roadmap
        else:
            active_roadmap = existing
    elif roadmaps:
        active_roadmap = roadmaps[0]
    else:
        careers = career_service.get_all_careers()
        default_id = careers[0]["id"] if careers else "frontend-developer"
        new_roadmap = roadmap_service.generate_roadmap(user_id=user_id, career_id=default_id)
        db_service.save_roadmap(user_id, new_roadmap)
        active_roadmap = new_roadmap

    # Career Switcher
    all_careers = career_service.get_all_careers()
    career_map = {c["id"]: c["title"] for c in all_careers}
    
    current_career_id = active_roadmap.get("career_id", "")
    current_idx = list(career_map.keys()).index(current_career_id) if current_career_id in career_map else 0
    
    col_sel, _ = st.columns([2, 1])
    with col_sel:
        selected_id = st.selectbox(
            "Current Roadmap Target Career",
            options=list(career_map.keys()),
            format_func=lambda cid: career_map.get(cid, cid),
            index=current_idx,
            key="roadmap_career_selector"
        )
        if selected_id != current_career_id:
            st.session_state["target_career_id"] = selected_id
            st.rerun()

    # Render Roadmap UI
    render_interactive_roadmap(active_roadmap, user_id=user_id)

    # Contextual TOBE prompt
    render_tobe_contextual_card(
        context_title="Need guidance on your roadmap?",
        context_prompt="Ask TOBE how to tackle your current milestone, find project ideas, or prepare for job interviews in this field."
    )
