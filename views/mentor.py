"""
Mentor Page View for TO BE Platform.
AI Career Mentor (TOBE) interface with zero emojis.
"""

import streamlit as st
from services.auth import auth_service
from components.mentor_ui import render_mentor_chat

def render_mentor_page():
    """Render the AI Mentor (TOBE) page."""
    user = auth_service.get_current_user()
    user_id = user["id"] if user else "guest"
    render_mentor_chat(user_id=user_id)
