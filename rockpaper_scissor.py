import random

print("rock paper or scissor game")
player1 = input("Enter your option: ")

choice = ["rock", "paper", "scissor" ]

player2 = random.choice(choice)

def game(p1, p2):
    if p1 == p2:
        print("Its a tie")

    elif p1 =="rock":
        if p2 == "scissor":
            print("Rock Wins")
        else:
            print("Paper Wins")

    elif p1 == "scissor":
        if p2 == "paper":
            print("Scissor Wins")
        else:
            print("Rock Wins")

    elif p1 == "paper":
        if p2 == "rock":
            print("Paper Wins")
        else:
            print("Scissor Wins")


game(player1, player2)