#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the pandas library
import pandas as pd


# In[2]:


#import the pandas library
import numpy as np 


# In[4]:


#create a data frame
data=pd.Series(['amit','kumar','pathak',np.nan,'tejprtap'])


# In[5]:


#print the data
data


# In[6]:


#check the null value
data.isnull()


# In[7]:


#fill the nan at the 0 index
data[0]=None


# In[8]:


#check the null value
data.isnull()


# In[9]:


#import the nan alue from numpy libray
from numpy import nan as na


# In[13]:


#create the dataframe
data=pd.Series([1,na,2,3,na,9])


# In[14]:


#delete the nan value
data.dropna()


# In[15]:


#delete the completely nan value
data.dropna(inplace=True
           )


# In[16]:


#print the data value
data


# In[17]:


#find out the null value
data.notnull()


# In[18]:


#create the dataframe
data1=pd.DataFrame([[1,3,5.3],[1,na,na],[na,na,na],[na,6,9]],dtype=np.float32
                  )


# In[19]:


#print the data
data1


# In[46]:


#delete the nan value from datasets data1
cleaned_data=data1.dropna()


# In[47]:


#print the data
data


# In[22]:


#cleaned the datasets
cleaned_data


# In[24]:


#delete the nan value of all
data.dropna(how='all')


# In[25]:


#fill up the nan value at index 4
data[4]=na


# In[26]:


#print the data
data1


# In[28]:


#drop the nan value at axis 1
data1.dropna(how='all',axis=1)


# In[31]:


#create dataframe of random vales
df=pd.DataFrame(np.random.randn(7,3))


# In[32]:


#indexing the data
df.iloc[:4,1]=na
df.iloc[:2,2]=na


# In[33]:


#print the data
df


# In[34]:


#drop the nan value
df.dropna()


# In[35]:


#drop the nan value with the thresing
df.dropna(thresh=2)


# In[36]:


#fill the nan value
df.fillna(0)


# In[37]:


df.fillna({1:0.5,2:0})


# In[39]:


#create the dataframe of random values
df=pd.DataFrame(np.random.randn(6,3
                               ))


# In[41]:


#indexing the data
df.iloc[2:1]=na
df.iloc[4:,2]=na


# In[42]:


#print the data
df


# In[ ]:




