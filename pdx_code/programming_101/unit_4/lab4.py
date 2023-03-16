import random

print("Welcome to Rock, Paper, Scissors!\n")

options = ['rock', 'paper', 'scissors']

for option in options:
    print(option)

choice = input("\nPlease choose one: \n")

computer_choice = random.choice(options)

if choice == computer_choice:
    message = "It's a tie!"

elif (choice == "rock" and computer_choice == "paper") or (choice == "paper" and computer_choice == "scissors") or (choice == "scissors" and computer_choice == "rock"):
    message = "You lose!"

elif (choice == "rock" and computer_choice == "scissors") or (choice == "paper" and computer_choice == "rock") or (choice == "scissors" and computer_choice == "paper"):
    message = "You win!"

print(f"\nYou chose {choice} and the computer chose {computer_choice}. {message}\n\n")

