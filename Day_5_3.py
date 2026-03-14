import pandas as pd

data = pd.read_csv("sales.csv")

data.columns = data.columns.str.strip()

data ["revenue"] = data["price"] * data["quantity"]

data_2 = data.groupby("product")["price"].sum()

print(data_2)

pivot = data.pivot_table(index= "city", columns= "product", values="revenue", aggfunc= "sum")

print(pivot)

data_3 = data.sort_values(by= "revenue" , ascending= False)

data_4 = data_3.head(2)

print(data_4)


data_5 = data.groupby("city")["revenue"].mean()

print(data_5)


