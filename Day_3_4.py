import pandas as pd

data = pd.read_csv("data_2.csv")
data.columns = data.columns.str.strip()

#problem1

filtered_data = data[data["score"]>=85]

print(filtered_data[["name", "score"]])

#problem2

data["total"] = data["score"] * data["age"]

sorted_data = data.sort_values(by= "total", ascending=False)

print(sorted_data[["name", "age", "score", "total"]])

#problem3

data["grade"] = "c"
data.loc[data["score"]>=80, "grade"] = "b"
data.loc[data["score"]>=90, "grade"] = "a"

Statistics_info = data.groupby("grade")["score"].agg(["mean", "max"])

pivot = data.pivot_table(index= "grade", columns="age", values= "score", aggfunc= "mean")

print(pivot)