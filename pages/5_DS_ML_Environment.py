# pages/5_DS_ML_Environment.py
import streamlit as st

st.set_page_config(layout="wide")

st.title("Payer DS/ML Environment Access")
st.caption("Simulated Portal for Data Science / Machine Learning Team")

st.markdown(
    """
    This page represents a central access point for Data Science and Machine Learning
    engineers involved in developing, deploying, and maintaining the platform's
    predictive models and data pipelines.
    """
)

st.divider()

st.header("Development & Operational Tools (Mockup Links)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Model Development & Experimentation")
    st.button("Access C3 AI Studio / Development IDE", use_container_width=True, help="Access integrated development environment (Mockup - non-functional)")
    st.button("Launch JupyterLab Notebook Instance", use_container_width=True, help="Start a managed notebook session (Mockup - non-functional)")
    st.button("Access Feature Store / Registry", use_container_width=True, help="Browse and manage ML features (Mockup - non-functional)")
    st.button("Access Unified Data Lake / Warehouse", use_container_width=True, help="Connect to curated data sources (Mockup - non-functional)")

with col2:
    st.subheader("Model Operations & Management")
    st.button("View Model Ops Dashboard", use_container_width=True, help="Monitor deployed model performance and health (Mockup - non-functional)")
    st.button("Manage ML Pipelines", use_container_width=True, help="View and manage data/ML pipeline configurations (Mockup - non-functional)")
    st.button("Access Model Registry", use_container_width=True, help="Browse and manage registered model versions (Mockup - non-functional)")
    st.button("Configure CI/CD for ML", use_container_width=True, help="Access continuous integration/deployment settings (Mockup - non-functional)")


st.divider()

# --- DS/ML RBAC Note ---
st.info(
    """
    **DS/ML Engineer Access Control & Data Handling:**

    *   **Tool Access:** Granted access to specialized development environments (IDEs, Notebooks), MLOps platforms, model registries, feature stores, and ML pipeline orchestration tools.
    *   **Data Access:** Access to data required for model building, training, validation, and monitoring. This may include:
        *   **Pseudonymized/De-identified Data:** Used where possible to minimize PHI exposure during development and testing.[5]
        *   **Protected Health Information (PHI):** Access to identifiable PHI within secure, audited environments may be granted when strictly necessary for specific tasks (e.g., debugging model performance for specific patient cases, certain types of feature engineering), governed by BAAs, data use agreements, and HIPAA's minimum necessary standard.
    *   **Purpose:** Focus is on the technical lifecycle of AI/ML models – development, training, validation, deployment, monitoring, and retraining.
    *   **Compliance:** All activities involving PHI must adhere to HIPAA regulations and organizational security policies.
    """
)