import pandas as pd

df = pd.read_csv('Exam_Table (1).csv')

df = df.dropna(subset=['Replicate'])


df['Replicate'] = df['Replicate'].astype(str).str.strip()

replicate_counts = df['Replicate'].value_counts().reset_index()

replicate_counts.columns = ['Replicate', 'Count']

print(replicate_counts)

replicate_counts.to_csv('buendia_b9_output.csv', index=False)