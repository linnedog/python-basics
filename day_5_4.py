import pandas as pd

student_data = pd.read_csv("day_5_students.csv")

scores_data = pd.read_csv("day_5_scores.csv")

merged_data = pd.merge(student_data, scores_data, on= "id", how= "left")

merged_data_2 = merged_data

merged_data_3 = merged_data 

print("---- Merged Data -----")

print(merged_data)

merged_data["grade"] = "c"

merged_data.loc[merged_data["score"]>=80, "grade"] = "b"

merged_data.loc[merged_data["score"]>=90, "grade"] = "a"

print("\n=====loc_merged_data=====")
print(merged_data)

# or 

merged_data_2 ["grade"] = merged_data_2["score"].apply(lambda x : "a" if x >= 90 else "B" if x >=80 else "c" )

print("\n=====apply_merged_data_2=====")
print(merged_data_2)

merged_data_3["score_per_age"] = merged_data_3["score"] / merged_data_3["age"]

groupby_data = merged_data_3.groupby("city")["score"].mean()

print("\n=====mean_groupby_data=====")
print(groupby_data)

pivot = merged_data_3.pivot_table(index= "city", columns="subject", values="score", aggfunc= "mean")

print("\n=====pivot_table=====")
print(pivot)



max_score_student = merged_data.groupby("city")["score"].transform("max")
max_score_student_list = merged_data[merged_data["score"] == max_score_student]
print("\n=====max_score_student=====")
print(max_score_student_list)


top3 = merged_data.sort_values(by= "score", ascending=False)

top3_list = top3.head(3)

print("\n=====top3_score_student=====")
print(top3_list[["name", "subject", "score"]])


statistics = merged_data.groupby("grade")["score"].agg(["mean", "max", "min"])

print("\n=====statistics_info=====")
print(statistics)