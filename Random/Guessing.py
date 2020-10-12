import random

random_number = random.randint(1,10)

guess = None

while guess != random_number:
    guess = input(f"Pick a number from 1 to 10: \n")
    guess = int(guess)
    if guess == random_number:
        print(f"YOU GOT IT!")
    elif guess < random_number:
        print(f"TOO LOW!")
    else:
        print(f"TOO HIGH!")

print(random_number)