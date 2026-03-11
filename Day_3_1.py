import pandas as pd

data = pd.read_csv("data_2.csv")
data.columns = data.columns.str.strip()

#Filtering data

filtered_data = data[data["score"]>=80]

#Create pivot table

pivot = filtered_data.pivot_table(index="age", values="score", aggfunc="mean")

print(pivot)