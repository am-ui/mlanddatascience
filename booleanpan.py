# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 04:03:13 2019

@author: AMIT
"""

#accessig the indexig as boolean
import pandas as pd 
   
# dictionary of lists 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[90, 40, 80, 98]} 
   
df = pd.DataFrame(dict, index = [True, False, True, False]) 
   
print(df) 
#print only true value
print(df.loc[True]) 
#retrive the one value
print(df.iloc[1]) 
#indexing the  only value
print(df.ix[True]) 
#retrive the value using ix method
print(df.ix[1]) 