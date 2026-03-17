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

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)