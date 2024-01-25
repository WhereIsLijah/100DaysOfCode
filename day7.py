"""
File: day7.py

Description:
    Caesar Cipher

Author: WhereIsLijah
Version: 1.0
Date: 2024-01-18
"""

# Program should Decode and Encode
# Shift determines how the alphabets shift

#create mapping for alphabets
#get input and attach number to each letter
#add key to each number of letter
#find corresponding alpha


import string
def caesar_cipher(plaintext, key):
    alphabet_mapping = [letter for letter in string.ascii_lowercase]

    for i in plaintext:
        alphabet_mapping


def main():
    # try:
        # print("Do you want to Encode or Decode")

    plaintext = input("Enter the Plaintext: ")
    key = input("Enter the Shift Number: ")

    caesar_cipher(plaintext, key)

    # except:



if __name__ == '__main__':
    main()