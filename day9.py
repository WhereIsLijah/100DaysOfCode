"""
File: day9.py

Description:
    Secret Auction

Author: WhereIsLijah
Version: 1.0
Date: 2024-02-01
"""

def main():
    choice = True
    bids = {}
    while choice:
        name = str.strip(input("What is your name?"))
        bid = float(input("What's your bid?"))

        bids[name] = bid

        choice = input("Are there any other bidders? (yes/no) \n").lower()
        if choice == 'no':
            choice = False

    max_bid = max(bids.values())

    winner = ''.join([key for key, value in bids.items() if value == max_bid])

    print(f"The winner is {winner} with a bid of {max_bid}")


if __name__ == '__main__':
    main()
