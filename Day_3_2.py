import pandas as pd

data = pd.read_csv("data_2.csv")
data.columns = data.columns.str.strip()

#Make grade

data["grade"] = "C"
data.loc[data["score"]>= 80, "grade"]= "B"
data.loc[data["score"]>= 90, "grade"]= "A"

#grouping, mean and print

grouping_data = data.groupby("grade")["score"].mean()

print(grouping_data)

#problem 2

grouping_data_2 = data.groupby("grade")["score"].max()

print(grouping_data_2)

