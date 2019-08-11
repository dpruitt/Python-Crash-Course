sandwich_orders = ["Ham", "Turkey", "Roast Beef"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I am making your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
