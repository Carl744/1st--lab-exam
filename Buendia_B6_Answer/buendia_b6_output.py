import pandas as pd

df = pd.read_csv('Exam_Table (1).csv')

most_abundant_species= df[df['Species']=='adelus']
print(most_abundant_species)

most_abundant_species.to_csv("buendia_b6_output.csv", index=False)