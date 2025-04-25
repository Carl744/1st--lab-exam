import pandas as pd

df = pd.read_csv('Exam_Table (1).csv')

df['Genus'] = df['Scientific Name'].astype(str).str.split().str[0]

genus_only = df[df['Genus'].str.startswith('Po')][['Genus']]

print(genus_only)

genus_only.to_csv('buendia_b3_output.csv', index=False)

