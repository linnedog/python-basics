import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

TEST = pd.read_csv("LLM_TEST.csv")

corr = TEST[['gestation_period', 'birth_weight', 'parity']].corr()

model = ols('birth_weight~ C(sex) + c(parity)+ c(season)', data=TEST).fit()
table = sm.stats.anova_lm(model, typ=3)
print(table)

