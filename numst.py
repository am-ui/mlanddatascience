# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:10:15 2019

@author: AMIT
"""

import numpy as np
#lower and upper
#print(np.char.lower(["AMIT","KUMAR"]))
#print(np.char.upper(["amit kumar"]))
#spliting
print(np.char.split("amit kumar pathak"))
print(np.char.split('amit kumar pathak',sep=","))
print(np.char.join("@","amit kumar pathak"))
