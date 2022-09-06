#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


import datetime
from matplotlib.dates import DateFormatter


# In[12]:


customer = pd.read_csv("C:\Ajay python/QVI_purchase_behaviour.csv")


# In[6]:


transaction = pd.read_csv("C:\Ajay python/QVI_transaction_data.csv")


# # Creating and interpreting high level summaries of the data

# In[7]:


transaction.head()


# In[8]:


transaction.info()


# In[9]:


transaction.describe()


# In[10]:


transaction.shape


# In[13]:


customer.head()


# In[14]:


customer.info()


# In[15]:


customer.describe()


# In[16]:


len(transaction)


# In[18]:


#checking for unique rows with 'TXN_ID'
transaction['TXN_ID'].nunique()


# In[20]:


#checking duplicated rows
transaction[transaction.duplicated(['TXN_ID'])].head()


# In[23]:


transaction.loc[transaction['TXN_ID'] == 48887,:]


# In[24]:


len(customer)


# In[25]:


customer['LYLTY_CARD_NBR'].nunique()


# # checking and removing outliers

# In[26]:


sns.boxplot(transaction.TOT_SALES)


# In[51]:



sns.histplot(transaction.TOT_SALES, kde = True)


# In[40]:


plt.scatter(transaction.TOT_SALES, transaction.PROD_NAME)


# In[41]:


numericdata = transaction.select_dtypes(['float','int'])


# In[42]:


numericdata.head()


# In[43]:


#removing outliers of TOT_SALES by using mean
x = numericdata[numericdata['TOT_SALES'] < 8]


# In[52]:


sns.histplot(x.TOT_SALES, kde = True)


# In[49]:


sns.histplot(x.TOT_SALES, kde = True)


# In[53]:


sns.boxplot(x.TOT_SALES)
# from this plot we can see that no outliers are there


# In[56]:


sns.boxplot(x.PROD_QTY)


# In[60]:


transaction['PROD_QTY'].value_counts()


# In[61]:


transaction.loc[transaction['PROD_QTY'] == 200 ,:]


# In[63]:


#this looklike outlier, so we are dropping this customer
transaction.drop(transaction.index[transaction['LYLTY_CARD_NBR'] == 226000], inplace = True)
customer.drop(customer.index[customer['LYLTY_CARD_NBR'] == 226000], inplace = True)


# In[65]:


#checking whether its droped or not
transaction.loc[transaction['LYLTY_CARD_NBR'] == 226000 ,:]


# # Checking data formats and correcting 
# 

# In[66]:


transaction.info()


# In[67]:


# the date format is in INT we need to convert into exact formate
transaction['DATE'].head()


# In[68]:


#changing the date formate
def integer_to_date(changedate):
    excel_anchor = datetime.datetime(1900, 1, 1)
    if(changedate < 60):
        delta_in_days = datetime.timedelta(days = (changedate - 1))
    else:
        delta_in_days = datetime.timedelta(days = (changedate - 2))
    converted_date = excel_anchor + delta_in_days
    return converted_date


# In[69]:


#applying new date formate to dataset
transaction['DATE'] = transaction['DATE'].apply(integer_to_date)


# In[70]:


#now the date is changed
transaction['DATE'].head()


# In[71]:


transaction.head()


# In[72]:


# creating 'PACK_SIZE' new column


# In[73]:


transaction['PACK_SIZE'] = transaction['PROD_NAME'].str.extract("(\d+)")
transaction['PACK_SIZE'] = pd.to_numeric(transaction['PACK_SIZE'])
transaction.head()


# In[87]:


#finding total sales on each date
a = pd.pivot_table(transaction, values = 'TOT_SALES', index = 'DATE', aggfunc = 'sum')


# In[88]:


a.head()


# In[90]:


# Check the distribution of PACK_SIZE
plt.figure(figsize = (10, 5))
plt.hist(transaction['PACK_SIZE'])     
plt.xlabel('Pack Size')
plt.ylabel('Frequency')
plt.title('Pack Size Histogram')


# # customer data
# 

# In[91]:


customer.head()


# In[92]:


len(customer)


# In[94]:


customer['LYLTY_CARD_NBR'].nunique()


# In[95]:


customer['LIFESTAGE'].nunique() # how many rows in 'LIFESTAGE'


# In[96]:


customer['LIFESTAGE'].unique()


# In[99]:


# count of lifestages
customer['LIFESTAGE'].value_counts()


# In[101]:


sns.countplot(y = customer['LIFESTAGE'], order = customer['LIFESTAGE'].value_counts().index)


# In[103]:


customer['PREMIUM_CUSTOMER'].nunique()


# In[105]:


customer['PREMIUM_CUSTOMER'].value_counts().sort_values(ascending = False)


# In[106]:


plt.figure(figsize = (12, 7))
sns.countplot(y = customer['PREMIUM_CUSTOMER'], order = customer['PREMIUM_CUSTOMER'].value_counts().index)
plt.xlabel('Number of Customers')
plt.ylabel('Premium Customer')


# In[ ]:




