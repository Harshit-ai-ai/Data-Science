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
gooddata['Gender'] = gooddata['Gender'].replace({1: 'Male', 2:'Female'})
gooddata['Smoker'] = gooddata['Smoker'].replace({1: 'Yes', 2: 'No'})
sns.pairplot(gooddata, plot_kws={'alpha': 0.5, 's': 10}, hue='Smoker', palette='Set1')
plt.show()