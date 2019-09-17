import random

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
winner = ""

for x in range(0, 4):
    winner += str(lottery[random.randrange(0, 15)])

print(f"The winning lottery combination is {winner}.")
