import random

rpslist = ('r', 'p', 's')

while True:
    computer = rpslist[random.randrange(0, 3)]
    player1 = input(f"Choose your weapon: \n{rpslist}\n> ").lower()
    if player1 not in rpslist:
        print("Please enter a valid option.\n")
    else:
        if player1 == computer:
            print(f"Computer chooses {computer}")
            print("There is a tie.")
            continue
        else:
            print(f"Computer chooses {computer}")
            if player1 == "r" and computer == "s":
                print("Player 1 wins!")
            if player1 == "s" and computer == "p":
                print("Player 1 wins!")
            if player1 == "p" and computer == "r":
                print("Player 1 wins!")
            if computer == "r" and player1 == "s":
                print("Computer wins!")
            if computer == "s" and player1 == "p":
                print("Computer wins!")
            if computer == "p" and player1 == "r":
                print("Computer wins!")

