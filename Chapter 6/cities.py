cities = {
    "Lansing": {
        "state": "Michigan",
        "population": 1,
        "fact": "Its ok."
    },
    "Grand Rapids": {
        "state": "Michigan",
        "population": 2,
        "fact": "Its cool."
    },
    "Detroit": {
        "state": "Michigan",
        "population": 3,
        "fact": "Its not as cool."
    }
}

for name, city in cities.items():
    print(f"{name}:")
    for key, value in city.items():
        print(f"{key.title()}: {value}")
