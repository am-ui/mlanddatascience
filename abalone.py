#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


df=pd.read_csv('abalone.csv')


# In[12]:


df.head()


# In[13]:


col=['sex','lenth','diameter','height','whole_wt','shucked_wt','viscera_wt','shell_wt','rings']


# In[14]:


df.columns=col


# In[15]:


df.head()


# In[16]:


df.info()


# In[17]:


df.hist(bins=50,figsize=(18,9))


# In[18]:


sns.pairplot(df)


# In[19]:


corr_matrix=df.corr()


# In[21]:


plt.figure(figsize=(18,9))
sns.heatmap(corr_matrix,annot=True)


# In[23]:


df.isnull().sum()


# In[24]:


df_cat=df.select_dtypes(include=[np.object])


# In[25]:


df_cat


# In[26]:


#method1
from sklearn.preprocessing import OneHotEncoder


# In[27]:


one_hot=OneHotEncoder(sparse=False)


# In[28]:


cod_vals=one_hot.fit_transform(df_cat)


# In[29]:


cod_vals


# In[30]:


#method 2
df_cat_coded=pd.get_dummies(df_cat,prefix=["sex"])


# In[31]:


df_cat_coded


# In[32]:


df_cat


# In[33]:


df_num=df.select_dtypes(include=[np.number])


# In[ ]:





# In[34]:


df_num


# In[35]:


target=df_num.rings


# In[36]:


target


# In[37]:


target=target.astype('float')


# In[38]:


df_num.head()


# In[40]:


df_num.drop('rings',axis=1,inplace=True)


# In[41]:


df_num.head()


# In[42]:


df_num


# In[43]:


df_cat_coded


# In[47]:


df_final=pd.concat([df_num,df_cat_coded],axis=1,join='outer')


# In[48]:


df_final.head()


# In[49]:


target


# In[50]:


from sklearn.model_selection import train_test_split


# In[52]:


x_train,x_test,y_train,y_test=train_test_split(df_final,target,test_size=0.2,random_state=42)


# In[53]:


from sklearn.ensemble import RandomForestRegressor


# In[55]:


rnd=RandomForestRegressor(n_estimators=10,n_jobs=1)


# In[56]:


rnd.estimator_params


# In[57]:


rnd.fit(x_train,y_train)


# In[59]:


RandomForestRegressor().get_params()


# In[60]:


param_grid={'n_estimators':[100,150,200,250],}


# In[61]:


from sklearn.model_selection import GridSearchCV


# In[64]:


tree_cv=GridSearchCV(RandomForestRegressor(),param_grid,n_jobs=-1,cv=5)


# In[65]:


tree_cv.fit(x_train,y_train)


# In[66]:


tree_cv.best_score


# In[ ]:


model=tree_cv.best_estimator_


# In[ ]:


model.score(x_test,y_test)


# In[ ]:




