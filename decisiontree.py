#!/usr/bin/env python
# coding: utf-8

# In[9]:


#taking data set
from sklearn.datasets import load_iris
iris_data=load_iris()
dir(iris_data) #similar to pd.info
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.matrics import accuracy_score


# In[2]:


features=iris_data.data
#here all atributes of data iris flower


# In[4]:


#checkig atriutes names
iris_data.feature_names


# In[6]:


labels=iris_data.target


# In[12]:


plt.xlabel("sepal lenth")
plt.ylabel("petal lenth")
plt.scatter(features[:,0],features[:,1],label="sepal info")
plt.scatter(features[:,2],features[:,-1],label="pital info",marker='x')
plt.legend()
plt.show()


# In[13]:


#data split
triain_d,test_d,train_l,test_l=train_test_split(features,labels)
#firsttwo section of the data
#last two section of the labels


# In[15]:


triain_d.shape


# In[16]:


train_l.shape


# In[19]:


#now calling decision tree classifiers
g_clf=DecisionTreeClassifier(criterion='gini')


# In[21]:


e_clf=DecisionTreeClassifier(criterion='entropy')


# In[22]:


#now trending the data
g_trained=g_clf.fit(triain_d,train_l)


# In[23]:


e_trained=e_clf.fit(triain_d,train_l)


# In[24]:


#now predicting using gini
g_output=g_trained.predict(test_d)


# In[25]:


e_output=e_trained.predict(test_d)


# In[31]:


gacc=accuracy_score(test_l,g_output)


# In[30]:


eacc=accuracy_score(test_l,g_output)


# In[32]:


pctacc=[gacc,eacc]
math=['ginn','entropy']
plt.pie[(pctacc,labels=math,shadow=True,autopct='%1.1f%%',explode=(0,0,2))]


# In[ ]:




