import pandas as pd

df = pd.read_csv('Exam_Table (1).csv')

df['Observer'] = df['Observer'].astype(str).str.split().str[0]

observer_only = df[df['Observer'].str.startswith('KS')][['Observer']]

print(observer_only)

observer_only.to_csv('buendia_b7_output.csv', index=False)