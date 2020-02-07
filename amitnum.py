# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:16:24 2019

@author: AMIT
"""

import numpy as np
#create an array
a=np.array([[1,2,3],[4,5,6]],dtype='float')
print("create an array:",a)
#create a null array
b=np.zeros((3,4))
print("null array",b)
#create a constant array using complex number
c=np.full((3,4),7,dtype="complex")
print("constant array using complex number",c)
#basic operation on array
a=np.array([1,2,3,4,5,6,7,8])
print("initial array:",a)
adding 1 at every element of arrray  
print("adding after array",a+1)
print("Subtracting after a array",a-3)
print("divide after array",a/2)
print("multiply",a*2)
print("the square of array",a**2)
#modifying an array
a*=2
print("after modification of array each elemennt of array multiplying by 2",a)
#create an array and its transpose 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
 
print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)
#demonstration and uniry operation 
arr=np.array([[1,3,2],
              [4,4,3],
              [7,3,4]])
print("arr")
#print maximum and minimum element of array
print("print the largest number of array",arr.max())
print("the largest number as row:",arr.max(axis=1))
print("the largest number as column:",arr.max(axis=0))
print("the minimunm number as row",arr.min())
#print sum of all elemennt of array
print("the sum of array",arr.sum())
#cumulative sum of the array
print ("Cumulative sum of each row:\n",arr.cumsum(axis = 1))
  #subtraction addition mu8ltiplicationn of two array
a=np.array([[1,2,3,4],
              [4,3,5,6]])
b=np.array([[2,3,6,5],
            [2,4,6,4]])
print("sum of the two array:",a+b)
print("the subtraction of the two array",a-b)
print("the multiplication of the two array",a*b)
 #fuction in numpy
 a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))
print("cosine value of array element :",np.cos(a))
print("the tangent value of the element:",np.tan(a))

 
