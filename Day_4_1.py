import pandas as pd

data = pd.read_csv("student.csv")
data_2 = pd.read_csv("scores.csv")

data.columns = data.columns.str.strip()

data_3= pd.merge(data, data_2, on="id", how="right")

print(data_3[["id", "name", "age", "score"]])

data_4 = data_3[data_3["score"]>=80]

print(data_4)

data_3["total"] = data_3["score"] * data_3["age"]

data_5= data_3.sort_values(by= "total", ascending=False)

print(data_5[["name", "age", "score", "total"]])
