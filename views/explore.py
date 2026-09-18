"""
Explore Page View for TO BE Platform.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design (Explore.tsx).
Header: "Every path worth considering."
"""

import streamlit as st
from services.career_service import career_service
from components.career_card import render_career_card
from components.mentor_ui import render_tobe_contextual_card

def render_explore_page():
    """Render Figma-styled career catalog and deep-dive views."""
    selected_career_id = st.session_state.get("selected_explore_career_id")
    if selected_career_id:
        render_career_detail_view(selected_career_id)
        return

    # Header
    st.markdown(
        """
        <div style="margin-bottom: 32px;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B7080; margin-bottom: 8px;">
                Explore
            </p>
            <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: clamp(28px, 4.5vw, 44px); font-weight: 400; letter-spacing: -0.025em; color: #1A1F2E; margin-bottom: 20px;">
                Every path worth considering.
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Search & Category Filters
    c1, c2 = st.columns([2, 1])
    with c1:
        search_query = st.text_input("Search careers or skills...", "")
    with c2:
        categories = ["All Categories"] + career_service.get_all_categories()
        selected_cat = st.selectbox("Category Filter", categories)

    cat_filter = None if selected_cat == "All Categories" else selected_cat
    careers = career_service.search_careers(query=search_query, category=cat_filter)

    st.markdown(f"<div style='font-size:13px; font-weight:600; color:#6B7080; text-transform:uppercase; letter-spacing:0.04em; margin: 20px 0 16px 0;'>Showing {len(careers)} Career Paths</div>", unsafe_allow_html=True)

    if not careers:
        st.info("No careers matched your search criteria.")
        return

    for c in careers:
        render_career_card(c, key_prefix="exp_list")

def render_career_detail_view(career_id: str):
    """Render full editorial deep-dive profile for a career."""
    career = career_service.get_career_by_id(career_id)
    if not career:
        st.error("Career not found.")
        if st.button("Return to Career Catalog"):
            st.session_state["selected_explore_career_id"] = None
            st.rerun()
        return

    if st.button("← Back to All Careers", key="back_to_catalog"):
        st.session_state["selected_explore_career_id"] = None
        st.rerun()

    title = career.get("title", "Career Profile")
    category = career.get("category_name", "Technology")
    tagline = career.get("tagline", "")
    overview = career.get("overview", "")
    what_you_will_do = career.get("what_you_will_do", [])
    core_skills = career.get("core_skills", [])
    tools = career.get("tools_and_technologies", [])
    salary_data = career.get("salary_data", {})
    education = career.get("education_and_training", {})
    portfolio = career.get("portfolio_and_projects", [])
    sources = career.get("sources_and_references", [])

    st.markdown(
        f"""
        <div class="tobe-hero-card" style="margin-top: 16px;">
            <span class="tobe-badge tobe-badge-navy" style="margin-bottom: 8px;">{category}</span>
            <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: 38px; font-weight: 400; color: #1A1F2E; margin-bottom: 8px;">
                {title}
            </h1>
            <p style="font-size: 16px; color: #6B7080; line-height: 1.6; margin-bottom: 20px;">
                {tagline}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # CTA Bar
    if st.button(f"Build Roadmap for {title}", type="primary", use_container_width=True):
        st.session_state["target_career_id"] = career_id
        st.session_state["nav_page"] = "My Path"
        st.rerun()

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    # Contextual TOBE prompt for this specific career
    render_tobe_contextual_card(
        context_title=f"Curious about {title}?",
        context_prompt=f"Ask TOBE about the real day-to-day work, entry requirements, or how to start preparing for a role in {title}."
    )

    t1, t2, t3, t4 = st.tabs(["Overview & Day-to-Day", "Skills & Tool Stack", "Salary & Education", "Portfolio Projects & Sources"])

    with t1:
        st.markdown(
            f"""
            <div class="tobe-card">
                <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 8px;">
                    Role Overview
                </div>
                <div style="font-size: 15px; color: #1A1F2E; line-height: 1.65;">
                    {overview}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if what_you_will_do:
            st.markdown(
                f"""
                <div class="tobe-card">
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 12px;">
                        What You Will Do Day-to-Day
                    </div>
                    {"".join([f'<div style="font-size:14px; color:#1A1F2E; margin-bottom:8px; line-height:1.5;">&bull; {item}</div>' for item in what_you_will_do])}
                </div>
                """,
                unsafe_allow_html=True
            )

    with t2:
        st.markdown(
            f"""
            <div class="tobe-card">
                <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 12px;">
                    Core Competencies & Skills
                </div>
                <div>
                    {"".join([f'<span class="tobe-chip">{s}</span>' for s in core_skills])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if tools:
            st.markdown(
                f"""
                <div class="tobe-card">
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 12px;">
                        Modern Tool Stack
                    </div>
                    <div>
                        {"".join([f'<span class="tobe-badge tobe-badge-navy" style="margin-right:6px; margin-bottom:6px;">{t}</span>' for t in tools])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    with t3:
        ph_salary = salary_data.get("philippines", {})
        us_salary = salary_data.get("global_remote_usd", {})

        st.markdown(
            f"""
            <div class="tobe-card">
                <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 14px;">
                    Salary Benchmarks
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div style="background: #F9F8F5; border: 1px solid #E4E2DB; padding: 16px; border-radius: 6px;">
                        <div style="font-size: 12px; font-weight: 700; color: #6B7080;">PHILIPPINES (PHP/MO)</div>
                        <div style="font-size: 14px; color: #1A1F2E; margin-top: 6px;">Entry: <strong>{ph_salary.get('entry_level', 'Competitive')}</strong></div>
                        <div style="font-size: 14px; color: #1A1F2E;">Mid: <strong>{ph_salary.get('mid_level', 'Competitive')}</strong></div>
                        <div style="font-size: 14px; color: #1A1F2E;">Senior: <strong>{ph_salary.get('senior', 'Competitive')}</strong></div>
                    </div>
                    <div style="background: #F9F8F5; border: 1px solid #E4E2DB; padding: 16px; border-radius: 6px;">
                        <div style="font-size: 12px; font-weight: 700; color: #6B7080;">GLOBAL / REMOTE (USD/YR)</div>
                        <div style="font-size: 14px; color: #1A1F2E; margin-top: 6px;">Entry: <strong>{us_salary.get('entry_level', 'Competitive')}</strong></div>
                        <div style="font-size: 14px; color: #1A1F2E;">Mid: <strong>{us_salary.get('mid_level', 'Competitive')}</strong></div>
                        <div style="font-size: 14px; color: #1A1F2E;">Senior: <strong>{us_salary.get('senior', 'Competitive')}</strong></div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if education:
            st.markdown(
                f"""
                <div class="tobe-card">
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 8px;">
                        Education & Pathways
                    </div>
                    <div style="font-size: 14px; color: #1A1F2E; line-height: 1.6;">
                        <strong>Typical Degree:</strong> {education.get('degree_relevance', 'Self-taught or Computer Science/Design')}<br>
                        <strong>Alternative Pathway:</strong> {education.get('alternative_pathways', 'Self-taught portfolio, community projects')}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    with t4:
        if portfolio:
            st.markdown(
                f"""
                <div class="tobe-card">
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 12px;">
                        Recommended Portfolio Projects
                    </div>
                    {"".join([f'<div style="background:#F9F8F5; border:1px solid #E4E2DB; padding:12px 16px; border-radius:6px; margin-bottom:8px;"><div style="font-weight:600; font-size:15px; color:#1A1F2E;">{p.get("title", "Project")}</div><div style="font-size:13px; color:#6B7080; margin-top:2px;">{p.get("description", "")}</div></div>' for p in portfolio])}
                </div>
                """,
                unsafe_allow_html=True
            )

        if sources:
            st.markdown(
                f"""
                <div class="tobe-card">
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 18px; font-weight: 500; color: #1A1F2E; margin-bottom: 8px;">
                        Industry Benchmarks & Sources
                    </div>
                    {"".join([f'<div style="font-size:13px; color:#6B7080; margin-bottom:4px;">&bull; {s}</div>' for s in sources])}
                </div>
                """,
                unsafe_allow_html=True
            )
