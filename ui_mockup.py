import streamlit as st
import pandas as pd

# Sample data
patients = pd.DataFrame({
    'ID': [12345, 67890],
    'Name': ['J. Doe', 'A. Smith'],
    'Risk Score': [85, 72],
    'Condition': ['Diabetes', 'Hypertension'],
    'Action': ['Prescribe', 'Outreach']
})

# Role selector
role = st.sidebar.selectbox('Select Role', ['Payer Analyst', 'Provider', 'Engagement Team'])

# Role-specific UI
if role == 'Payer Analyst':
    st.title('Payer Analyst Dashboard')
    st.dataframe(patients)
    st.button('Approve All')
elif role == 'Provider':
    st.title('Provider View')
    st.dataframe(patients[['Name', 'Risk Score', 'Condition']])
    st.button('Prescribe Bottle')
elif role == 'Engagement Team':
    st.title('Engagement Team Alerts')
    st.write('Alerts: Patient 12345 missed dose at 8 AM')
    st.button('Send Text')