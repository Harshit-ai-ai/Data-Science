import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
data= pd.read_csv(r'C:\Users\User\Downloads\credit_card_transactions.csv')
data.drop(columns=['trans_date_trans_time'] ,axis=1, inplace=True)
data.drop(columns=['merchant'], axis=1, inplace=True)
data.drop(columns=['category'], axis=1, inplace=True)
data.drop(columns=['first', 'last', 'gender', 'street', 'city', 'merch_zipcode', 'state', 'trans_num', 'job', 'dob'], axis=1, inplace=True)
from sklearn.preprocessing import StandardScaler
sscaler= StandardScaler()
ssdata = pd.DataFrame(sscaler.fit_transform(data))
feature_list=['cc_num', 'amt', 'zip', 'lat', 'long', 'city_pop', 'unix_time', 'merch_lat', 'merch_long', 'is_fraud']
fig, axes= plt.subplots(figsize=(10, 6))
fig.suptitle('Feature vs Class', size=20)
plt.hist(ssdata[10], bins=30, linewidth=1.5, edgecolor='black')
plt.title('is_fraud') 
plt.show()