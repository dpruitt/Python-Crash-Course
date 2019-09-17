from random import randrange

class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randrange(1, self.sides + 1)


def main():
    d6 = Die(6)
    d10 = Die(10)
    d20 = Die(20)

    for x in range(0, 10):
        print(f"Rolling d6: {d6.roll_die()}")
        print(f"Rolling d10: {d10.roll_die()}")
        print(f"Rolling d20: {d20.roll_die()}")


if __name__ == "__main__":
    main()