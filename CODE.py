import random

print("Rock Paper Scissors Game")
print("------------------------")
print("rock beats scissors, scissors beats paper, paper beats rock\n")

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock/paper/scissors (or quit to stop): ").lower()

    if user_choice == "quit":
        print("Thanks for playing")
        break

    if user_choice not in options:
        print("Invalid choice, try again")
        continue

    comp_choice = random.choice(options)
    print("Computer chose:", comp_choice)

    if user_choice == comp_choice:
        print("It's a tie")
    elif (user_choice == "rock" and comp_choice == "scissors") \
         or (user_choice == "paper" and comp_choice == "rock") \
         or (user_choice == "scissors" and comp_choice == "paper"):
        print("You win")
    else:
        print("Computer wins")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Game ended")
        break
