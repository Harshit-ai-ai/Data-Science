import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r'C:\Users\91981\Downloads\Module-4-Data-Sets\NHANES.csv')
gooddata = data.loc[:, ['BMXWT', 'SEQN', 'SMQ020', 'RIAGENDR', 'RIDAGEYR', 'DMDEDUC2', 'BMXHT', 'BMXBMI']]
gooddata.columns=['Weight', 'Seqn', 'Smoker', 'Gender', 'Age', 'Education', 'Height', 'BMI']
duplicates = gooddata[gooddata.duplicated()]
gooddata.drop_duplicates()
gooddata.dropna(inplace=True)
gooddata.drop(columns='Seqn', inplace=True)
print(gooddata.head())
def IQR_bounds(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

numeric_cols = ['Weight', 'Height', 'BMI', 'Age']
outliers = pd.DataFrame()
for col in numeric_cols:
    lower_bound, upper_bound = IQR_bounds(gooddata, col)
    outliers_in_col = gooddata[(gooddata[col] < lower_bound) | (gooddata[col] > upper_bound)]
    outliers = pd.concat([outliers, outliers_in_col])
outliers = outliers.drop_duplicates()
fig, axis = plt.subplots(2, 2, figsize=(15, 10))
sns.histplot(data=gooddata, x='Weight', ax=axis[0, 0])
sns.histplot(data=gooddata, x='Height', color='pink', ax=axis[0, 1])
sns.histplot(data=gooddata, x='BMI', color='red', ax=axis[1, 0])
sns.histplot(data=gooddata, x='Age', color='gold', ax=axis[1, 1])
plt.show()
