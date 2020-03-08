# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:03:44 2019

@author: BITTU
"""
def findpair(arr,k):
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j]==k:
                pair=[i,j]
                
    return pair

arr=[8,6,45,96,23,47,55,21]
print("Array:\n",arr)
pair=findpair(arr,100)
print("Pair:",pair)


