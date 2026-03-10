import pandas as pd

data = pd.read_csv("data.csv")
data.columns = data.columns.str.strip()

belowscore85 = data[data["score"]>=85]

print(belowscore85["name"])

age_22data = data[data["age"]>=22]

age_22_score_85 = age_22data[age_22data["score"]>=85]

print(age_22_score_85["name"])

data ["total"] = data["score"] * data["age"]

print(data)

above_80_data = data[data["score"]>=80]

sorted_data = above_80_data.sort_values(by="score", ascending=False)

print(sorted_data[["name", "score"]])

group_mean_data = data.groupby("age")["score"].mean()

print(group_mean_data)

