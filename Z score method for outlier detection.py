import pandas as pd
from sklearn.preprocessing import StandardScaler
data = pd.read_csv(r'C:\Users\User\Downloads\credit_card_transactions.csv')
feature_list = ['cc_num', 'amt', 'zip', 'lat', 'long', 'city_pop', 'unix_time', 'merch_lat', 'merch_long', 'is_fraud']
def z_score_method(data, col):
    y = data[col].mean()
    z = data[col].std()
    threshold = 3
    outliers = data[(data[col] > y + threshold * z) | (data[col] < y - threshold * z)]
    return outliers.drop_duplicates()

outlier=z_score_method(data,feature_list)
gooddata = data.drop(outlier.index)
gooddata.dropna(inplace=True)
print(gooddata)