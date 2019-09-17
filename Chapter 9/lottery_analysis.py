import random

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
my_ticket = "1234"
winner = ""
number_of_draws = 0

while not my_ticket == winner:
    winner = ""
    for x in range(0, 4):
        winner += str(lottery[random.randrange(0, 15)])
    number_of_draws += 1

print(f"You won the lottery. It only took {number_of_draws} tries.")
