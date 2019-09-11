import random

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = 0
        self.keep = False

    def roll(self):
        self.value = random.randrange(1, self.sides + 1)

    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Dice:
    def __init__(self, list):
        self.dice = []
        for number in list:
            self.dice.append(Die(number))

    def roll_dice(self):
        for die in self.dice:
            die.roll()

dice = Dice([6, 6, 6, 6, 6])

for x in range(1, 2):
    dice.roll_dice()
    dice.dice.sort(key=lambda x: x.value)
    print(dice.dice)
    choices = input("Which dice do you want to keep?\n")
    print(choices)

