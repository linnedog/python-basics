import pandas as pd

data = pd.read_csv("student.csv")
data_2 = pd.read_csv("scores.csv")

data.columns = data.columns.str.strip()

merged_data = pd.merge(data, data_2, on="id", how="inner")

filtered_data =merged_data[merged_data["score"]>=80]

pivot=filtered_data.pivot_table(index= "city", columns="subject", values= "score", aggfunc= "mean")

