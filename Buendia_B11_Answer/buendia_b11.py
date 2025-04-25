import pandas as pd

df = pd.read_csv('Exam_Table (1).csv')

drop_duplicates = df['Date', 'Site', 'Scientific Name']

print(drop_duplicates)

drop_duplicates.to_csv('buendia_b11_output.csv', index=False)