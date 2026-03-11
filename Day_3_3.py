import pandas as pd

data = pd.read_csv("data_2.csv")
data.columns = data.columns.str.strip()

#grading

data["grade"] = "c"
data.loc[data["score"]>=80, "grade"] = "b"
data.loc[data["score"]>=90, "grade"] = "a"

#basic statistics

Statistics_info = data.groupby("grade")["score"].agg(["mean", "max", "min"])

#print

print(Statistics_info)
