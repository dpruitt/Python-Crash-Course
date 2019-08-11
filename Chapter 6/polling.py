favorite_languages = {
    "Jen": "Python",
    "Sarah": "C",
    "Edward": "Ruby",
    "Phil": "Python"
}

people = ["Phil", "Dylan", "Ben", "Sarah"]

for person in people:
    if person in favorite_languages.keys():
        print(f"Thanks for taking the poll already, {person}.")
    else:
        print(f"Please go take the poll, {person}.")
