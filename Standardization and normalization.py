import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data= pd.read_excel(r'E:\Personal\Honey\MIS\KG Jasmine 2021\MIS Myself Competition Result.xlsx', sheet_name='Sheet1')
print(data)
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
mmscaler= MinMaxScaler()
print(data.columns)
data['MinMaxScaler'] = mmscaler.fit_transform(data[['Total']])
print(data[['Total', 'MinMaxScaler']])
sscaler= StandardScaler()
data['StandardScaler'] = sscaler.fit_transform(data[['Total']])
print(data[['Total', 'StandardScaler']])
rscaler= RobustScaler()
data['RobustScaler'] = rscaler.fit_transform(data[['Total']])
print(data[['Total', 'RobustScaler']])
SD=data.std()
print(SD)
plt.figure(figsize=(10, 6))
for i,col in enumerate(data['MinMaxScaler'],1):
    sns.histplot(data['MinMaxScaler'], kde=True)
    plt.title(col)
plt.tight_layout()
plt.plot()
plt.show()  