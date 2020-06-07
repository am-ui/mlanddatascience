#!/usr/bin/env python
# coding: utf-8

# In[6]:


#knn with iris
#loading iris data 
from sklearn.datasets import load_iris
#loading another library
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


# In[8]:


iris = load_iris()


# In[9]:


#listing all data 
dir(iris)


# In[11]:


features=iris.data  #only feature of data
label=iris.target
#spliting the data
trian_x,test_x,train_y,test_y=train_test_split(features,label,test_size=0.2)


# In[12]:


#calling decision tree classifiers
d_clf=DecisionTreeClassifier()


# In[17]:


k_clf=KNeighborsClassfier()


# In[16]:


#train decision tree
train_des=d_clf.fit(train_x,train_y)


# In[ ]:


trained_knn= k_clf.fit(train_x,train_y) #trainned the knn
output_des=trained_des.predict(test_x) #predict first  data
output_knn=trained_knn.predict(test_x) #predict  second data
acc_des=accuracy_score(test_y,output_des)#checking accuracy

#knn
f=iris.data
l.iris.target
X,x,Y,y=
# In[19]:


#working with KNN and extra data
import pandas as pd
import matplotlib.pyplot as plt
#rather than matplotlib we can also use seaborn
#pip install seaborn
import seaborn as sb


# In[ ]:


get_ipython().system('date')


# In[20]:


#loading csv file
df=pd.read_csv('social.csv')
df.info()


# In[ ]:


df.head()
sb.counplot[df['Gender']]
#data analysis
#df
features=df.iloc[:,[2,3]].values
label=df.iloc[:,-1].values
#spliting data 
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_x=train_test_split(features,test_size=0.2)
#applying features scalling
from sklearn.preprocessing import StandardScaler
#applying on features scalling function
std=StandardScaler()
#applying o trainn x
train_xf=std.fit_transform(train_x)
#now applying on test_x
test_xf=std.transform(test_x)
#calling knn
from sklearn.neighborsClassifiers()
kclf=KNeighborsClassifiers()
traied_knn=kclf.fit(trained_xf,trained_y)
#predictig output
output=trained_knn.predict(test_xf)
ooutput
#to check accurity score
from sklearn.metrics import StandardScalling

