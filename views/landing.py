"""
Landing Page View for TO BE Platform.
VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design.
Hero Headline: "Explore what could be next." (with Fraunces serif italic).
No pill badge above hero.
Features: 01 Reflect / 02 Discover / 03 Chart your path, Career previews, TOBE section, and footer attribution.
"""

import streamlit as st
from config import PROJECT_NAME, AI_MENTOR_NAME
from services.career_service import career_service
from components.theme import render_footer

def render_landing_page():
    """Render Figma-accurate editorial product landing page."""
    
    # =========================================================================
    # HEADER
    # =========================================================================
    col_logo, col_nav, col_actions = st.columns([2, 3, 2])
    
    with col_logo:
        st.markdown(
            f"""
            <div style="font-family: 'Fraunces', Georgia, serif; fontSize: 20px; font-weight: 500; color: #243760; letter-spacing: -0.03em; padding-top: 6px;">
                {PROJECT_NAME}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_nav:
        st.markdown(
            """
            <div style="display: flex; justify-content: center; gap: 24px; padding-top: 10px; font-size: 14px; font-weight: 500; color: #6B7080;">
                <span>What to be &bull; Why to be &bull; How to be</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_actions:
        c_log, c_start = st.columns([1, 1.4])
        with c_log:
            if st.button("Log In", key="land_hdr_login", use_container_width=True):
                st.session_state["view_mode"] = "auth"
                st.session_state["auth_mode"] = "login"
                st.rerun()
        with c_start:
            if st.button("Start Exploring", key="land_hdr_start", type="primary", use_container_width=True):
                st.session_state["view_mode"] = "auth"
                st.session_state["auth_mode"] = "signup"
                st.rerun()

    st.markdown("<div style='margin-top: 64px;'></div>", unsafe_allow_html=True)

    # =========================================================================
    # HERO SECTION (Figma layout)
    # =========================================================================
    st.markdown(
        """
        <div style="text-align: center; max-width: 780px; margin: 0 auto 36px auto;">
            <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: clamp(40px, 6.5vw, 76px); font-weight: 400; color: #1A1F2E; line-height: 1.06; letter-spacing: -0.03em; margin-bottom: 24px;">
                Explore what could<br />
                <em style="color: #243760; font-style: italic;">be next.</em>
            </h1>
            <p style="font-size: 18px; color: #6B7080; max-width: 520px; margin: 0 auto 40px auto; line-height: 1.7; font-weight: 400;">
                Discover careers that connect with your interests, skills, and goals. Understand what they involve, then build a path toward the ones you want to explore.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Hero CTAs
    c_h1, c_space, c_h2 = st.columns([1.2, 0.2, 1.2])
    with c_h1:
        if st.button("Start Exploring", key="hero_start_btn", type="primary", use_container_width=True):
            st.session_state["view_mode"] = "auth"
            st.session_state["auth_mode"] = "signup"
            st.rerun()
    with c_h2:
        if st.button("Explore Careers", key="hero_browse_btn", use_container_width=True):
            st.session_state["is_authenticated"] = True
            st.session_state["nav_page"] = "Explore"
            st.session_state["view_mode"] = "app"
            st.rerun()

    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

    # =========================================================================
    # WHAT / WHY / HOW (3 Core Pillars)
    # =========================================================================
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 36px;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B7080; margin-bottom: 8px;">
                The TO BE Philosophy
            </p>
            <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 32px; font-weight: 400; color: #1A1F2E; letter-spacing: -0.02em;">
                Three questions that shape your journey
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_w1, col_w2, col_w3 = st.columns(3)

    with col_w1:
        st.markdown(
            """
            <div class="tobe-card" style="height: 220px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 12px; font-weight: 700; color: #243760; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 8px;">
                        Discover &bull; 01
                    </div>
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 8px;">
                        WHAT TO BE
                    </div>
                    <div style="font-size: 14px; color: #6B7080; line-height: 1.6;">
                        Explore possible careers based on your interests, skills, strengths, and goals without being pigeonholed into a single track.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_w2:
        st.markdown(
            """
            <div class="tobe-card" style="height: 220px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 12px; font-weight: 700; color: #7A9E8E; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 8px;">
                        Explore &bull; 02
                    </div>
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 8px;">
                        WHY TO BE
                    </div>
                    <div style="font-size: 14px; color: #6B7080; line-height: 1.6;">
                        Understand what a career actually involves, explore salary benchmarks, and see why a path might connect with you.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_w3:
        st.markdown(
            """
            <div class="tobe-card" style="height: 220px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 12px; font-weight: 700; color: #5B7FA6; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 8px;">
                        My Path &bull; 03
                    </div>
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 20px; font-weight: 500; color: #1A1F2E; margin-bottom: 8px;">
                        HOW TO BE
                    </div>
                    <div style="font-size: 14px; color: #6B7080; line-height: 1.6;">
                        Discover the skills, curated tutorials, milestone projects, and step-by-step preparation to move toward your goals.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

    # =========================================================================
    # HOW IT WORKS (01 Reflect, 02 Discover, 03 Chart your path)
    # =========================================================================
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 36px;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B7080; margin-bottom: 8px;">
                How It Works
            </p>
            <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 32px; font-weight: 400; color: #1A1F2E; letter-spacing: -0.02em;">
                A guided, transparent process
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    s1, s2, s3 = st.columns(3)
    steps_data = [
        ("01", "Reflect", "Answer thoughtful questions about your interests, values, and working style. No rigid tests or labels."),
        ("02", "Discover", "Explore careers curated to you with realistic salary benchmarks, day-in-the-life stories, and growth outlooks."),
        ("03", "Chart your path", f"Build a step-by-step plan, track milestones, and receive grounded mentorship from {AI_MENTOR_NAME}.")
    ]
    cols = [s1, s2, s3]
    for idx, (num, title, desc) in enumerate(steps_data):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="tobe-card" style="height: 180px;">
                    <div style="font-family: 'Fraunces', Georgia, serif; font-size: 22px; color: #243760; margin-bottom: 4px;">{num}</div>
                    <div style="font-size: 16px; font-weight: 600; color: #1A1F2E; margin-bottom: 6px;">{title}</div>
                    <div style="font-size: 14px; color: #6B7080; line-height: 1.5;">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

    # =========================================================================
    # CAREER EXPLORATION PREVIEW
    # =========================================================================
    st.markdown(
        """
        <div style="margin-bottom: 28px;">
            <p style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B7080; margin-bottom: 4px;">
                Catalog Preview
            </p>
            <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 28px; font-weight: 400; color: #1A1F2E; letter-spacing: -0.02em;">
                Every path worth considering
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    preview_careers = career_service.get_all_careers()[:3]
    p1, p2, p3 = st.columns(3)
    p_cols = [p1, p2, p3]
    for idx, c in enumerate(preview_careers):
        with p_cols[idx]:
            skills_html = "".join([f'<span class="tobe-chip">{s}</span>' for s in c.get("core_skills", [])[:3]])
            st.markdown(
                f"""
                <div class="tobe-card" style="height: 250px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span class="tobe-badge tobe-badge-slate">{c.get('category_name')}</span>
                            <span style="font-size: 12px; font-weight: 600; color: #243760;">94% Match</span>
                        </div>
                        <div style="font-family: 'Fraunces', Georgia, serif; font-size: 18px; font-weight: 500; color: #1A1F2E; margin-bottom: 4px;">
                            {c.get('title')}
                        </div>
                        <div style="font-size: 13px; color: #6B7080; line-height: 1.5; margin-bottom: 12px;">
                            {c.get('tagline', '')}
                        </div>
                    </div>
                    <div>
                        <div style="margin-bottom: 4px;">{skills_html}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

    # =========================================================================
    # TOBE AI MENTOR PREVIEW (Figma layout)
    # =========================================================================
    st.markdown(
        f"""
        <div class="tobe-card" style="background: #243760; border: none; color: #FFFFFF; padding: 40px 36px;">
            <div style="max-width: 640px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                    <div style="width: 7px; height: 7px; border-radius: 50%; background: #7A9E8E;"></div>
                    <span style="font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.6);">
                        {AI_MENTOR_NAME} &bull; Career Mentor
                    </span>
                </div>
                <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 30px; font-weight: 400; color: #FFFFFF; line-height: 1.2; margin-bottom: 14px;">
                    A thoughtful companion for your questions
                </h2>
                <p style="font-size: 15px; color: rgba(255,255,255,0.85); line-height: 1.65; margin-bottom: 24px;">
                    {AI_MENTOR_NAME} helps you talk through trade-offs, explore what day-to-day work actually feels like, and navigate next steps without judgment or pressure.
                </p>
            </div>
            <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.14); border-radius: 6px; padding: 14px 18px; font-size: 14px; color: rgba(255,255,255,0.9); font-style: italic; max-width: 580px;">
                &ldquo;I'm drawn to both UX Design and Data Analytics. How can I explore which day-to-day work suits me better?&rdquo;
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================================================================
    # FINAL CTA
    # =========================================================================
    st.markdown(
        """
        <div style="text-align: center; padding: 64px 0 24px 0;">
            <h2 style="font-family: 'Fraunces', Georgia, serif; font-size: 36px; font-weight: 400; color: #1A1F2E; margin-bottom: 12px;">
                Ready to explore what could be next?
            </h2>
            <p style="font-size: 16px; color: #6B7080; margin-bottom: 28px;">
                Start with a 5-minute discovery quiz or browse our comprehensive career catalog.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    c_f1, c_fspace, c_f2 = st.columns([1.2, 0.2, 1.2])
    with c_f1:
        if st.button("Start Discovery Assessment", key="cta_start_btn", type="primary", use_container_width=True):
            st.session_state["view_mode"] = "auth"
            st.session_state["auth_mode"] = "signup"
            st.rerun()
    with c_f2:
        if st.button("Browse Catalog", key="cta_browse_btn", use_container_width=True):
            st.session_state["is_authenticated"] = True
            st.session_state["nav_page"] = "Explore"
            st.session_state["view_mode"] = "app"
            st.rerun()

    # Footer attribution
    render_footer()
