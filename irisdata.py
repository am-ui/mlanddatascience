#creating dataset
#from sklearn import datasets
#only checking iris data 
#[i for i in dir(datasets) if 'iris' in i]
#only loading iris
#from sklearn.datasets import load_iris
#now load_iris is similar to csv file
#iris=load_iris()
#dir(iris)
#print feature name
#iris.feature_names
#printing target name
#iris.target_names
#iris.data.shape





#2nd

from sklearn.datasets import load_iris
iris=load_iris()
features=iris.data
labels=iris.target
#to div into training and testing
from sklearn.model_selection import train_test_split
#help(train_test_split)
train_test_split(features,labels,test_size=0.2)
#X is 80%data
#Y is 20%data
#x is the 80%labels
#y is the 20% of the labels
#here test size range is 0.0.......1.0
#0.1 means 100%
# X is the training data with features
# x is traing data with labels
#Y is trained data with features
#y is trained data with labels
#features_train,features_test,label_train,label_test=label_train_split
we can also use train size
X.shape
X[0]
Y.shape
x.shape
y.shape
from sklearn.tree import DecisionTreeClassifiers
clf=DecisionTreeClassifiers()
trainned=clf.fit(X,x)
output=trained.predict(y)
prin(toutput)#this is predicted ans



#tomorrow
