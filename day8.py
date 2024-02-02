"""
File: day8.py

Description:
    Caesar Cipher

Author: WhereIsLijah
Version: 1.0
Date: 2024-01-18
"""
import string

def caesar_cipher1(choice, plaintext, key):
    if choice == 'decode':
        key = -key
    # creating a new list of where the cipher_text will be stored
    cipher_text = []

    # looping over all the characters in plaintext
    for char in plaintext:
        # checking if character is alphabet
        if char.isalpha():
            # setting the base of the Ascii values with values for both cases
            ascii_offset = ord('a') if char.islower() else ord('A')
            # creating the shift of characters by subtracting the current character from the offset i.e a/A
            # and adding the key before using the modulus operator  by the number of letters of the alphabet
            # and reconverting to the ascii value
            shifted = ((ord(char) - ascii_offset + key) % 26) + ascii_offset
            # converting the ascii value to character before storing the ascii character
            cipher_text.append(chr(shifted))
        else:
            # appending non-alphabets
            cipher_text.append(char)
    return ''.join(cipher_text)


def caesar_cipher(choice, plaintext, key):
    # changing thr shift of the key if user's choice is to encode
    if choice == 'decode':
        key = -key

    # using a list comprehension to create a new list of lower alphabet letters [a, b, c,...]
    alphabet_mapping = [letter for letter in string.ascii_lowercase]

    # creating a new alphabet_hashmap to store letters and their corresponding indices
    alphabet_hashmap = {}
    for index, value in enumerate(alphabet_mapping):
        alphabet_hashmap[value] = index
    # creating an empty string variable to store the resulting encoded/decoded text
    cipher_text = ""

    # Looping through the plaintext by each index and character
    for index, value in enumerate(plaintext):
        # checking if value is present in the alphabet hashmap
        if value in alphabet_hashmap.keys():
            # using mod to loop over the alphabet hashmap incase the shift key is higher than index 25
            shift_key = (alphabet_hashmap[value] + key) % 26
            # creates a new list of character found at a certain index if it is equal to the shift key
            keys_with_value = ''.join([key for key, value in alphabet_hashmap.items() if value == shift_key])
        else:
            cipher_text += value
        cipher_text += keys_with_value
    return cipher_text

# entry point of program, gets user inputs and calls a function to verify input
def main():
    try:
        choice = str.strip(input("Do you want to Encode or Decode?\n").lower())
        if choice not in ['encode', 'decode']:
            raise ValueError

        plaintext = input("Enter the Plaintext: ")
        key = int(input("Enter the Shift Number: "))
        print(f"The {choice}d text is: {caesar_cipher1(choice, plaintext, key)}")

    except ValueError:
        print(f'Error: Invalid input. Please ensure your choices are correct and the shift number is an integer.')


if __name__ == '__main__':
    main()