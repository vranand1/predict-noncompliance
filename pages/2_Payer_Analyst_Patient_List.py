# pages/2_Payer_Analyst_Patient_List.py
import streamlit as st
import pandas as pd
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import generate_dummy_patient_data
except ImportError:
    st.error("Failed to import utility functions. Make sure utils.py is in the root directory.")
    st.stop()

st.set_page_config(layout="wide")

st.title("Payer Analyst Patient List")

# --- Generate or Load Data ---
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = generate_dummy_patient_data(250)

df_display = st.session_state.patient_data.copy()

# Format dates for display if they are datetime objects
if pd.api.types.is_datetime64_any_dtype(df_display):
    df_display = df_display.dt.strftime('%Y-%m-%d').fillna('N/A')
if pd.api.types.is_datetime64_any_dtype(df_display['Action Date']):
    df_display['Action Date'] = df_display['Action Date'].dt.strftime('%Y-%m-%d').fillna('N/A')


# --- Filtering Simulation ---
st.sidebar.header("Filter Options (Mockup)")
providers = ['All'] + sorted(df_display['Provider'].unique().tolist())
selected_provider = st.sidebar.selectbox("Filter by Provider:", providers)

actions = ['All'] + sorted(df_display['Provider Action'].dropna().unique().tolist())
selected_action = st.sidebar.selectbox("Filter by Provider Action:", actions)

# Apply filters (demonstration - in real app, this would query backend)
if selected_provider!= 'All':
    df_display = df_display[df_display['Provider'] == selected_provider]
if selected_action!= 'All':
    df_display = df_display[df_display['Provider Action'] == selected_action]


# --- Display Patient Table ---
st.header("Identified Patient Cohort")
st.dataframe(df_display, use_container_width=True)
st.caption(f"Displaying {len(df_display)} records based on filter selection.")

st.divider()

# --- PHI/BAA Note ---
st.warning(
    """
    **Protected Health Information (PHI) Handling Advisory:**

    *   **Contains PHI:** This view displays Protected Health Information. Access is strictly controlled via Role-Based Access Control (RBAC) and limited to authorized personnel.
    *   **HIPAA Compliance:** All interactions with this data must adhere to the Health Insurance Portability and Accountability Act (HIPAA) regulations, including the Minimum Necessary standard.
    *   **Business Associate Agreement (BAA):** If this platform is provided or managed by a third-party vendor, a formal Business Associate Agreement (BAA) **must** be in place. This agreement legally requires the vendor to implement HIPAA-compliant safeguards to protect PHI. Failure to have a BAA is a significant compliance violation.
    """
)