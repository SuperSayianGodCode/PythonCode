# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:15:21 2019

@author: BITTU
"""
import collections
from collections import defaultdict
import numpy as np

## Function to find the candidate for Majority 
#def findCandidate(arr):
#    
#    n=len(arr)
#    max_index=0
#    count=0
#    for i in range(n):
#        if arr[max_index]==arr[i]:
#            count+=1
#        else:
#            count-=1
#        
#        if count==0:
#            max_index=i
#            count=1
#            
#            
#    return arr[max_index]
#
## Function to check if the candidate occurs more than n/2 times 
#def isMajority(arr, candidate): 
#    
#    count = 0
#    n=len(arr)
#    for i in range(n): 
#        if arr[i] == candidate: 
#            count += 1
#    if count > n/2: 
#        return True
#    else: 
#        return False

# Function to print Majority Element 
def printMajority(arr,visited): 
    # Find the candidate for Majority 
#    candidate = findCandidate(arr) 
#      
#    # Print the candidate if it is Majority 
#    if isMajority(arr, candidate) == True: 
#        print(candidate) 
#    else: 
#        print("No Majority Element")
    elem=[]
    n=len(arr)
    for i in range(n-1):
        count=0
        if visited[i]==1:
            continue
        
        for j in range(i,n-1):
            if arr[i]==arr[j]:
                count+=1
                
        visited[i]=1       
        elem.append([i,count])
        
    return elem
       
#arr=[0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
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

print(d)
print(type(d))
print(max(d.keys()),": ",d.get(max(d.keys())))