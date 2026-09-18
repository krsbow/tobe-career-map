"""
TOBE Contextual AI Mentor Component (Figma Design).
Appears contextually throughout the product where useful (Explore, Discover, My Path, Home).
Zero emojis, clean conversational interface.
"""

from typing import Dict, Any, List, Optional
import streamlit as st
from config import AI_MENTOR_NAME
from services.mentor_service import mentor_service

def render_tobe_contextual_card(context_title: str = "", context_prompt: str = ""):
    """Render an in-page contextual prompt for TOBE."""
    prompt_text = context_prompt or "Have a question about what you're exploring? I can help you think it through."
    
    st.markdown(
        f"""
        <div class="tobe-card" style="background: #243760; border: none; color: #FFFFFF; padding: 24px; margin: 24px 0;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <div style="width: 7px; height: 7px; border-radius: 50%; background: #7A9E8E;"></div>
                <div style="font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.6);">
                    {AI_MENTOR_NAME} &bull; Career Mentor
                </div>
            </div>
            <div style="font-family: 'Fraunces', Georgia, serif; font-size: 1.25rem; font-weight: 400; color: #FFFFFF; margin-bottom: 6px;">
                {context_title or f"Talk it through with {AI_MENTOR_NAME}"}
            </div>
            <div style="font-size: 0.9rem; color: rgba(255,255,255,0.85); line-height: 1.5; margin-bottom: 16px;">
                {prompt_text}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.expander(f"Ask {AI_MENTOR_NAME} a question"):
        render_tobe_chat_inline(user_id="user_active", context_hint=context_title)

def render_tobe_chat_inline(user_id: str = "guest", context_hint: str = ""):
    """Render embedded conversational interface with TOBE."""
    if "mentor_history" not in st.session_state:
        st.session_state["mentor_history"] = [
            {
                "role": "assistant",
                "content": f"Hi! I'm {AI_MENTOR_NAME}, your career mentor. You don't have to have everything figured out right now. What's on your mind?"
            }
        ]

    # Conversation history
    for msg in st.session_state["mentor_history"]:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class="tobe-chat-bubble-user">
                    {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="tobe-chat-bubble-ai">
                    <div style="font-size: 0.72rem; font-weight: 700; color: #243760; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.05em;">
                        {AI_MENTOR_NAME}
                    </div>
                    {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

    user_query = st.chat_input(f"Ask {AI_MENTOR_NAME} about {context_hint or 'your career path'}...", key=f"tobe_inp_{context_hint}")
    if user_query:
        st.session_state["mentor_history"].append({"role": "user", "content": user_query})
        with st.spinner(f"{AI_MENTOR_NAME} is thinking..."):
            reply = mentor_service.generate_mentor_reply(
                user_id=user_id,
                message=user_query,
                chat_history=st.session_state["mentor_history"]
            )
        st.session_state["mentor_history"].append({"role": "assistant", "content": reply})
        st.rerun()

def render_mentor_chat(user_id: str = "guest") -> None:
    """Standalone view for TOBE mentor conversation."""
    render_tobe_contextual_card(
        context_title="Chat with TOBE",
        context_prompt="Explore questions, discuss career transitions, or analyze what skills you should focus on next."
    )
