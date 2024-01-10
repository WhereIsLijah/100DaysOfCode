# Treasure Island

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