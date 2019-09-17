import json

with open('favorite_number.json') as file:
    number = json.load(file)
    print(f"We remember your favorite number, its {number}")