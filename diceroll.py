import sys
import random


def diceroll(n=1):
	minrange=n
	maxrange=n+6
	result = random.randint(minrange, maxrange)
	print("dice has been rolled... your lucky number is:", result)
	
	
	
dicetype=int(input("1.Do you want a standard dice:\n2.Customize and give your own range:\n"))	
if dicetype == 1 :
	diceroll()
elif 	dicetype == 2 :
	min=int(input("Enter the minimum value:"))
	diceroll(n=min)
else :
	print("invalid option. try again!!!!")
	