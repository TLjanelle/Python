from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
    print(f"\nPlayer score: {player_wins} \nComputer Score: {computer_wins} \n")
    print("Rock...")
    print("Paper...")   
    print("Scissors...\n")

    player = input("(Enter your choice): ").lower() 
    if player =="quit" or player == "q":
        break
    random_num = randint(0,2)
    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}.\n") 

    if player == computer:
        print("It is a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!!")
            player_wins += 1
        elif computer == "paper":
            print("Computer wins!!")
            computer_wins += 1
    elif player == "paper":
        if computer =="rock":
            print("Player wins!!")
            player_wins += 1
        elif computer == "scissors":
            print("Computer wins!!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!!") 
            player_wins += 1
        elif computer == "rock":
            print("Computer wins!!")
            computer_wins += 1
    else:
        print("Please enter a valid move")


if player_wins > computer_wins:
   print("\n CONGRATS, YOU WON!\n")
elif player_wins == computer_wins:
    print(f"ITS A TIE")
else:
    print("OH NO :( THE COMPUTER WON!")
    