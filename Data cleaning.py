import pandas as pd
data= pd.read_excel(r'E:\Personal\Honey\MIS\KG Jasmine 2021\MIS Myself Competition Result.xlsx' , sheet_name='Sheet1')
print(data['Total'])
missing= data['Total'].isnull().sum()
data.fillna(method='ffill')
print(data['Total']>8)