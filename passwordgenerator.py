# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 02:40:49 2020

@author: BITTU
"""

import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
  
#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter1=chr(random.randint(65,90)) 
#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) 
#Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122))
#Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122))
#Generate a random digit (based on ASCII code)
digit1=chr(random.randint(48,57))
#Generate a random digit (based on ASCII code)
digit2=chr(random.randint(48,57))
#Generate a random special character (based on ASCII code)
spchar1=chr(random.randint(33,47))
#Generate a random special character (based on ASCII code)
spchar2=chr(random.randint(33,47))

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + spchar1 + spchar2
print(password)
password = shuffle(password)

#Ouput
print(password)