"""
Discover Page View for TO BE Platform.
Conversational, multi-step career discovery assessment with zero emojis.
"""

import streamlit as st
from config import PROJECT_NAME
from components.assessment_ui import render_assessment_wizard

def render_discover_page():
    """Render career discovery page."""
    render_assessment_wizard()
