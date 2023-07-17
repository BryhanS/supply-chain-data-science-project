#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:14:25 2020

@author: haythamomar
"""
import pandas as pd

from datetime import datetime
import numpy as np
retail= pd.read_csv('online_retail2.csv')

retail= retail.drop_duplicates()
retail= retail.dropna(axis=0,how='any')
retail.info()

retail['InvoiceDate']=pd.to_datetime(retail['InvoiceDate'])

retail['InvoiceDate'].dt.year
retail['InvoiceDate'].dt.month
retail['InvoiceDate'].dt.week
retail['InvoiceDate'].dt.day


retail['InvoiceDate'].dt.strftime('%W %Y')

retail['InvoiceDate'].max()

retail['InvoiceDate'].min()

retail['InvoiceDate'].max()- retail['InvoiceDate'].min()



#### recency 

##max date of dataset

max_date= retail.InvoiceDate.max()

retail.columns
last_purchase_Date= retail.groupby('Customer ID',as_index=False)['InvoiceDate'].max()

last_purchase_Date['Recency']= max_date- last_purchase_Date['InvoiceDate']

last_purchase_Date['Recency'].describe()

import matplotlib.pyplot as plt

last_purchase_Date['Recency_days']= last_purchase_Date['Recency'].dt.components['days']


plt.hist(last_purchase_Date['Recency_days'])


### modelling 

import numpy as np

customers= np.unique(retail['Customer ID'])

len(customers)

retail['date']= retail['InvoiceDate'].dt.strftime('%Y-%m-%d')

customer_grouped= retail.groupby(['Customer ID','date'],
                                 as_index=False).count()[['Customer ID','date']]

inter_data= pd.DataFrame()

for customer in customers:
    c_d= customer_grouped[customer_grouped['Customer ID']== customer]
    c_d['previous_date']= c_d['date'].shift(1) 
    inter_data= pd.concat([inter_data,c_d],axis=0)


inter_data.info()
inter_data['date']=pd.to_datetime(inter_data['date'])
inter_data['previous_date']=pd.to_datetime(inter_data['previous_date'])

inter_data['duration']=inter_data['date']-inter_data['previous_date']

inter_data['duration']=inter_data['duration'].dt.components['days']


inter_arrival= inter_data.groupby('Customer ID')['duration'].mean()


import pandas as pd

stocks= pd.read_csv('stocks.csv',index_col= 'Date',parse_dates= True)

stocks.plot()


monthly_series_mean= stocks.resample('M').mean()
year_series_mean= stocks.resample('Y').mean()
quarter_series_mean= stocks.resample('W').mean()

monthly_series_mean.plot()

# SUM (), first(),last(),

quarter_series_sum= stocks.resample('W').sum()

MSFT= stocks[['MSFT']]

MSFT['rolling_weekly']= MSFT.rolling(window=7).mean()
MSFT['rolling_monthly']=MSFT['MSFT'].rolling(window=30).mean()
MSFT['Aug-2011': 'Dec-2011'].plot()



































































