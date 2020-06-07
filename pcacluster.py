#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.decomposition import PCA
from sklearn.datasets import load_iris, load_digits
import matplotlib.pyplot as plt


# In[2]:


dataset = load_iris()

X = dataset.data
y = dataset.target


# In[3]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    stratify=y, random_state=42)


# In[4]:


from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth=2, random_state=42)

clf.fit(X_train, y_train)


# In[5]:


preds = clf.predict_proba(X_test)


# In[6]:


from sklearn.metrics import accuracy_score

print(f"Accuracy score without PCA: {accuracy_score(y_test, preds.argmax(axis=1)):.2f}")


# In[7]:


pca = PCA(n_components=2)
X_centered = X - X.mean(axis=0)
pca.fit(X_centered)


# In[8]:


X_pca = pca.transform(X_centered)


# In[9]:


plt.plot(X_pca[y==0, 0], X_pca[y==0, 1], 'bo', label="Setosa")
plt.plot(X_pca[y==1, 0], X_pca[y==1, 1], 'go', label="Versicolor")
plt.plot(X_pca[y==2, 0], X_pca[y==2, 1], 'ro', label="Verginica")
plt.legend(loc=0)


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.3,
                                                    stratify=y, random_state=42)

clf = DecisionTreeClassifier(max_depth=2, random_state=42)

clf.fit(X_train, y_train)


# In[16]:


preds = clf.predict_proba(X_test).argmax(axis=1)
print(f"Accuracy score without PCA: {accuracy_score(y_test, preds):.2f}")


# In[12]:


#digit datasets
dis= load_digits()

X = dataset.data
y = dataset.target


# In[14]:


dir(dis)


# In[17]:


img=ds.images
img.shape
plt.imshow(imag[0],cmap=plt.get_cmap(nipy_spectral',5))


# In[18]:


plt.inshow(img[0],cmp=plt.cm.biary)


# In[ ]:




