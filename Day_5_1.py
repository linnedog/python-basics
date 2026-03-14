import pandas as pd

data = pd.read_csv("day_5.csv")

data.columns = data.columns.str.strip()

data_2 = data


data_2 ["result"]= data_2["score"].apply(lambda x: "pass" if x>= 85 else "fail")

print(data_2)

data ["score_per_age"] = data.apply(lambda row : row["score"] / row["age"], axis=1)

print(data)