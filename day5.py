"""
File: day5.py

Description:
    Password Generator that takes in user input of letters symbols and numbers

Author: WhereIsLijah
Version: 1.0
Date: 2024-01-16
"""

import random as r
import string

def password_generator(no_letter, no_symbol, no_numbers):
    if no_letter + no_symbol + no_numbers < 8 or no_letter < 4:
        raise ValueError("Invalid parameters entered for password generation")

    password = (r.choices(string.ascii_letters, k = no_letter) +
                r.choices(string.punctuation, k = no_symbol) +
                r.choices(string.digits, k = no_numbers))

    r.shuffle(password)

    return ''.join(password)

def main():

    try:
        print("Welcome to the Password Generator\n")

        no_letter = int(input("How many letters would you like in your password?\n"))
        no_symbol = int(input("How many symbols would you like?\n"))
        no_numbers = int(input("How many numbers would you like?\n"))

        generated_password = password_generator(no_letter, no_symbol, no_numbers)
        print(generated_password)

    except ValueError as e:
        print(f"Failed to generate password. Please check the input parameters: {e}")

if __name__ == "__main__":
    main()
