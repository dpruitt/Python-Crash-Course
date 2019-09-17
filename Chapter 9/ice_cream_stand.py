from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self):
        super().__init__("I Scream", "Ice Cream")
        self.flavors = ["Vanilla", "Chocolate", "Strawberry"]

    def print_flavors(self):
        print(self.flavors)


def main():
    stand = IceCreamStand()
    stand.print_flavors()


if __name__ == "__main__":
    main()