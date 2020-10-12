import random

random_number = random.randint(1,10)

while True:
    guess = input(f"Pick a number from 1 to 10: \n")
    guess = int(guess)
    if guess < random_number:
        print(f"TOO LOW!")
    elif guess > random_number:
        print(f"TOO HIGH!")
    else:
        print(f"YOU WON!!!")
        play_again = input("Do you want to play again? (y/n) \n")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!:)")
            break