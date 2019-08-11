pets = {
    "Myrtle": {
        "owner": "Dylan",
        "age": 3
    },
    "Rufus": {
        "owner": "Leona",
        "age": 9
    },
    "Greg's Dog": {
        "owner": "Greg",
        "age": 1
    }
}

for pet, info in pets.items():
    print(pet)
    for value in info.values():
        print(value)

