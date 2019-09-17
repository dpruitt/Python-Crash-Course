from users import User
from privileges import Privileges


class Admin(User):

    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.privileges = Privileges(["can add post", "can delete user", "can ban user"])


def main():
    user = Admin("Power", "Hungry", 200)
    user.privileges.show_privileges()


if __name__ == "__main__":
    main()