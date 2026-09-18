"""
Career Profile visualization component for TO BE.
Visualizes RIASEC interest dimensions, strengths, current skills, and priorities.
Clean rounded card layouts, radar chart, zero emojis.
"""

from typing import Dict, Any
import streamlit as st
import plotly.graph_objects as go
from components.icons import get_icon

def render_career_profile(profile_data: Dict[str, Any]) -> None:
    """Render comprehensive Career Profile summary with friendly visual cards."""
    riasec_scores = profile_data.get("riasec_scores", {})
    strengths = profile_data.get("strengths", [])
    skills = profile_data.get("current_skills", [])
    priorities = profile_data.get("career_priorities", [])
    work_prefs = profile_data.get("work_preferences", [])

    sparkles_icon = get_icon("sparkles", size=18, color="#2563EB")
    target_icon = get_icon("target", size=18, color="#059669")
    bookmark_icon = get_icon("bookmark", size=18, color="#D97706")

    st.markdown(
        f"""
        <div class="tobe-hero-card">
            <div style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700; color: #0F172A; margin-bottom: 6px;">
                Your Career Discovery Profile
            </div>
            <div style="font-size: 0.95rem; color: #475569; line-height: 1.5;">
                This structured profile reflects your current balance of interests, strengths, and work styles. It is designed to guide exploration, not confine you to a single track.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            f"""
            <div style="font-weight: 700; font-size: 1.05rem; color: #0F172A; display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                {target_icon} <span>Interest Dimensions (RIASEC)</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Radar Chart for RIASEC
        dim_labels = ["Realistic<br>(Hands-on)", "Investigative<br>(Analytical)", "Artistic<br>(Creative)", 
                      "Social<br>(Empathy)", "Enterprising<br>(Leadership)", "Conventional<br>(Structured)"]
        dim_keys = ["R", "I", "A", "S", "E", "C"]
        scores = [riasec_scores.get(k, {}).get("score", 15) for k in dim_keys]
        
        # Close radar loop
        r_vals = scores + [scores[0]]
        theta_vals = dim_labels + [dim_labels[0]]

        fig = go.Figure(
            data=[
                go.Scatterpolar(
                    r=r_vals,
                    theta=theta_vals,
                    fill='toself',
                    fillcolor='rgba(37, 99, 235, 0.18)',
                    line=dict(color='#2563EB', width=2.5),
                    name='Interest Level'
                )
            ]
        )
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=9, color="#94A3B8")),
                angularaxis=dict(tickfont=dict(size=11, color="#334155", family="Plus Jakarta Sans, sans-serif"))
            ),
            showlegend=False,
            margin=dict(l=40, r=40, t=20, b=20),
            height=300,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(
            f"""
            <div style="font-weight: 700; font-size: 1.05rem; color: #0F172A; display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                {sparkles_icon} <span>Core Strengths & Priorities</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if strengths:
            check_icon = get_icon("check", size=14, color="#2563EB")
            strengths_html = "".join([f'<div style="display:flex; align-items:center; gap:8px; font-size:0.9rem; color:#1E293B; margin-bottom:6px;">{check_icon} <strong>{s}</strong></div>' for s in strengths])
            st.markdown(strengths_html, unsafe_allow_html=True)

        if priorities:
            st.markdown("<div style='margin-top: 14px; font-weight:600; font-size:0.85rem; color:#64748B;'>CAREER PRIORITIES</div>", unsafe_allow_html=True)
            priorities_html = "".join([f'<span class="tobe-badge tobe-badge-amber" style="margin-right:6px; margin-top:6px;">{p}</span>' for p in priorities])
            st.markdown(f"<div style='margin-bottom:12px;'>{priorities_html}</div>", unsafe_allow_html=True)

        if work_prefs:
            st.markdown("<div style='margin-top: 10px; font-weight:600; font-size:0.85rem; color:#64748B;'>WORK STYLE PREFERENCES</div>", unsafe_allow_html=True)
            for wp in work_prefs:
                st.markdown(f"<div style='font-size:0.85rem; color:#475569;'>• {wp}</div>", unsafe_allow_html=True)

    # Skills section
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="tobe-card">
            <div style="font-weight: 700; font-size: 1rem; color: #0F172A; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
                {bookmark_icon} <span>Current Skills & Tools You Know</span>
            </div>
            {"".join([f'<span class="tobe-chip">{s}</span>' for s in skills]) if skills else '<div style="font-size:0.85rem; color:#64748B;">No prior technical tools logged yet—which is great! You can start from beginner foundations.</div>'}
        </div>
        """,
        unsafe_allow_html=True
    )
