# pages/3_Payer_Analyst_Configuration.py
import streamlit as st

st.set_page_config(layout="wide")

st.title("Payer Analyst Configuration")

st.header("Program Parameters")

# --- Risk Threshold ---
st.subheader("Risk Score Threshold")
threshold_risk = st.slider(
    "Set minimum Risk Score for patient inclusion (`Threshold_Risk`):",
    min_value=0.0,
    max_value=1.0,
    value=st.session_state.get('threshold_risk', 0.70), # Use session state to persist value
    step=0.05,
    help="Patients with a risk score below this threshold may be excluded from certain lists or recommendations."
)
# Store the value in session state if needed across pages/runs
st.session_state.threshold_risk = threshold_risk
st.write(f"Current Risk Score Threshold set to: **{threshold_risk:.2f}**")

st.divider()

# --- High-Cost-Impact Rules ---
st.subheader("High-Cost-Impact Criteria Definition")
st.markdown("Define rules based on diagnosis (ICD-10) or medication (NDC) codes.")

cost_icd_codes = st.multiselect(
    "Select High-Cost-Impact ICD-10 Codes (Examples):",
    options=["E11.9", "I10", "J45.909", "M06.9", "F32.9", "K21.9", "M19.90"],
    default=st.session_state.get('cost_icd_codes', ["E11.9", "I10", "J45.909"]),
    help="Select ICD-10 codes associated with high healthcare costs."
)
st.session_state.cost_icd_codes = cost_icd_codes

cost_ndc_codes = st.text_area(
    "Enter High-Cost-Impact NDC Codes (Examples - Use comma separation):",
    value=st.session_state.get('cost_ndc_codes', "0002-8215-01, 0071-0156-23, 50242-0040-62, 0378-0149-01"),
    height=100,
    help="Enter National Drug Codes (NDC) for high-cost medications, separated by commas."
)
st.session_state.cost_ndc_codes = cost_ndc_codes

st.write("Current High-Cost Criteria:")
st.write(f"- **ICD-10 Codes:** {', '.join(cost_icd_codes) if cost_icd_codes else 'None selected'}")
st.write(f"- **NDC Codes:** {cost_ndc_codes if cost_ndc_codes else 'None entered'}")

st.divider()

# --- Bottle Responsiveness Profile ---
st.subheader("Bottle Responsiveness Profile Characteristics (Read-Only)")
st.markdown(
    """
    This profile estimates a patient's likelihood to benefit from and effectively use a smart pill bottle intervention.
    It is based on a predictive model maintained by the DS/ML Team, analyzing factors such as:

    *   **Prior Adherence Patterns:** Historical medication adherence metrics (e.g., PDC/MPR from claims data).
    *   **Demographics:** Factors like age group, which may correlate with technology adoption or adherence challenges.
    *   **Clinical Factors:** Comorbidity burden, complexity of the medication regimen.
    *   **Behavioral Factors:** Previous engagement with health technology (if available), patient-reported barriers.
    *   *(Other factors as determined by the DS/ML model development process)*

    *Note: Payer Analysts view this profile information but do not directly configure the underlying model parameters here.*
    """
)

st.divider()

# --- RBAC Reminder ---
st.info(
    """
    **Access Note:** Configuration changes made here impact patient identification and program rules across the platform.
    Access to this configuration page is restricted to authorized Payer Analysts or administrative roles.
    All changes are logged for auditing purposes.
    """
)