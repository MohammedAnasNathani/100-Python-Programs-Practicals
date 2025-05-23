import random

choices = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Enter rock, paper, or scissors (or 'n' to quit): ").lower()
    if player_choice == 'n':
        break
    elif player_choice not in choices:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")
