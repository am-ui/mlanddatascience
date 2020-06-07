#!/usr/bin/env python
# coding: utf-8

# In[4]:


#handling data
import pandas as pd


# In[5]:


#loading datasets
df=pd.read_csv(r'C:\Users\AMIT\Downloads\mallanalysis.csv')


# In[17]:


#priting top five data
df.head()
#by manual analysis we have to decide the right column
usefull_understooddata=df.iloc[:,[3,4]].values
#now finding the nnumber of cluster and analysing ai by elbow method
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#analysig kmeans
#KMeans()
wcss=[]
#lets assume max number of cluster is 10
for i in range(1,11):
    #kmeans algo is being used
    mykm=KMeans(n_clusters==i)
    #now applying this state to data
    mykm.fit(usefull_data)
             #inertia means summry of formula
    wcss.append(mykm.Inertia_) 
    print(wcss)
#ploting graph number of cluster v/s wcss
plt.plot(range(1,11),wcss,label="wcss with cluster no using K-means++")
plt.legend()
plt.show()
    


# In[ ]:





# In[ ]:




