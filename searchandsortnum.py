# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:44:22 2019

@author: AMIT
"""

# importing libraries
import numpy as np
 
# sort along the first axis
#a = np.array([[12, 15], [10, 1]])
#arr1 = np.sort(a, axis = 0)        
#print ("Along first axis : \n", arr1)   
#arr2= np.sort(a, axis = 1)        
#print ("Along neglect axis : \n", arr2)
#arr3= np.sort(a, axis = -1)        
#print ("Along last axis : \n", arr3)
#a2=np.array([65,58,5,68,46,57,0,94])
#print("the orignal array",a2)
#b=np.argsort(a2)
#print("the sorted array",b)
#c=np.argmax(a2)
#print("the maximum element of the araay is :",c)
#d=np.argmin(a2)
#print("the minimum element of the array is :",d)
#e=np.nanargmin(a2)
#print("the minimum element of array neglecting the nan value :",e)
#f=np.nanargmax(a2)
#print("the maximum element of the array neglecting the nan value",f)

#a = np.array([9, 3, 1, 3, 4, 3, 6])
 
 
#b = np.array([4, 6, 9, 2, 1, 8, 7]) 
#print('column a, column b')
#for (i, j) in zip(a, b):
 #   print(i, ' ', j)
 
# Sort by a then by b
#ind = np.lexsort((b, a)) 
#print('Sorted indices->', ind)
  #searching the array
#g=np.arange(12).reshape(3,4)
#print("the created array is :",g)
#h=np.argmax(g)
#print("the maximum element of creating array:",h)
#print("the maximum element using indexing :",np.argmax(g,axis=1))
#i=np.argmin(g)
#print("the minimum element of the array is :",i)
#print("the manimum element using indexing :",np.argmin(g,axis=1))





#counting the element of the array
#a = np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]])
#b = np.count_nonzero(([[0,1,7,0,0],[3,0,0,2,19]]))
 
#print("Number of nonzero values is :",a)
#print("Number of nonzero values is :",b)

import matplotlib.pyplot as plt 
  
# x co-ordinates 
x = np.arange(0, 9) 
A = np.array([x, np.ones(9)]) 
  
# linearly generated sequence 
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24] 
# obtaining the parameters of regression line 
w = np.linalg.lstsq(A.T, y)[0]  
  
# plotting the line 
line = w[0]*x + w[1] # regression line 
plt.plot(x, line, 'r-') 
plt.plot(x, y, 'o') 
plt.show()




  