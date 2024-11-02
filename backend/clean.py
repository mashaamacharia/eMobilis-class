# Sample Python code to analyze survey data on cloud security incidents
import pandas as pd

# Load the dataset
df = pd.read_csv('survey_data.csv')

# Filter data to analyze SMEs that experienced data breaches
data_breaches = df[df['incident_type'] == 'Data Breach']

# Count occurrences of data breaches
breach_count = data_breaches['incident_type'].count()

print(f'Total number of SMEs affected by data breaches: {breach_count}')
