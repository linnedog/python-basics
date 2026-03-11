import pandas as pd

data = pd.read_csv("data_2.csv")
data.columns = data.columns.str.strip()

data["grade"] = "c"
data.loc[data["score"]>=80, "grade"] = "b"
data.loc[data["score"]>=90, "grade"] = "a"

pivot= data.pivot_table(index= "grade", columns= "age", values= "score", aggfunc= "mean")

print(pivot)