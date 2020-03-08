# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:10:36 2019

@author: BITTU
"""
import collections
from collections import defaultdict
import numpy as np

arr=np.array([0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,3])
#printMajority(arr,visited)
#print(collections.Counter(arr))
dict=collections.Counter(arr)
print(dict)
#key_max = max(dict.keys(), key=(lambda k: dict[k]))
#key_min = min(dict.keys(), key=(lambda k: dict[k]))
#print("min:",key_min,"max:",key_max)
d = defaultdict(list)
for key, value in dict.items():
    print(key," ",value)
    d[value].append(key)

#print(d)
#print(type(d))
print(max(d.keys()),": ",d.get(max(d.keys())))