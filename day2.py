"""
File: day2.py

Description:
    This module calculates the tip based on user input for a bill

Author: WhereIsLijah
Version: 1.0
Date: 2024-01-08
"""

def tip_calculator(bill, people, tip_percent):
    tip_calc = (bill/people)
    final_tip = (tip_calc * (tip_percent/100)) + tip_calc
    return final_tip

def main():
    print("Welcome to the Tip Calculator")

    try:
        bill = float(input("What was the total bill?"))
        people = int(input("How many people to split the bill?"))
        tip_percent = int(input("what percentage tip would you like to give? 10, 12 or 15?"))

        if tip_percent not in [10, 12, 15]:
            raise ValueError("Invalid Tip percentage, Choose either 10, 12, or 15")

        amt_per_person = tip_calculator(bill, people, tip_percent)
        print(f"Each person should pay: ${amt_per_person:.1f}")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()



