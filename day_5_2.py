import pandas as pd

data = pd.read_csv("student.csv")

data.columns = data.columns.str.strip()

data ["category"] = data["score"].apply(lambda x: "excellent" if x >= 90 else "good" if x>=80 else "bad")

print(data)

