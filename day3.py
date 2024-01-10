"""
File: day3.py

Description:
    This script is an interactive game called 'Treasure Island'.
    The player makes choices to find the treasure. The game progresses based on
    the player's choices and ends when the player wins or encounters a 'Game Over'.


Author: WhereIsLijah
Version: 1.0
Date: 2024-01-08
"""

print("Welcome to Treasure Island, Your mission is to find the treasure")
choice = input("Left or Right: \n").lower()


if choice == 'left':
    choice = input("Swim or Wait: \n").lower()
    if choice == 'wait':
        choice = input("Which door? \n").lower()
        if choice == 'yellow':
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")