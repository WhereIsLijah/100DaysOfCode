"""
File: day7.py

Description:
    Caesar Cipher

Author: WhereIsLijah
Version: 1.0
Date: 2024-01-18
"""
#create ceaser cipher with a twist, put it in reverse


import string
def caesar_cipher(choice, plaintext, key):
    alphabet_mapping = [letter for letter in string.ascii_lowercase]

    hashmap = {}
    for index, value in enumerate(alphabet_mapping):
        hashmap[value] = index
    cipher_text = ""

    if choice == 'decode':
        key *= -1

    for index, value in enumerate(plaintext):
        if value in hashmap.keys():
            shift_key = (hashmap[value] + key) % 26
            keys_with_value = ''.join([key for key, value in hashmap.items() if value == shift_key])
            cipher_text += keys_with_value
    return cipher_text

def user_choice(choice, plaintext, key):
    if choice != 'encode' and choice != 'decode':
        raise ValueError("Invalid Input")
    else:
        result = caesar_cipher(choice, plaintext, key)
        return result

def main():
    try:
        choice = input("Do you want to Encode or Decode?\n").lower()
        plaintext = input("Enter the Plaintext: ").lower()
        key = int(input("Enter the Shift Number: "))

        print(f"The {choice}d text is: {user_choice(choice, plaintext, key)}")


    except ValueError as e:
        print(f"{e}, You can either Encode or decode!")



if __name__ == '__main__':
    main()