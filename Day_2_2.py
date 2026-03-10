import pandas as pd

student = pd.read_csv("student.csv")
scores = pd.read_csv("scores.csv")

data = pd.merge(student, scores, on="id")


data.columns = data.columns.str.strip()


data["total"] = data["score"] * data["age"]

data_2 = data[data["score"]>=80]

group_simple_statistics = data_2.groupby("age")["score"].agg(["mean", "max", "min"])


print(group_simple_statistics)

