"""
Compare Page View for TO BE Platform.
Side-by-side career comparison with clean visual indicators and zero emojis.
"""

import streamlit as st
from services.career_service import career_service
from components.icons import get_icon

def render_compare_page():
    """Render side-by-side career comparison."""
    compare_icon = get_icon("compare", size=22, color="#2563EB")
    dollar_icon = get_icon("dollar", size=14, color="#059669")
    check_icon = get_icon("check", size=14, color="#2563EB")

    all_careers = career_service.get_all_careers()
    career_titles = [c["title"] for c in all_careers]

    # Selected defaults
    c1_default = st.session_state.get("compare_career_1")
    c1_idx = 0
    if c1_default:
        for idx, c in enumerate(all_careers):
            if c["id"] == c1_default:
                c1_idx = idx
                break

    c2_idx = 1 if len(all_careers) > 1 else 0

    st.markdown(
        f"""
        <div class="tobe-hero-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                {compare_icon}
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.6rem; font-weight: 800; color: #0F172A;">
                    Compare Career Paths
                </div>
            </div>
            <div style="font-size: 0.95rem; color: #475569;">
                Evaluate differences in day-to-day responsibilities, skill stacks, salary benchmarks, and portfolio expectations.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Selectors
    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        sel_c1_title = st.selectbox("Select First Career:", career_titles, index=c1_idx, key="sel_comp_1")
    with col_sel2:
        sel_c2_title = st.selectbox("Select Second Career:", career_titles, index=c2_idx, key="sel_comp_2")

    c1 = next((c for c in all_careers if c["title"] == sel_c1_title), None)
    c2 = next((c for c in all_careers if c["title"] == sel_c2_title), None)

    if not c1 or not c2:
        return

    # Comparison Grid Cards
    st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True)
    comp_col1, comp_col2 = st.columns(2)

    def render_career_comp_card(career):
        c_id = career.get("id")
        category = career.get("category_name", "Tech")
        title = career.get("title", "")
        tagline = career.get("tagline", "")
        skills = career.get("core_skills", [])
        tools = career.get("tools_and_technologies", [])
        salary = career.get("salary_data", {}).get("philippines", {}).get("mid_level", "Competitive")
        what_you_do = career.get("what_you_will_do", [])

        st.markdown(
            f"""
            <div class="tobe-card">
                <span class="tobe-badge tobe-badge-blue" style="margin-bottom: 6px;">{category}</span>
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.4rem; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
                    {title}
                </div>
                <div style="font-size: 0.88rem; color: #64748B; margin-bottom: 14px;">
                    {tagline}
                </div>
                
                <div style="font-weight: 700; font-size: 0.82rem; color: #64748B; text-transform: uppercase; margin-bottom: 6px;">PHILIPPINES MID-LEVEL SALARY</div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #059669; margin-bottom: 14px;">
                    {salary}
                </div>

                <div style="font-weight: 700; font-size: 0.82rem; color: #64748B; text-transform: uppercase; margin-bottom: 6px;">CORE SKILLS</div>
                <div style="margin-bottom: 14px;">
                    {"".join([f'<span class="tobe-chip">{s}</span>' for s in skills[:5]])}
                </div>

                <div style="font-weight: 700; font-size: 0.82rem; color: #64748B; text-transform: uppercase; margin-bottom: 6px;">PRIMARY TOOLS</div>
                <div style="margin-bottom: 14px;">
                    {"".join([f'<span class="tobe-badge tobe-badge-purple" style="margin-right:4px; margin-bottom:4px;">{t}</span>' for t in tools[:4]])}
                </div>

                <div style="font-weight: 700; font-size: 0.82rem; color: #64748B; text-transform: uppercase; margin-bottom: 6px;">WHAT YOU DO</div>
                {"".join([f'<div style="font-size:0.85rem; color:#334155; margin-bottom:4px; display:flex; gap:6px;">{check_icon} <span>{w}</span></div>' for w in what_you_do[:3]])}
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(f"Generate Roadmap for {title}", key=f"comp_road_{c_id}", type="primary", use_container_width=True):
            st.session_state["target_career_id"] = c_id
            st.session_state["nav_page"] = "My Path"
            st.rerun()

    with comp_col1:
        render_career_comp_card(c1)

    with comp_col2:
        render_career_comp_card(c2)
