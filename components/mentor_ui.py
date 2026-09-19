"""
TOBE Guided Career Mentor Component (Streamlit Counterpart).
Provides structured, natural question choices across WHAT / WHY / HOW / PRACTICAL.
Zero UI category labels, zero headings above questions, zero completion cards, zero free-text chat input, zero emojis.
"""

from typing import Dict, Any, List, Optional
import streamlit as st
from config import AI_MENTOR_NAME
from services.guided_mentor import guided_mentor
from data.seed_data import CAREERS_SEED

def render_tobe_contextual_card(context_title: str = "", context_prompt: str = "", career_id: str = ""):
    """Render an in-page contextual prompt for TOBE."""
    prompt_text = context_prompt or "Explore questions and next steps with your career mentor."
    
    st.markdown(
        f"""
        <div class="tobe-card" style="background: #243760; border: none; color: #FFFFFF; padding: 24px; margin: 24px 0; border-radius: 12px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <div style="width: 7px; height: 7px; border-radius: 50%; background: #7A9E8E;"></div>
                <div style="font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.6);">
                    {AI_MENTOR_NAME} &bull; Career Mentor
                </div>
            </div>
            <div style="font-family: 'Fraunces', Georgia, serif; font-size: 1.25rem; font-weight: 400; color: #FFFFFF; margin-bottom: 6px;">
                {context_title or f"Explore with {AI_MENTOR_NAME}"}
            </div>
            <div style="font-size: 0.9rem; color: rgba(255,255,255,0.85); line-height: 1.5; margin-bottom: 16px;">
                {prompt_text}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.expander(f"Explore with {AI_MENTOR_NAME}"):
        render_guided_mentor_inline(career_id=career_id)

def render_guided_mentor_inline(career_id: str = ""):
    """Render structured guided mentor interface with natural question buttons without chat input or completion cards."""
    career = guided_mentor.get_career(career_id) or CAREERS_SEED[0]
    
    if "guided_history" not in st.session_state or st.session_state.get("guided_career_id") != career["id"]:
        st.session_state["guided_career_id"] = career["id"]
        st.session_state["guided_explored"] = []
        st.session_state["guided_history"] = [
            {
                "role": "assistant",
                "content": f"Hi! I'm {AI_MENTOR_NAME}, your career mentor. Let's explore the {career['title']} pathway together."
            }
        ]

    # Render History Turns
    for msg in st.session_state["guided_history"]:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class="tobe-chat-bubble-user" style="background: #243760; color: white; padding: 14px 18px; border-radius: 12px; margin: 10px 0; max-width: 85%; margin-left: auto;">
                    <div>{msg["content"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="tobe-chat-bubble-ai" style="background: #F8F9FA; border: 1px solid #E5E7EB; color: #1A1F2E; padding: 16px 20px; border-radius: 12px; margin: 10px 0; max-width: 85%;">
                    <div style="font-size: 0.72rem; font-weight: 700; color: #243760; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.05em;">
                        {AI_MENTOR_NAME}
                    </div>
                    <div style="white-space: pre-line; line-height: 1.6;">{msg["content"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    explored = st.session_state.get("guided_explored", [])
    next_questions = guided_mentor.get_next_questions(career, explored)

    # Natural Question Buttons (No headings, No category badges)
    if next_questions:
        cols = st.columns(min(len(next_questions), 3))
        for idx, q_def in enumerate(next_questions):
            col = cols[idx % len(cols)]
            with col:
                btn_label = q_def['question']
                if st.button(btn_label, key=f"btn_q_{career['id']}_{q_def['intent']}_{idx}", use_container_width=True):
                    # Append User Turn
                    st.session_state["guided_history"].append({
                        "role": "user",
                        "content": q_def["question"]
                    })
                    # Append AI Grounded Turn
                    answer = q_def["answer"]
                    st.session_state["guided_history"].append({
                        "role": "assistant",
                        "content": answer
                    })
                    st.session_state["guided_explored"].append(q_def["intent"])
                    st.rerun()

def render_mentor_chat(user_id: str = "guest") -> None:
    """Standalone view for TOBE guided mentor conversation."""
    selected_career_id = st.selectbox(
        "Select Career to Explore with TOBE:",
        options=[c["id"] for c in CAREERS_SEED],
        format_func=lambda cid: next((f"{c['title']} ({c.get('category_name', c['field'])})" for c in CAREERS_SEED if c["id"] == cid), cid)
    )
    render_guided_mentor_inline(career_id=selected_career_id)
