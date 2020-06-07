#!/usr/bin/env python
# coding: utf-8

# In[3]:


#creating dataset
from sklearn import datasets
#only checking iris data 
[i for i in dir(datasets) if 'iris' in i]
#only loading iris
from sklearn.datasets import load_iris
#now load_iris is similar to csv file
iris=load_iris()
dir(iris)
#print feature name
iris.feature_names
#printing target name
iris.target_names
iris.data.shape


# In[4]:


#iris.DEScr


# In[5]:


#now storing features value
features=iris.data
features


# In[6]:


spl=features[:,0]


# In[7]:


lables=iris.target


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.scatter(features[:,0],features[:,1],label="Sepal length and width")
plt.scatter(features[:,2],features[:,-1],label="Sepal length and width")
plt.legend()
plt.plot()


# In[11]:


#now using dedcision tree classifieres
from sklearn.tree import DecisionTreeClassifier


# In[12]:


desclf=DecisionTreeClassifier()


# In[18]:


#now training with data
traineddec=desclf.fit(features,lables)


# In[17]:


#now predicting output
traineddec.predict(features[0].reshape(1,4))
features[0]


# In[16]:


features[0].shape


# In[ ]:




