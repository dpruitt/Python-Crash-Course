sandwich_orders = ["Pastrami", "Ham", "Turkey", "Pastrami", "Roast Beef", "Pastrami"]
finished_sandwiches = []

print("We have run out of pastrami. Sorry.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I am making your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
