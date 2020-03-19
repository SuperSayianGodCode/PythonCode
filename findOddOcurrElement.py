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

##################################################################################################3

import numpy as np
oddOcurr=[] 
occurCount={}
arr=np.array([0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,3])
visited=np.array([False for i in range(len(arr))])
for i in range(len(arr)):
    for j in range(len(arr)):
        if (arr[i]==arr[j] and visited[j]==False):
            if (arr[j] in occurCount):
                occurCount[arr[j]]+=1
            else:
                occurCount[arr[j]]=1
            visited[j]=True   
        else:
            continue
            
print(occurCount)

for key in occurCount:
    if occurCount[key]%2!=0:
       print(key,": ",occurCount[key])
