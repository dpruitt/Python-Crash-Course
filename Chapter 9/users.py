class User:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def describe_user(self):
        print(f"First Name: {self.first} \nLast Name: {self.last} \nAge: {self.age}")
        
    def greet_user(self):
        print(f"Hellow {self.first} {self.last}!")


def main():
    bob = User("Bob", "Guy", 13)
    jason = User("Jason", "Bourne", 33)
    dude = User("Dude", "Bro", 69)

    bob.greet_user()
    jason.describe_user()
    dude.greet_user()


if __name__ == "__main__":
    main()
