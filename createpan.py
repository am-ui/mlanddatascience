# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 03:43:12 2019

@author: AMIT
"""

import pandas as pd
#create dataframe
am=['amit','kumar','pathak','bihar','chhapra','maashrakh']
df=pd.DataFrame(am)
print(df)
am1={'name':['amit','kumar','pathak','bihar'],
     'age':['20','19','21','22']}
amit1=pd.DataFrame(am1)
print(amit1)
#dealing with rows ad column
am2={'name':['amit','abhishek','aditya','ankit','aryan','amritansh','anshool'],
     'age':['18','19','20','21','22','23','24'],
     'qualification':['b.tech','bsc','bca','mca','diploma','doctrate','pharmacy'],
     'address':['bihar','patna','bhagalpur','muzaffarpur','darbhanga','begusaray','danapur']}
amit2=pd.DataFrame(am2)
print(amit2[['name','address']])
am3={'name':['amit','abhishek','aditya','ankit','aryan','amritansh','anshool'],
   'age':['18','19','20','21','22','23','24'],
     'qualification':['b.tech','bsc','bca','mca','diploma','doctrate','pharmacy'],
     'address':['bihar','patna','bhagalpur','muzaffarpur','darbhanga','begusaray','danapur']}
amit3=pd.DataFrame(am3)
print=(amit3)
#read the data using pandas dataframe
data = pd.read_csv("C:\Users\AMIT\Desktop\diamond.csv")
#print the specific value of data as ideal and fair 
first==data.loc("ideal")
second=data.loc("fair")
print(first )#\n\n\n second)
print(second)
  
# dropping passed columns 
data.drop(["x", "y"], axis = 1, inplace = True) 
  
 #display 
print(data)
# retrieving row by loc method 
first = data.loc["x"] 
second = data.loc["y"] 
  
  
print(first, "\n\n\n", second)
#dealing with the missing data
import numpy as np
data1={'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
amit=pd.DataFrame(data1)
print(amit.isnull())
#fill the null value
print(amit.fillna(2))
#drop the null value
print(amit.dropna())

 
