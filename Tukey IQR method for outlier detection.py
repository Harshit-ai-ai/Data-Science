# Tukey IQR method for outlier detection
import numpy as np
import pandas as pd
data= pd.read_csv(r'C:\Users\User\Downloads\credit_card_transactions.csv')
feature_list=['cc_num', 'amt', 'zip', 'lat', 'long', 'city_pop', 'unix_time', 'merch_lat', 'merch_long', 'is_fraud']
def IQR_method(data, column):
    outlier_list=pd.concat([outlier_list, outliers])

    for col in column:
     Q1 = data[col].quantile(0.25)
     Q3 = data[col].quantile(0.75)
     IQR = Q3 - Q1
     lower_bound = Q1 - 1.5 * IQR
     upper_bound = Q3 + 1.5 * IQR
     outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]


    return outliers.drop_duplicates()
outlier= IQR_method(data, feature_list)  
 