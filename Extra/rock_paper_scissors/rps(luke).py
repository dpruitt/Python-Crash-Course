import random

if __name__ == 'main':
    rpslist = ('r', 'p', 's', 'q')
    victorycondition = {'r': 's', 's': 'p', 'p': 'r'}
    while True:
        player1 = input(f"Choose your weapon: \n(R)ock, (P)aper, (S)cissors, (Q)uit\n> ").lower()
        if player1 not in rpslist:
            print("Please enter a valid option.\n")
        elif player1 == 'q':
            break
        else:
            computer = rpslist[random.randrange(0, 3)]
            print(f"Computer chooses {computer}\nPlayer chooses {player1}")
            if player1 == computer:
                print("There is a tie.")
            else:
                if victorycondition.get(player1) == computer:
                    print("Player wins!")
                elif victorycondition.get(computer) == player1:
                    print("Computer wins!")
    print("Thanks for playing!")