cities = {
    "Lansing": {
        "state": "Michigan",
        "population": 1,
        "fact": "Its ok.",
        "age": 100
    },
    "Grand Rapids": {
        "state": "Michigan",
        "population": 2,
        "fact": "Its cool.",
        "age": 200
    },
    "Detroit": {
        "state": "Michigan",
        "population": 3,
        "fact": "Its not as cool.",
        "age": 300
    }
}

for name, city in cities.items():
    print(f"\n{name}:")
    for key, value in city.items():
        print(f"\t{key.title()}: {value}")
