import pandas as pd

data = pd.read_csv("student_2.csv")
data_2 = pd.read_csv("sales.csv")


data.columns = data.columns.str.strip()

data_3 = data[data["score"]>=80]

print(data_3[["name", "city"]])

data_2["revenue"] = data_2 ["price"] * data_2["quantity"]

data_4 = data_2.groupby("city")["revenue"].sum()

print(data_4)

pivot = data_2.pivot_table(index= "city", columns= "product", values="revenue", aggfunc= "sum")

print(pivot)

data_5 = data_4.sort_values(ascending=False)

top_2 = data_5.head(3)

print(top_2)