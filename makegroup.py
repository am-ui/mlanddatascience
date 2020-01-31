#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[8]:


df=pd.DataFrame({'name':['amit','kumar','pathak','amzad','ansari','kanishka'],
           'salary':[546774,6585879,574979,546977,65803,758945384],
           'data1':np.random.randn(6),
            'data2':np.random.randn(6)})


# In[9]:


df.head()


# In[12]:


df['data1'].mean()


# In[13]:


df['data2'].mean()


# In[14]:


df['data1'].median()


# In[15]:


df['data2'].median()


# In[18]:


group1=df.groupby('name')['salary']


# In[25]:


group2=df['salary'].groupby(df['data1'])


# In[26]:


print(group1)


# In[27]:


print(group2)


# In[28]:


group1.describe()


# In[29]:


group2.describe()


# In[33]:


group1


# In[38]:


group1.value_counts()


# In[40]:


group2.value_counts()


# In[41]:


for data, group in group1:
    print(data, group, end="\n")


# In[42]:


for data, group in group2:
    print(data, group, end="\n")


# itration
# 

# In[43]:


df


# In[48]:


for name ,group in df.groupby('salary'):
    print(name,group1, end='\n')


# In[49]:


am=df.groupby(['data1'])


# In[50]:


am


# In[55]:





# In[58]:


for k, gr in group1:
    print(k, gr, end="\n")


# In[61]:


dict(list(df.groupby('data1')))


# In[63]:


dict(list(df.groupby('name')))


# In[67]:


pieces=dict(list(df.groupby('name')))


# In[68]:


pieces['amit']


# In[70]:


df.dtypes


# In[71]:


for dtype, group in df.groupby(df.dtypes, axis=1):
    print(dtype, group, end="\n")


# In[ ]:




