"""
File: day7.py

Description:
    Hangman

Author: WhereIsLijah
Version: 1.0
Date: 2024-01-18
"""

# - Generate random words
# - Generate as many blanks
# - Ask user to guess:
#     - If letter is correct then fill up blanks
#         repeat loop
#     - If letter is wrong then reduce a life
#
# 6 incorrect guesses

import random

def word_list():
    words = ["SLAPS", "COCONUT", "TREE", "LAPTOP"]
    return random.choice(words)

def create_blanks(chosen_word):
    return ['_'] * len(chosen_word)

def game_logic(word_entry, chosen_word, word_blank, life):
    if len(word_blank) != 1 and not word_entry.isalpha():
        print("Please enter a 'Single' Alphabet")
        return life, word_blank

    occurrences = find_occurrences(chosen_word, word_entry)
    if not occurrences:
        life -= 1

        print(f"life is: {life}")
        print(word_blank)
        return life
    else:
        return fill_blank(word_entry, occurrences, word_blank, life)


def find_occurrences(s, char):
    return [index for index, c in enumerate(s) if c == char]


def isListFilled(word_blank):
    return '_' not in word_blank


def fill_blank(word_entry, occurrences, word_blank, life):
    print(f"fill_blank: {word_entry}")
    for i in range(len(occurrences)):
        if isListFilled(word_blank) is True:
            print(word_blank)
            life = 0
            return life, 'Game Over!'
        elif word_blank[occurrences[i]] == '_':
            for i in range(len(occurrences)):
                word_blank[occurrences[i]] = word_entry
                print(word_blank)
            return word_blank
        else:
            return word_blank, "You already guessed that letter, try a different one!."
    print(word_blank)


def user_input(chosen_word, word_blank):
    life = 6
    while life > 0:
        print(f"life remaining: {life}")
        word_entry = input("Guess a letter: ").upper()
        # word_guess(word_entry)
        life, word_blank = game_logic(word_entry, chosen_word, word_blank, life)


        if life == 0:
            print("Game over!")
            break


def main():
    chosen_word = word_list()
    word_blank = create_blanks(chosen_word)
    print(chosen_word)
    print(word_blank)
    user_input(chosen_word, word_blank)


if __name__ == "__main__":
    main()

# convert game to ClI
