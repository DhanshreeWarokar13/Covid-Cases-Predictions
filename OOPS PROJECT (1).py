#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# to read the datasets

df = pd.read_excel (r'C:\Users\Dhanashree\Desktop\covide cases in world.xlsx', sheet_name='Sheet1')

df.drop(['S.no'],axis=1,inplace=True)

total_cases = df[' Cases'].sum()
total_deaths = df['death'].sum()
print('Confirmed Cases till date:',total_cases)
print('Total Deaths till date:',total_deaths)
df.style.background_gradient(cmap='Greens')#colors the blocks according to range of cases


# In[ ]:





# In[2]:


#to find the total no. of active cases
import pandas as pd

df = pd.read_excel (r'C:\Users\Dhanashree\Desktop\covide cases in world.xlsx', sheet_name='Sheet1')

df['Active Cases'] = df[' Cases'] - (df['death'] + df['cured'])

total_active_cases = df['Active Cases'].sum()

print('Total number of active cases across World:', total_active_cases)

Tot_Cases = df.groupby('Countries')['Active Cases'].sum().sort_values(ascending=False).to_frame() #sort according to number of active cases
Tot_Cases.style.background_gradient(cmap='Blues')#colors the blocks according to range of cases


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

chart = pd.read_excel(r'C:\Users\Dhanashree\Desktop\Worldwide.xlsx', sheet_name='Sheet1')


x = list(chart['Dates'])
y = list(chart['Daily cases'])

plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.title("Observing the pattern of cases")
plt.show()


# In[4]:


import pandas as pd
from fbprophet import Prophet

df = pd.read_excel (r'C:\Users\Dhanashree\Desktop\Daily_cases.xlsx', sheet_name='Sheet1')

confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()


confirmed.columns = ['ds','y']
confirmed['ds'] = pd.to_datetime(confirmed['ds'])
confirmed.tail()

c = Prophet(interval_width=0.95) 
c.fit(confirmed) 
future = c.make_future_dataframe(periods=365) 
future.tail()

#predicting the future cases
forecast = c.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

confirmed_forecast_plot = c.plot(forecast)


# In[ ]:




