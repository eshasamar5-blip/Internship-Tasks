
import random

choice = ["Rock", "Paper", "Scissor"]

while True:
    user = input(
        "Make your choice (Rock, Paper, Scissor)\n"
        "You can use Rock, rock, R, r for Rock\n"
        "Paper, paper, P, p for Paper\n"
        "Scissor, scissor, S, s for Scissor\n"
        "Type 'end' to exit:\n"
        "YOUR CHOICE="
    )

    if user.lower()=="end":
        print ("Game Over!")
        break

    if user.lower() == "r":
        user = "Rock"
    elif user.lower() == "p":
        user = "Paper"
    elif user.lower() == "s":
        user ="Scissor"

    else:
        user = user.capitalize()
    if user not in choice:
        print ("Invalid choice! Try again...")
        continue

    computer = random.choice(choice)

    print ("You chose:", user)
    print ("Computer chose:", computer)

    if user == computer:
        print ("It is a Tie!")

    elif user == "Rock" and computer =="Scissor":
        print ("You Win!")

    elif user == "Paper" and computer == "Rock":
        print("You Win!")

    elif user == "Scissor" and computer == "Paper":
        print ("You Win!")

    else:
        print ("You Lose!")

