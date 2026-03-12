import pandas as pd

data = pd.read_csv("sales.csv")

data.columns = data.columns.str.strip()

data ["revenue"] = data ["price"] * data ["quantity"]

data_2 = data.groupby("city")["revenue"].sum()

print(data_2)


pivot = data.pivot_table(index= "city", columns= "product", values= "revenue", aggfunc= "sum")

sorted_data = pivot.sort_values(by= "city", ascending=False)

print(sorted_data)