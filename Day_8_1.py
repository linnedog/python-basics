import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
TEST = pd.read_csv("LLM_TEST.csv", encoding='cp949')

#상관분석
corr_results = TEST[['gestation_period', 'birth_weight', 'parity']].corr()
print("\n 상관분석 결과")
print(corr_results)

#ANOVA
anova_model = ols('birth_weight ~ C(sex) * C(season)', data=TEST).fit()
anova_result = sm.stats.anova_lm(anova_model, typ=3)
print("\n 분산분석 결과")
print(anova_result)

from statsmodels.stats.multicomp import pairwise_tukeyhsd

posthoc = pairwise_tukeyhsd(TEST['birth_weight'], TEST['season'], alpha=0.05)
print("\n tukey-hsd 결과")
print(posthoc)

reg_model = ols('birth_weight ~ gestation_period + parity + sex', data=TEST).fit()
print("\n 회귀분석 결과")

print(reg_model.summary())
from statsmodels.stats.outliers_influence import variance_inflation_factor
X = TEST[['gestation_period', 'parity', 'sex']]
X = sm.add_constant(X) # Intercept 추가
vif_df = pd.DataFrame()
vif_df["feature"] = X.columns
vif_df["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
print("\n vif 결과")
print(vif_df)

import os
from dotenv import load_dotenv
from openai import OpenAI

# --------------------------------
# 5. LLM 입력용 데이터 텍스트화 (핵심 수치들 모으기)
# --------------------------------

# 1) 회귀 분석 결과 (계수 테이블 위주)
reg_summary = reg_model.summary().as_text()

# 2) ANOVA 결과
anova_summary = anova_result.to_string()

# 3) VIF 결과
vif_summary = vif_df.to_string()

# 4) 지역별 평균 (기존에 네가 하려던 것)
region_stats = TEST.groupby("region")["gestation_period"].mean().to_string()

# --------------------------------
# 6. Prompt 생성 (전문가 페르소나 부여)
# --------------------------------

prompt = f"""
당신은 대한민국 한우 사양 관리 및 통계 분석 전문가입니다. 
아래의 다각도 통계 분석 결과를 바탕으로 '한우 번식 성적 심층 분석 보고서'를 작성해 주세요.

[1. 지역별 평균 임신 기간]
{region_stats}

[2. 분산 분석(ANOVA) 결과 - 성별 및 시즌 영향]
{anova_summary}

[3. 회귀 분석 결과 - 생시 체중 영향 요인]
{reg_summary}

[4. 다중공선성(VIF) 검계]
{vif_summary}

[보고서 작성 가이드라인]
- 통계적 유의성(P-value)을 언급하며 각 변수의 영향력을 해석할 것.
- 특히 산차(parity)가 생시 체중에 미치는 긍정적 영향에 대해 고찰할 것.
- 농가 현장에서 적용 가능한 실무적인 사양 관리 제언을 포함할 것.
- 말투는 격의 없으면서도 전문성을 유지할 것.
"""

# --------------------------------
# 7. LLM 호출 (환경 변수 사용 권장)
# --------------------------------

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

# --------------------------------
# 8. 결과 출력 및 저장
# --------------------------------

report_content = response.choices[0].message.content

print("\n" + "="*50)
print("AI 생성 한우 번식 분석 보고서")
print("="*50)
print(report_content)

# 파일로 저장해서 나중에 포트폴리오로 제출해!
with open("hanwoo_analysis_report.txt", "w", encoding="utf-8") as f:
    f.write(report_content)