import pandas as pd
from openai import OpenAI

# --------------------------------
# 1. CSV 읽기1
# --------------------------------

df = pd.read_csv("llm_test_data.csv", encoding="cp949")

# --------------------------------
# 2. 날짜 전처리
# --------------------------------

df["birth_date"] = pd.to_datetime(df["birth_date"])
df["mating_date"] = pd.to_datetime(df["mating_date"])
df["delivery_date"] = pd.to_datetime(df["delivery_date"])

# --------------------------------
# 3. 파생 변수 생성
# --------------------------------

df["age_at_mating_days"] = (df["mating_date"] - df["birth_date"]).dt.days

# --------------------------------
# 4. 통계 계산
# --------------------------------

region_stats = df.groupby("region")["gestation_period"].mean()

print("지역별 평균 임신기간")
print(region_stats)

# --------------------------------
# 5. LLM 입력 데이터 준비
# --------------------------------

data_text = region_stats.to_string()

# --------------------------------
# 6. Prompt 생성
# --------------------------------

prompt = f"""
다음은 한우 번식 데이터에서 계산된 지역별 평균 임신기간이다.

{data_text}

지역별 차이를 해석하고
가능한 원인을 설명하라.
"""

print("\nLLM Prompt:")
print(prompt)

# --------------------------------
# 7. LLM 호출
# --------------------------------

client = OpenAI(
    api_key="api_key",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# --------------------------------
# 8. 결과 출력
# --------------------------------

answer = response.choices[0].message.content

print("\nLLM 해석 결과")
print(answer)