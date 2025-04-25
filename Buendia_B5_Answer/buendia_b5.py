import pandas as pd

df = pd.read_csv('Exam_Table (1).csv')

df = df.dropna(subset=['Species'])


df['Species'] = df['Species'].astype(str).str.strip()

name_counts = df['Species'].value_counts().reset_index()

name_counts.columns = ['Species', 'Size est (cm)'].str.mean()

print(name_counts)

name_counts.to_csv('b6.csv', index=False)