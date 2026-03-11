import pandas as pd

data = pd.read_csv("data.csv")
data.columns = data.columns.str.strip()

# Data filtering

filtered_data = data[data["score"]>=80]

#Create total

filtered_data ["total"] = filtered_data ["score"] * filtered_data ["age"]

#sort data and print

sorted_data = filtered_data.sort_values(by= "total", ascending=False)

print(sorted_data)

