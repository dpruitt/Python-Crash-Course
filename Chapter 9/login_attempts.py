class User:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first} \nLast Name: {self.last} \nAge: {self.age}")

    def greet_user(self):
        print(f"Hellow {self.first} {self.last}!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0


jason = User("Jason", "Bourne", 33)
print(jason.login_attempts)
jason.increment_login_attempts()
print(jason.login_attempts)
jason.reset_login_attempts()
print(jason.login_attempts)
