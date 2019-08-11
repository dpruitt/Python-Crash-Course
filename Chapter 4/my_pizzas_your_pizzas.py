pizzas = ["Cheese", "Pepperoni", "Sausage"]
friend_pizzas = pizzas[:]

pizzas.append("Bacon")
friend_pizzas.append("Pineapple")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

