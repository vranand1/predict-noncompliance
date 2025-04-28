# pages/4_Provider_Recommendation.py
import streamlit as st
import random

st.set_page_config(layout="centered") # More focused layout for this page

st.title("Smart Pill Bottle Recommendation")
st.caption("Simulating Provider View (e.g., within EHR)")

# --- Simulate data for a single patient recommendation ---
# In a real app, this data would be specific to the patient context
patient_id_masked = f"PAT_***{random.randint(100, 999)}"
risk_score = round(random.uniform(0.75, 0.95), 2)
cost_impact_flag = "Yes"
responsiveness_flag = "Yes"

# --- Recommendation Panel ---
with st.container(border=True):
    st.subheader(f"Rationale for Patient: {patient_id_masked}")

    st.markdown(f"**Non-Adherence Risk:** :red[High] (Score: {risk_score})")
    st.markdown(f"**Potential High Cost Impact:** {cost_impact_flag} *(Based on diagnosis/medication profile)*")
    st.markdown(f"**Likely to Benefit from Smart Bottle:** {responsiveness_flag} *(Based on adherence profile)*")

    st.divider()

    st.markdown("**Recommendation:** Consider Smart Pill Bottle Intervention")

    # --- Action Buttons (Non-functional) ---
    st.markdown("**Provider Action:**")
    col1, col2, col3 = st.columns([1, 1, 3]) # Adjust column ratios as needed
    with col1:
        accept_button = st.button("Accept", key="accept", help="Accept this recommendation (Mockup - non-functional)")
    with col2:
        decline_button = st.button("Decline", key="decline", help="Decline this recommendation (Mockup - non-functional)")

    if accept_button:
        st.success("Action Recorded: Accepted (Mockup)")
    if decline_button:
        st.warning("Action Recorded: Declined (Mockup)")

st.divider()

# --- RBAC & Permissible Use Note ---
st.info(
    """
    **Provider Access Control & Permissible Use:**

    *   **Patient Scope:** Providers access recommendations **only** for their assigned patients.
    *   **Minimum Necessary:** Information displayed is limited to the minimum necessary data required for clinical decision-making regarding this specific intervention.
    *   **Permissible Use:** Data accessed via this recommendation panel must only be used for legitimate **Treatment** or **Healthcare Operations** purposes as defined under HIPAA.
    *   **Confidentiality:** Patient information remains confidential and subject to all applicable privacy regulations.
    """
)