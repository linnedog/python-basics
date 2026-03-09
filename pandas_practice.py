import pandas as pd
data = pd.read_csv("data.csv")
data.columns = data.columns.str.strip()

data["total"] = data["score"] * data["age"]

filtered_data = data[data["score"]>=80]

sorted_data = filtered_data.sort_values(by="total", ascending=False)

print(sorted_data[["name", "age", "score", "total"]])