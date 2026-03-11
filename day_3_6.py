import pandas as pd

data = pd.read_csv("sales.csv")
data.columns = data.columns.str.strip()

pivot = data.pivot_table(index="city", columns="product", values="amount", aggfunc="mean")

pivot = pivot.sort_values(by="apple", ascending=False)

print(pivot)

