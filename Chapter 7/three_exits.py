# conditional test
age = 0
while age > 0:
    age = input("How old are you?\n")
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

# counter
age = 0
count = 0
while count < 3:
    age = input("How old are you?\n")
    age = int(age)
    count += 1
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

# quit
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
