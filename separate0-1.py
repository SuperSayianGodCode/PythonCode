# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 07:28:34 2019

@author: BITTU
"""


arr=[0,1,1,0,0,0,1,0,1,1,1,0,0]
temp=[0 for i in range(len(arr))]

print(arr)
print(range(len(arr)))
j=0
for i in range(len(arr)):
    if(arr[i]==0):
        temp[j]=arr[i]
        j+=1
        
for i in range(len(arr)):
    if(arr[i]==1):
        temp[j]=arr[i]
        j+=1
    
    
print(temp)

'''

import numpy as np

a=np.array([0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,0])
b=[]
b.extend(a[a==0])
b.extend(a[a==1])
print(b)

'''