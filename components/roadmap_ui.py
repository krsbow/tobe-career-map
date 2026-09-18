"""
Interactive Roadmap UI Component for TO BE.
Aesthetic: Minimal, clean, sleek, editorial milestone tracker with zero emojis.
"""

from typing import Dict, Any, Optional
import streamlit as st
from services.roadmap_service import roadmap_service
from services.database import db_service
from utils.formatting import format_date_human
from components.icons import get_icon

def render_interactive_roadmap(roadmap: Dict[str, Any], user_id: str) -> None:
    """Render refined, editorial roadmap with smooth status transitions."""
    progress_data = roadmap_service.calculate_progress(roadmap)
    overall_pct = progress_data["overall_percentage"]
    completed_cnt = progress_data["completed_count"]
    total_cnt = progress_data["total_count"]
    in_prog_cnt = progress_data["in_progress_count"]

    # Header Card
    st.markdown(
        f"""
        <div class="tobe-hero-card">
            <span class="tobe-badge tobe-badge-green" style="margin-bottom: 8px;">Active Career Path</span>
            <div style="font-family: 'Outfit', sans-serif; font-size: 1.6rem; font-weight: 700; color: #0F172A; margin-bottom: 4px;">
                {roadmap.get('title', 'Your Personalized Roadmap')}
            </div>
            <div style="font-size: 0.92rem; color: #475569; margin-bottom: 16px;">
                {roadmap.get("description", "A structured pathway from foundational skills to portfolio development.")}
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                <div style="font-size: 0.8rem; font-weight: 600; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;">Milestone Progress</div>
                <div style="font-family: 'Outfit', sans-serif; font-size: 0.95rem; font-weight: 700; color: #0F172A;">{overall_pct}%</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.progress(overall_pct / 100.0)

    # Next Recommended Step Highlight
    next_step = roadmap_service.get_next_recommended_step(roadmap)
    if next_step:
        item = next_step["item"]
        st.markdown(
            f"""
            <div style="background: #FFFFFF; border: 1px solid #2563EB; border-left: 4px solid #2563EB; border-radius: 10px; padding: 16px 20px; margin: 16px 0 24px 0; box-shadow: 0 1px 3px rgba(37, 99, 235, 0.05);">
                <div style="font-size: 0.72rem; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    Next Priority Step &bull; {next_step['phase_title']}
                </div>
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 600; color: #0F172A; margin-bottom: 4px;">
                    {item.get('title')}
                </div>
                <div style="font-size: 0.88rem; color: #475569;">
                    {item.get('description', '')}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='font-family: Outfit, sans-serif; font-size: 1.2rem; font-weight: 600; color: #0F172A; margin: 24px 0 12px 0;'>Roadmap Phases</div>", unsafe_allow_html=True)

    # =========================================================================
    # PHASES AND TASKS
    # =========================================================================
    for p_idx, phase in enumerate(roadmap.get("phases", [])):
        p_items = phase.get("items", [])
        p_total = len(p_items)
        p_done = sum(1 for i in p_items if i.get("status") == "completed")
        p_pct = int((p_done / p_total * 100)) if p_total > 0 else 0

        is_phase_complete = (p_pct == 100 and p_total > 0)

        with st.expander(f"{phase.get('title')} &mdash; {p_done}/{p_total} Complete ({p_pct}%)", expanded=(not is_phase_complete)):
            if phase.get("description"):
                st.caption(phase.get("description"))

            for item in p_items:
                item_id = item.get("id")
                title = item.get("title")
                desc = item.get("description", "")
                status = item.get("status", "not_started")
                completed_at = item.get("completed_at")
                resources = item.get("resources", [])
                is_user_created = item.get("is_user_created", False)

                status_color = "#059669" if status == "completed" else ("#2563EB" if status == "in_progress" else "#E2E8F0")
                status_label = "Completed" if status == "completed" else ("In Progress" if status == "in_progress" else "Not Started")
                badge_class = "tobe-badge-green" if status == "completed" else ("tobe-badge-blue" if status == "in_progress" else "tobe-badge-slate")

                st.markdown(
                    f"""
                    <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-left: 3px solid {status_color}; border-radius: 8px; padding: 14px 16px; margin-bottom: 10px;">
                        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
                            <div style="font-weight: 600; font-size: 0.95rem; color: #0F172A;">
                                {title}
                            </div>
                            <span class="tobe-badge {badge_class}">{status_label}</span>
                        </div>
                        {f'<div style="font-size: 0.85rem; color: #475569; margin: 4px 0 8px 0;">{desc}</div>' if desc else ''}
                        {f'<div style="font-size: 0.75rem; color: #059669;">Completed on {format_date_human(completed_at)}</div>' if completed_at and status == "completed" else ''}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Action controls for status toggle
                btn_cols = st.columns([2.5, 1, 1])
                with btn_cols[1]:
                    if status != "completed":
                        if st.button("Mark Complete", key=f"btn_done_{p_idx}_{item_id}", type="primary", use_container_width=True):
                            roadmap_service.update_item_status(roadmap, item_id, "completed")
                            db_service.save_roadmap(user_id, roadmap)
                            st.rerun()
                    else:
                        if st.button("Reopen Step", key=f"btn_reopen_{p_idx}_{item_id}", use_container_width=True):
                            roadmap_service.update_item_status(roadmap, item_id, "in_progress")
                            db_service.save_roadmap(user_id, roadmap)
                            st.rerun()

                with btn_cols[2]:
                    if status == "not_started":
                        if st.button("Start Step", key=f"btn_start_{p_idx}_{item_id}", use_container_width=True):
                            roadmap_service.update_item_status(roadmap, item_id, "in_progress")
                            db_service.save_roadmap(user_id, roadmap)
                            st.rerun()

                # Resource links
                if resources:
                    ext_icon = get_icon("external_link", size=11, color="#2563EB")
                    res_html = "".join([f'<a href="{res.get("url", "#")}" target="_blank" style="display:inline-flex; align-items:center; gap:4px; font-size:0.78rem; font-weight:500; color:#2563EB; background:#F8FAFC; border:1px solid #E2E8F0; padding:2px 8px; border-radius:6px; text-decoration:none; margin-right:6px; margin-top:2px;">{ext_icon} {res.get("title", "Resource")}</a>' for res in resources])
                    st.markdown(f"<div style='margin-bottom:10px;'>{res_html}</div>", unsafe_allow_html=True)

    # Custom task adder
    with st.expander("Add Custom Milestone Task"):
        task_phase_idx = st.selectbox(
            "Assign to Phase:",
            options=range(len(roadmap.get("phases", []))),
            format_func=lambda i: f"Phase {i+1}: {roadmap['phases'][i]['title']}"
        )
        task_title = st.text_input("Task Title (e.g., 'Build Personal Portfolio Case Study')")
        task_desc = st.text_area("Task Description or Link")

        if st.button("Add Task", type="primary"):
            if task_title:
                roadmap_service.add_custom_item(
                    roadmap,
                    phase_index=task_phase_idx,
                    title=task_title,
                    description=task_desc
                )
                db_service.save_roadmap(user_id, roadmap)
                st.success("Task added to roadmap.")
                st.rerun()
