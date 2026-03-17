import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

TEST = pd.read_csv("LLM_TEST.csv", encoding='cp949')

corr = TEST[['gestation_period', 'birth_weight', 'parity']].corr()

print(corr)

model = ols('birth_weight~ C(sex) + C(season)', data=TEST).fit()
table = sm.stats.anova_lm(model, typ=3)
print(table)

reg_model = ols('birth_weight ~ gestation_period + parity', data=TEST).fit()

print(reg_model.summary())

import seaborn as sns
import matplotlib.pyplot as plt


# 한글 깨짐 방지 (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 시각화 시작
plt.figure(figsize=(10, 6))
sns.regplot(x='gestation_period', y='birth_weight', data=TEST, 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})

plt.title('임신 기간에 따른 생시 체중 변화 (회귀선 포함)')
plt.xlabel('임신 기간 (일)')
plt.ylabel('생시 체중 (kg)')
plt.grid(True)
plt.show()