"""
File: day10.py

Description:
    Calculator

Author: WhereIsLijah
Version: 1.0
Date: 2024-02-02
"""


def calculator(first_num, operation, second_num):
    if operation == '+':
        return first_num + second_num
    elif operation == '-':
        return first_num - second_num
    elif operation == '*':
        return first_num * second_num
    elif operation == '/':
        return first_num / second_num
    else:
        return "Choose an appropriate Operator!"

def main():
    
    first_num = float(input("What's the first number: "))
    print("\n+\n-\n*\n/\n")
    operation = input("\nPick an operation:").strip()
    second_num = float(input("\nWhat's the second number:"))

    print(f"The answer is: {calculator(first_num, operation, second_num)}")


if __name__ == '__main__':
    main()