def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(ingredient)


make_sandwich("turkey", "ham", "roast beef", "cheese")
make_sandwich("ham", "cheese")
make_sandwich("turkey", "lettuce", "cheese")