# pages/1_Payer_Analyst_Dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import generate_dummy_patient_data, get_aggregate_metrics, get_chart_data
except ImportError:
    st.error("Failed to import utility functions. Make sure utils.py is in the root directory.")
    st.stop()

st.set_page_config(layout="wide")

st.title("Payer Analyst Dashboard")

# --- Generate or Load Data ---
# In a real app, data might be loaded or fetched here.
# For the mockup, we generate it on each run.
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = generate_dummy_patient_data(250)

df = st.session_state.patient_data
metrics = get_aggregate_metrics(df)
chart_data = get_chart_data(df)

# --- Display Key Metrics ---
st.header("Key Program Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Patients Analyzed", f"{metrics['Total Patients Analyzed']:,}")
col2.metric("Total Recommended for Intervention", f"{metrics['Total Recommended']:,}")
col3.metric("Provider Acceptance Rate", f"{metrics['Acceptance Rate']:.1%}")


st.divider()

# --- Display Placeholder Charts ---
st.header("Population Segmentation")
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Distribution by Risk Score")
    # Prepare data for st.bar_chart (needs index to be strings)
    risk_dist_df = pd.DataFrame({
        'Count': chart_data['risk_distribution'].values
    }, index=[str(interval) for interval in chart_data['risk_distribution'].index])
    st.bar_chart(risk_dist_df)

    st.subheader("Segmentation by Bottle Responsiveness")
    resp_df = pd.DataFrame(chart_data['responsiveness_distribution'])
    resp_df.columns = ['Count']
    st.bar_chart(resp_df)


with col_chart2:
    st.subheader("Segmentation by Cost Impact")
    # Use Matplotlib for a pie chart
    fig_cost, ax_cost = plt.subplots(figsize=(4, 3)) # Smaller figure size
    cost_labels = chart_data['cost_impact_distribution'].index
    cost_sizes = chart_data['cost_impact_distribution'].values
    ax_cost.pie(cost_sizes, labels=cost_labels, autopct='%1.1f%%', startangle=90)
    ax_cost.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig_cost)


st.divider()

# --- RBAC Note ---
st.info(
    """
    **Payer Analyst Role-Based Access Control (RBAC):**
    Payer Analysts typically have broad access to application features, including dashboards,
    configuration settings, and patient lists necessary for population analysis and program management.
    Access is governed by HIPAA's minimum necessary principle and organizational policies.
    All activities are subject to audit.
    """
)

# --- Optional: Display Raw Data Sample (for context during mockup review) ---
with st.expander("View Sample Raw Data Used for Aggregates"):
    st.dataframe(df.head(10))