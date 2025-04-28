# app.py
import streamlit as st

st.set_page_config(
    page_title="Healthcare Analytics Mockup",
    layout="wide"
)

st.title("Healthcare Analytics Platform Mockup")
st.sidebar.success("Select a page above.")

st.markdown(
    """
    This application provides interactive mockups for various UI concepts
    and user roles within a hypothetical healthcare analytics platform.

    **Select a page from the sidebar** to explore different views:
    - Payer Analyst Dashboard
    - Payer Analyst Patient List
    - Payer Analyst Configuration
    - Provider Recommendation (EHR Sim)
    - DS/ML Environment Access
    - Security & Compliance Overview

    *Note: This is a prototype using dummy data. Features like buttons and
    links (beyond page navigation) are non-functional.*
    """
)