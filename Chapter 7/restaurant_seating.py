guests = input("How many people are in the dinner group?\n")
guests = int(guests)

if guests > 8:
    print("You will need to wait for a table.")
else:
    print("Your table is ready.")
