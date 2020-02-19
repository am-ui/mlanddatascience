# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:11:54 2019

@author: AMIT
"""

import numpy as amit
#a=amit.array([[1,3,5],
 #             [4,6,7],
 #             [7,8,4]])
#print("rank of matrix a is:",amit.linalg.matrix_rank(a))
#print("determinant of matrix a is:",amit.linalg.det(a))
#print("inverse of the matrix a is:",amit.linalg.inv(a))
#print("trace of the matrix a is:",amit.trace(a))
#print("power increase of 3 of matrix a is:",amit.linalg.matrix_power(a,3))
#find eigon value
#b=amit.array([[2,-5j],
 #             [3-6j]])
#print(b)
#x,y=amit.eigh(b)
#print("eigon value of x is:",x)
#print("eigon value of y is:",y)
#compute the eigon value
#from numpy import linalg as amit1
#c=amit.diag(1,2,3)#create array using diag function
#print(c)
#x1,y1=amit.eigh(c)
#print("the eigon value of x1 and y1 is :",x1,y1)
#dot product and scalar product
#c=amit.dot(9,6)
#print("the dot product of c is:",c)
#d=(3+4i)
#e=(6+7i)
#final product=amit.dot(d,e)
#print("the vector product of d and e is:"final product)
#f=amit.array([[2,3,4],
 #             [6,4,8]])
#g=amit.array([6,8,5])
#h=amit.solve.linalg(f,g)
#print("the solution of the both array is:",h)
 import matplotlib.pyplot as plt
 #i=amit.arange(0,9)
 #j=amit.array(i,amit.ones(9))
 #k=[24.4,56,67.8,76,67,47.5,78.9,78.45]
 #l=amit.linalg.Istsq(j.t,i)[0]
 #line=l[0]+l[1]#ploting the line
 #plt.plot(i,line,'r-')
 #plt.plot(i,k,'o')
 #plt.show()
mport matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()
