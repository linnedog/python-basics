import pandas as pd

data = pd.read_csv("student_2.csv")
data.columns = data.columns.str.strip()

data["grade"]="c"
data.loc[data["score"]>=80, "grade"]="b"
data.loc[data["score"]>=90, "grade"]="a"

#filter

filtered_data = data[data["score"]>=80]

filtered_data["weighted"] = filtered_data["score"] * filtered_data["age"]

#pivot

pivottable= filtered_data.pivot_table(index="city", columns="grade", values="score", aggfunc = "mean")

print(pivottable)