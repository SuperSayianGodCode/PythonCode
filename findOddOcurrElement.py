# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:38:38 2019

@author: BITTU
"""
import collections
from collections import defaultdict
import numpy as np
    
oddOcurr=[]   
arr=np.array([0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,3])
dict=collections.Counter(arr)
print(dict)
d = defaultdict(list)
#for key, value in dict.items():
#    print(key," ",value)
#    d[value].append(key)

for key, value in dict.items():
    if value%2!=0:
        oddOcurr.append([key,value])

print(oddOcurr)

