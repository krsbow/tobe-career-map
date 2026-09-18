"""
Career Card Component for TO BE Platform.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design (Explore.tsx).
"""

from typing import Dict, Any, Optional
import streamlit as st

def render_career_card(career: Dict[str, Any], show_matching_reasons: bool = False, key_prefix: str = "") -> None:
    """Render Figma-styled editorial career card."""
    career_id = career.get("id") or career.get("career_id")
    title = career.get("title", "Career")
    category = career.get("category_name", "Technology")
    tagline = career.get("tagline", "")
    core_skills = career.get("core_skills", [])[:4]
    alignment_tier = career.get("alignment_tier", "High Alignment")
    why_reasons = career.get("why_it_appeared", [])
    salary = career.get("salary_summary")

    if not salary and "salary_data" in career:
        salary = career.get("salary_data", {}).get("philippines", {}).get("mid_level", "Competitive")

    # Match badge
    match_pct = 94 if "Strong" in str(alignment_tier) else 85

    st.markdown(
        f"""
        <div class="tobe-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="tobe-badge tobe-badge-slate">{category}</span>
                <span style="font-size: 13px; font-weight: 600; color: #243760;">{match_pct}% Match</span>
            </div>
            <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 6px;">
                {title}
            </div>
            <div style="font-size: 14px; color: #6B7080; line-height: 1.5; margin-bottom: 14px;">
                {tagline}
            </div>
            <div style="margin-bottom: 12px;">
                {"".join([f'<span class="tobe-chip">{s}</span>' for s in core_skills])}
            </div>
            {f'<div style="font-size: 13px; color: #6B7080; margin-bottom: 14px;">Salary: <strong style="color: #1A1F2E;">{salary}</strong></div>' if salary else ''}
        </div>
        """,
        unsafe_allow_html=True
    )

    if show_matching_reasons and why_reasons:
        st.markdown(
            f"""
            <div style="background: #F0EFE9; border: 1px solid #E4E2DB; border-radius: 6px; padding: 10px 14px; margin-top: -10px; margin-bottom: 14px;">
                <div style="font-size: 11px; font-weight: 700; color: #243760; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Why this connects with you</div>
                {"".join([f'<div style="font-size: 13px; color: #1A1F2E; margin-bottom: 3px;">&bull; {r}</div>' for r in why_reasons[:2]])}
            </div>
            """,
            unsafe_allow_html=True
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Explore Details", key=f"{key_prefix}_exp_{career_id}", use_container_width=True):
            st.session_state["selected_explore_career_id"] = career_id
            st.session_state["nav_page"] = "Explore"
            st.rerun()

    with col2:
        if st.button("Build Roadmap", key=f"{key_prefix}_road_{career_id}", type="primary", use_container_width=True):
            st.session_state["target_career_id"] = career_id
            st.session_state["nav_page"] = "My Path"
            st.rerun()
