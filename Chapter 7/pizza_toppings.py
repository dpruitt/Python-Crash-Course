topping = ""
while True:
    topping = input("What topping would you like on your pizza?\n")
    if topping.lower() == "quit":
        break
    print(f"Ok. I will add {topping} to your pizza.")
