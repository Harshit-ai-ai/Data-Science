import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
data = pd.read_excel(r'E:\Personal\Harshit\AIS\test.xlsx', sheet_name='Sheet1')
feature_list=['height', 'weight', 'age']
data.drop(columns=['name'] ,axis=1, inplace=True)
sscaler= StandardScaler()
ssdata = pd.DataFrame(sscaler.fit_transform(data), columns=data.columns)
def StDev_method(data, feature_list):
    outliers_indices = set()
    outliers = pd.DataFrame()
    for col in feature_list:
        mean = data[col].mean()
        std_dev = data[col].std()
        cutoff = std_dev * 3
        lower_bound = mean - cutoff
        upper_bound = mean + cutoff
        outlier_rows = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        outliers_indices.update(outlier_rows.index.tolist())
        outliers = pd.concat([outliers, outlier_rows])
    outliers = outliers.drop_duplicates()
    return list(outliers_indices), outliers
outlier_indices, outliers = StDev_method(ssdata, feature_list)
gooddata = ssdata.drop(index=outlier_indices)
print(gooddata)
print("Outlier Indices:", outlier_indices)
print("Outliers:", outliers)