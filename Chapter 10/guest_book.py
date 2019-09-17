name = ""

with open('guest_book.txt', 'a') as file:
    while True:
        name = input("What is your name?\n")
        if name == "q":
            break
        file.write(name + "\n")
