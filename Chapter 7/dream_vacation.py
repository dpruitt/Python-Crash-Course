places = []
place = ""

while True:
    place = input("If you could visit one place in the world, where would you go?\n")
    if place.lower() == "quit":
        break
    places.append(place)

print("Here is where everyone you would go:")
for place in places:
    print(place.title())
