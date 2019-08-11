buffet = ("chicken", "steak", "mac and cheese", "potatoes", "corn")

print("First Menu:")
for food in buffet:
    print(food)

# uncomment the line below to cause tuple assignment error
# buffet[0] = "porkchop"

buffet = ("porkchop", "beans", "mac and cheese", "potatoes", "corn")

print("\nSecond Menu:")
for food in buffet:
    print(food)
