#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris

iris = load_iris()


# In[2]:


from sklearn.ensemble import RandomForestClassifier

# Limit max depth
model = RandomForestClassifier(max_depth = 3, n_estimators=10)

# Train
model.fit(iris.data, iris.target)
# Extract single tree
estimator_limited = model.estimators_[5]
estimator_limited


# In[3]:


model = RandomForestClassifier(max_depth = None, n_estimators=10)
model.fit(iris.data, iris.target)
estimator_nonlimited = model.estimators_[5]


# In[12]:


from sklearn.tree import export_graphviz
export_graphviz(estimator_limited, out_file='tree_limited.jpg', feature_names = iris.feature_names,
                class_names = iris.target_names,
                rounded = True, proportion = False, precision = 2, filled = True)


# In[13]:


export_graphviz(estimator_nonlimited, out_file='tree_nonlimited.jpg', feature_names = iris.feature_names,
                class_names = iris.target_names,
                rounded = True, proportion = False, precision = 2, filled = True)


# In[6]:


#!dot -Tpng tree_limited.dot -o tree_limited.png -Gdpi=600


# In[14]:


from IPython.display import Image
Image(filename = 'tree_limited.jpg')


# In[8]:


get_ipython().system('dot -Tpng tree_nonlimited.dot -o tree_nonlimited.png -Gdpi=600')


# In[15]:


Image(filename = 'tree_nonlimited.jpg')


# In[ ]:




