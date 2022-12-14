import pandas as pd
import numpy as np


df=pd.read_csv(r'https://raw.githubusercontent.com/siddheshphatarpekar/Dataset/main/NDAP_REPORT_7150.csv').dropna()
df.replace(np.nan,0)
Pending_cases_statewise=pd.pivot_table(df,index=['State']
                             ,values=['Pending cases','Original pending cases']
                             ,aggfunc=np.sum)
Pending_state_S=Pending_cases_statewise.sort_values(by='Pending cases',ascending=False)

Pending_cases_districtwise=df[(df['State'] == 'Uttar Pradesh')].pivot_table(index=['District']
                             ,values=['Pending cases','Original pending cases']
                             ,aggfunc=np.sum)
Pending_district_S=Pending_cases_districtwise.sort_values(by='Pending cases',ascending=False)

Pending_cases_type=df[(df['District and taluk court case type'] != 'Total')].pivot_table(index=['District and taluk court case type']
                             ,values=['Pending cases','Original pending cases']
                             ,aggfunc=np.sum)
Pending_type_S=Pending_cases_type.sort_values(by='Pending cases',ascending=False)

print('\n')
print('Top 10 District in Uttar Pradesh With Pending Cases ')
print(Pending_district_S.head(10))
print('\n')
print('Top 10 State with Pending Cases')
print(Pending_state_S.head(10))
print('\n')
print(Pending_type_S.head())
