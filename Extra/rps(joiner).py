import random

weapons = ('r', 'p', 's')
while True:
    player1 = input(f"Choose your weapon: \n(R)ock, (P)aper, (S)cissors, (Q)uit\n> ").lower()
    if player1 == 'q':
        break
    elif player1 not in weapons:
        print("Please enter a valid option.\n")
    else:
        computer = weapons[random.randrange(0, 3)]
        print(f"Computer chooses {computer}\nPlayer chooses {player1}")
        if player1 == computer:
            print("There is a tie.")
        elif weapons[weapons.index(player1) - 1] == computer:
            print("Player wins!")
        else:
            print("Computer wins!")
print("Thanks for playing!")