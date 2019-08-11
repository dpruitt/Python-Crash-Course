favorite_places = {
    "Dylan": ["US", "Canada", "Mexico"],
    "Bob": ["Japan"],
    "Jack": ["France", "Germany", "Spain"]
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: {', '.join(places)}")

