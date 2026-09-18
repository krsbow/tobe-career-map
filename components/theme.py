"""
Theme and Global Style Engine for TO BE Platform.
EXACT VISUAL SOURCE OF TRUTH: Recreated from Figma Make project design.
Typography: 'Fraunces' (display serif) + 'Instrument Sans' (body sans).
Palette: Warm White #F9F8F5, Navy #243760, Slate #5B7FA6, Sage #7A9E8E, Border #E4E2DB.
Radius: 6px, Refined editorial styling, subtle micro-motion, zero emojis.
Includes 'created by krsbow' attribution.
"""

import streamlit as st
from config import PROJECT_NAME

def inject_global_theme():
    """Inject Figma-accurate CSS stylesheet."""
    st.markdown(
        """
        <style>
        /* Import Figma fonts */
        @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,300;1,9..144,400&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');

        :root {
            --background: #F9F8F5;
            --foreground: #1A1F2E;
            --card: #FFFFFF;
            --primary: #243760;
            --primary-hover: #1A2846;
            --secondary: #EEF1F8;
            --muted: #F0EFE9;
            --muted-foreground: #6B7080;
            --accent-sage: #7A9E8E;
            --border: #E4E2DB;
            --ring: #5B7FA6;
            --radius: 6px;
            --font-display: 'Fraunces', Georgia, serif;
            --font-body: 'Instrument Sans', system-ui, sans-serif;
        }

        html, body, [class*="css"], [class*="st-"] {
            font-family: var(--font-body) !important;
            color: var(--foreground) !important;
            background-color: var(--background) !important;
            -webkit-font-smoothing: antialiased;
        }

        /* Suppress default Streamlit sidebar */
        [data-testid="stSidebar"], section[data-testid="stSidebarNav"], [data-testid="stSidebarNavItems"] {
            display: none !important;
            visibility: hidden !important;
            width: 0px !important;
            margin: 0px !important;
            padding: 0px !important;
        }

        /* Streamlit main block container */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 4rem !important;
            max-width: 1140px !important;
        }

        /* Headings - Fraunces Serif */
        h1, h2, h3, h4, .display-font {
            font-family: var(--font-display) !important;
            font-weight: 400 !important;
            color: var(--foreground) !important;
            letter-spacing: -0.025em !important;
            line-height: 1.15 !important;
        }

        /* Smooth reveal animation */
        @keyframes subtleFadeUp {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .stApp {
            background-color: var(--background) !important;
            animation: subtleFadeUp 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        /* Figma Editorial Cards */
        .tobe-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 24px;
            margin-bottom: 16px;
            transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .tobe-card:hover {
            border-color: #CBD5E1;
            box-shadow: 0 6px 20px rgba(26, 31, 46, 0.05);
            transform: translateY(-2px);
        }

        /* Minimal Hero Card */
        .tobe-hero-card {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 36px 32px;
            margin-bottom: 28px;
            box-shadow: 0 2px 8px rgba(26, 31, 46, 0.03);
            position: relative;
        }

        /* Editorial Badges & Pills */
        .tobe-badge {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 3px 10px;
            border-radius: var(--radius);
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }
        .tobe-badge-navy {
            background-color: var(--secondary);
            color: var(--primary);
            border: 1px solid #D6DFEE;
        }
        .tobe-badge-sage {
            background-color: #F0F6F3;
            color: #466958;
            border: 1px solid #D2E4DC;
        }
        .tobe-badge-slate {
            background-color: #F0EFE9;
            color: #6B7080;
            border: 1px solid #E4E2DB;
        }

        /* Skill Chips */
        .tobe-chip {
            display: inline-block;
            background: #F0EFE9;
            color: #243760;
            font-size: 0.78rem;
            font-weight: 500;
            padding: 3px 10px;
            border-radius: 4px;
            border: 1px solid #E4E2DB;
            margin-right: 5px;
            margin-bottom: 5px;
        }

        /* Figma Native Button Overrides */
        div.stButton > button {
            border-radius: var(--radius) !important;
            font-family: var(--font-body) !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            padding: 0.55rem 1.25rem !important;
            border: 1px solid var(--border) !important;
            background-color: #FFFFFF !important;
            color: var(--foreground) !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
            cursor: pointer !important;
        }
        div.stButton > button:hover {
            border-color: var(--foreground) !important;
            transform: translateY(-1px) !important;
        }
        div.stButton > button[kind="primary"] {
            background-color: var(--primary) !important;
            color: #FFFFFF !important;
            border: 1px solid var(--primary) !important;
        }
        div.stButton > button[kind="primary"]:hover {
            background-color: var(--primary-hover) !important;
            border-color: var(--primary-hover) !important;
            box-shadow: 0 4px 14px rgba(36, 55, 96, 0.2) !important;
        }

        /* Top Radio Navigation Bar */
        div[role="radiogroup"] {
            display: flex !important;
            flex-wrap: wrap !important;
            justify-content: flex-start !important;
            gap: 4px !important;
            background: transparent !important;
            padding: 0px !important;
            border: none !important;
        }
        div[role="radiogroup"] label {
            background: transparent !important;
            border-radius: var(--radius) !important;
            padding: 6px 14px !important;
            font-weight: 500 !important;
            font-size: 0.88rem !important;
            color: var(--muted-foreground) !important;
            border: 1px solid transparent !important;
            transition: all 0.2s ease !important;
            cursor: pointer !important;
        }
        div[role="radiogroup"] label:hover {
            color: var(--foreground) !important;
        }
        div[role="radiogroup"] label:has(input:checked) {
            background: var(--secondary) !important;
            color: var(--primary) !important;
            border: 1px solid #D6DFEE !important;
            font-weight: 600 !important;
        }

        /* Progress Bar (Navy line) */
        .stProgress > div > div > div > div {
            background-color: var(--primary) !important;
            border-radius: 2px !important;
        }
        .stProgress > div > div > div {
            background-color: var(--border) !important;
            border-radius: 2px !important;
            height: 4px !important;
        }

        /* Minimal Chat Bubbles */
        .tobe-chat-bubble-user {
            background-color: var(--primary);
            color: #FFFFFF;
            border-radius: 8px 8px 2px 8px;
            padding: 12px 18px;
            margin-left: auto;
            max-width: 80%;
            margin-bottom: 12px;
            font-size: 0.92rem;
            line-height: 1.5;
        }
        .tobe-chat-bubble-ai {
            background-color: #FFFFFF;
            color: var(--foreground);
            border: 1px solid var(--border);
            border-radius: 8px 8px 8px 2px;
            padding: 16px 20px;
            margin-right: auto;
            max-width: 85%;
            margin-bottom: 14px;
            font-size: 0.92rem;
            line-height: 1.6;
            box-shadow: 0 1px 4px rgba(26, 31, 46, 0.02);
        }

        /* Footer */
        .tobe-footer {
            text-align: center;
            padding: 48px 0 16px 0;
            margin-top: 64px;
            border-top: 1px solid var(--border);
            color: var(--muted-foreground);
            font-size: 0.82rem;
        }
        .tobe-footer-tag {
            display: inline-block;
            background: var(--muted);
            color: var(--muted-foreground);
            padding: 3px 12px;
            border-radius: var(--radius);
            font-size: 0.78rem;
            font-weight: 500;
            border: 1px solid var(--border);
            margin-top: 8px;
            letter-spacing: 0.02em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def render_footer():
    """Render minimal, elegant footer with 'created by krsbow'."""
    st.markdown(
        f"""
        <div class="tobe-footer">
            <div style="font-family: var(--font-display); font-size: 1.1rem; color: #243760; margin-bottom: 4px;">{PROJECT_NAME}</div>
            <div style="color: #6B7080; margin-bottom: 8px;">What to be. Why to be. How to be.</div>
            <div class="tobe-footer-tag">created by krsbow</div>
        </div>
        """,
        unsafe_allow_html=True
    )
