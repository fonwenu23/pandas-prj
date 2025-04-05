import random

def number():
    print(f"Hello, Welcome to the game")
    x = 1
    y = 9
    #choice = int(input(f"Guess a number between {x} and {y}?: "))
    result = random.randint(x, y)
    while True:
        try:
            choice = int(input(f"Guess a number between {x} and {y}: "))
            if choice ==  result:
                print(f"you win, the magic number was {choice}")
                break
            elif choice > result:
                print(f"lower")
            else: 
                choice < result
                print(f"higher")
        except ValueError:
            print("Enter a valid number")
number()
