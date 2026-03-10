import pandas as pd

data = pd.read_csv("data.csv")
data.columns = data.columns.str.strip()

data ["grade"] = "C"


data.loc[data["score"]>=80, "grade"]= "B"
data.loc[data["score"]>=90, "grade"]= "A"

print(data)

group_simple_statistics = data.groupby("age")["score"].agg(["mean", "max", "min"])

print(group_simple_statistics)