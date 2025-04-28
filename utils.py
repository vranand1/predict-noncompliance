# utils.py
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_dummy_patient_data(num_patients=100):
    """Generates a DataFrame with dummy patient data for the Payer Analyst list."""
    patient_ids = [f"PT{str(i).zfill(6)}" for i in range(1, num_patients+1)]
    risk_scores = np.random.uniform(0.3, 0.95, num_patients).round(2)
    cost_impact = np.random.choice(['Y', 'N'], num_patients, p=[0.4, 0.6])
    responsiveness = np.random.choice(['Y', 'N', 'Maybe'], num_patients, p=[0.5, 0.3, 0.2])
    recommendation = (risk_scores > 0.7) & (cost_impact == 'Y') & (responsiveness == 'Y')
    recommendation_str = ['Y' if rec else 'N' for rec in recommendation]
    providers = [f"Provider {chr(ord('A') + random.randint(0, 4))}" for _ in range(num_patients)]

    rec_dates = []
    provider_actions = []
    action_dates = []

    for rec in recommendation:
        if rec:
            rec_date = datetime.now() - timedelta(days=random.randint(1, 60))
            rec_dates.append(rec_date.strftime('%Y-%m-%d'))
            action = random.choice(['Pending', 'Accepted', 'Declined', 'Pending', 'Pending']) # Skew towards Pending
            provider_actions.append(action)
            if action!= 'Pending':
                action_dates.append((rec_date + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'))
            else:
                action_dates.append(None)
        else:
            rec_dates.append(None)
            provider_actions.append(None)
            action_dates.append(None)

    data = {
        'Patient ID (masked)': patient_ids,
        'Risk Score': risk_scores,
        'Cost Impact': cost_impact,
        'Responsiveness': responsiveness,
        'Recommendation': recommendation_str,
        'Provider': providers,
        'Rec Date': rec_dates,
        'Provider Action': provider_actions,
        'Action Date': action_dates
    }
    df = pd.DataFrame(data)
    # Ensure correct types for display/sorting if needed
    df['Rec Date'] = pd.to_datetime(df['Rec Date'], errors='coerce')
    df['Action Date'] = pd.to_datetime(df['Action Date'], errors='coerce')
    return df

def get_aggregate_metrics(df):
    """Calculates dummy aggregate metrics from the patient data."""
    total_patients = len(df)
    # Fix: Get scalar value instead of Series
    total_recommended = df['Recommendation'].eq('Y').sum()
    accepted_count = df['Provider Action'].eq('Accepted').sum()
    declined_count = df['Provider Action'].eq('Declined').sum()

    if (accepted_count + declined_count) > 0:
        acceptance_rate = accepted_count / (accepted_count + declined_count)
    else:
        acceptance_rate = 0.0

    return {
        'Total Patients Analyzed': total_patients,
        'Total Recommended': total_recommended,
        'Acceptance Rate': acceptance_rate
    }

def get_chart_data(df):
    """Generates data suitable for placeholder charts."""
    risk_distribution = df['Risk Score'].value_counts(bins=10, sort=False)
    cost_impact_distribution = df['Cost Impact'].value_counts()
    responsiveness_distribution = df['Responsiveness'].value_counts()

    return {
        'risk_distribution': risk_distribution,
        'cost_impact_distribution': cost_impact_distribution,
        'responsiveness_distribution': responsiveness_distribution
    }

# Example Usage (can be run standalone for testing)
if __name__ == '__main__':
    dummy_df = generate_dummy_patient_data(250)
    print("Generated Patient Data Sample:")
    print(dummy_df.head())
    metrics = get_aggregate_metrics(dummy_df)
    print("\nAggregate Metrics:")
    print(metrics)
    chart_data = get_chart_data(dummy_df)
    print("\nChart Data Samples:")
    print("Risk Distribution:\n", chart_data['risk_distribution'])
    print("Cost Impact:\n", chart_data['cost_impact_distribution'])
    print("Responsiveness:\n", chart_data['responsiveness_distribution'])