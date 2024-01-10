"""
File: day4.py

Description:
    A rock, paper and scissors game


Author: WhereIsLijah
Version: 1.0
Date: 2024-01-08
"""
import random


def rps(user_choice):
    game_options = ['rock', 'paper', 'scissors']
    ai_choice = random.choice(game_options)

    if user_choice == ai_choice:
        return f'User Played: {user_choice} and AI played: {ai_choice}, It is a Tie'
    elif (user_choice == 'rock' and ai_choice == 'scissors') or \
            (user_choice == 'paper' and ai_choice == 'rock') or \
            (user_choice == 'scissors' and ai_choice == 'paper'):
        return f'User Played: {user_choice} and AI played: {ai_choice}, User wins Game!'
    else:
        return f'User Played: {user_choice} and AI played: {ai_choice}, AI wins Game!'


def main():
    try:
        user_choice = input("Rock, Paper or Scissors?\n").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            raise ValueError("Invalid Choice!")
        else:
            game_result = rps(user_choice)
            print(game_result)

    except ValueError as e:
        print(f"Wrong Choice made: {e}")


if __name__ == "__main__":
    main()
