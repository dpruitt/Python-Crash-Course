name = input("What is your name?\n")

with open('guest.txt', 'w') as file:
    file.write(name)

