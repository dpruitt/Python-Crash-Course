age = 0
while True:
    age = input("How old are you?\n")
    if age.lower() == "quit":
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
