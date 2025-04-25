import pandas as pd

df = pd.read_csv('Exam_Table (1).csv')


df = df.dropna(subset=['Scientific Name'])


df['Scientific Name'] = df['Scientific Name'].astype(str).str.strip()

name_counts = df['Scientific Name'].value_counts().reset_index()

name_counts.columns = ['Scientific Name', 'Count']

print(name_counts)

name_counts.to_csv('scientific_name_size.csv', index=False)