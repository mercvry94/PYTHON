import random

name = input("What is your name? ")
print("Hello, " + name + "!")

mylist = ["rock", "paper", "scissors"]
score = 0

while True:
    computer_action = random.choice(mylist)
    user_action = input("Enter a choice (rock, paper, scissors): ")
    print(f"{name} chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(f"Rock smashes scissors! {name} wins!")
            score += 1
        else:
            print(f"Paper covers rock! {name} loses.")
            score -= 1
    elif user_action == "paper":
        if computer_action == "rock":
            print(f"Paper covers rock! {name} wins!")
            score += 1
        else:
            print(f"Scissors cuts paper! {name} loses.")
            score -= 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print(f"Scissors cuts paper! {name} wins!")
            score += 1
        else:
            print(f"Rock smashes scissors! {name} loses.")
            score -= 1
    print(f"{name} has {score} points")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

