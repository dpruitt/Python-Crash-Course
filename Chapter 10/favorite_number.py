import json

number = input("What is your favorite number?\n")

with open('favorite_number.json', 'w') as file:
    json.dump(number, file)
    print(f"We saved your favorite number as {number}")

