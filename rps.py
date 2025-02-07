import random

print("WELCOME TO ROCK-PAPER-SCISSORS!!!!!!!")
print("---------------------------------------")
print("Basic instructions:")
print("1. You have three choices - \t○ ROCK \t ○ PAPER \t○ SCISSORS")
print(
    "2. Move to win - \n○ Rock beats Scissors \n○ Scissors beats Paper \n○ Paper beats Rock \n○If both players choose "
    "the same option then its a Tie!")
print("3. To end the game : Enter End")
print("Let's start the game!!")


def first():
    us = 0  # user-score
    cs = 0  # computer-score
    while True:
        ui = input("Enter your choice (ROCK,PAPER,SCISSORS):").lower()  # user input
        while ui not in ["rock", "paper", "scissors", "end"]:
            print("Invalid Choice... Please Try again")
            ui = input("Enter your choice (ROCK,PAPER,SCISSORS):").lower()
        if ui == "end":
            print("Thanks for playing Game!!!")
            break
        cc = random.choice(["rock", "paper", "scissors"])
        print("computer's choice:", cc)
        if ui == cc:
            print("Its a Tie..")
        elif ((ui == "rock" and cc == "scissors") or (ui == "scissors" and cc == "paper") or (
                ui == "paper" and cc == "rock")):
            result = "user"
            us = us + 1
            print("You Win....")
        else:
            result = "computer"
            cs = cs + 1
            print("Computer Win...")
        print(f"Your score:{us} and Computer score:{cs}")


first()
