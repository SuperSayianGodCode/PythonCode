#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:49:44 2020

@author: rahul
"""

def gcd(a,b):
#    print("Inside gcd func:a=",a," b=",b)
    if len(b)==1:
#        print("inside if:",b)
#        print("len(b):",len(b))
        if(b[0]==0): 
            return a 
        else: 
#            tmp=a%b[0]
#            res = [int(x) for x in str(tmp)] 
            return gcd(b[0],[a%b[0]])
    elif len(b)==0:
        return a
    else:
#        print("Inside else:a=",a," b=",b)
#        print("len(b):",len(b))
        return gcd(b[0],b[1:])
        
arr=[3,4,29,64,11,73]       
print(gcd(arr[0],arr[1:]))
