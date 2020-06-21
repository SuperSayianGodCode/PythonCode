# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:25:21 2020

@author: BITTU
"""
from random import randint

#create a list of play options
options=["Rock", "Paper", "Scissors"]


while True:
    #assign a random move to the computer
    computerturn = options[randint(0,len(options)-1)].lower()
    #ask user to input their move
    player = input("Rock, Paper, Scissors?").strip().lower()
    if player==computerturn:
        print("Tie!")
        continue
    elif player==options[0].lower():
        if computerturn==options[1].lower():
            print("You lose!", computerturn, "covers", player)
            print("Better Luck next time.")
        else:
            print("You win!", player, "smashes", computerturn)
            print("We have a winner!!!")
        break    
    elif player==options[1].lower():
        if computerturn==options[2].lower():
            print("You lose!", computerturn, "cuts", player)
            print("Better Luck next time.")
        else:
            print("You win!", player, "covers", computerturn)
            print("We have a winner!!!")
        break    
    elif player==options[2].lower():
        if computerturn==options[0].lower():
            print("You lose!", computerturn, "smashes", player)
            print("Better Luck next time.")
        else:
            print("You win!", player, "cuts", computerturn)
            print("We have a winner!!!")
        break
    else:
        print("That's not a valid move. Check your spelling!")
        continue