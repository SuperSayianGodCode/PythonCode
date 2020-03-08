# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:43:09 2019

@author: BITTU
"""

import numpy as np
import math

def revKElement(arr,k):
    #print(arr)
    if k>len(arr)-1:
        return
    
    print("k:",k)
    i,j=0,(k-1)
    print(j)
    while i<=math.floor((k-1)/2) and j>=math.floor((k-1)/2):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
        
    print(arr)

arr=np.array([54,89,75,19,35,66,73,24])
print(arr)
revKElement(arr,5)

#print(a)