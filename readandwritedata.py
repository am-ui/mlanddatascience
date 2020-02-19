# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 04:21:08 2019

@author: AMIT
"""

import xlrd
 
loc = (r'C:\Users\AMIT\Desktop\diamond.csv') 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

sheet.cell_value(0, 0) 