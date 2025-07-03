import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r'E:\Personal\Harshit\AIS\Data-Science\data.csv')
feature_list=['Year', 'MSRP', 'Engine HP', 'Engine Cylinders']
data.drop(columns=['Engine Fuel Type','Number of Doors', 'Market Category', 'Vehicle Size', 'Vehicle Style', 'Popularity'], axis=1, inplace=True)
data.rename(columns={'Make':'Company'}, inplace=True)
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)
def IQR_method(data, columns):
    outlier_indices = set()
    for col in columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outlier_rows = data[(data[col] <= lower_bound) | (data[col] >= upper_bound)]
        outlier_indices.update(outlier_rows.index.tolist())
    outliers = data.loc[list(outlier_indices)]
    return outliers.drop_duplicates()
    
outlier = IQR_method(data, feature_list)
gooddata = data.drop(outlier.index)
gooddata.dropna(inplace=True)

plt.figure(figsize=(10, 6))
corr_mat=gooddata.corr()
sns.heatmap(corr_mat, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
