# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:23:57 2020

@author: BITTU
"""

def findSubArray(arr, Sum):
    
    l=0
    r=0
    maxlength=0
    calculatedSum=0
    subArray=[]
    while(l<len(arr) and r<len(arr)):
        calculatedSum+=arr[r]
        r+=1
        while(calculatedSum>Sum and l<=r):
            calculatedSum-=arr[l]
            l+=1
        if(calculatedSum==Sum and l<=r and maxlength<r-l):
            maxlength=r-l
            subArray=arr[l:r]
            
    return subArray

arr=[1,2,3,4,5,0,0,0,6,7,8,9]
print("Array:\n",arr)
subArray=findSubArray(arr,15)
print("subArrayLength:",subArray)