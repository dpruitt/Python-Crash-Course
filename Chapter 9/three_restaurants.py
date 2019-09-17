class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name: {self.name} \nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open!")


ravioli = Restaurant("Ravioli Ravioli", "Italian")
ravioli.describe_restaurant()

mexico = Restaurant("Mexican Restaurant", "Mexican")
mexico.describe_restaurant()

japanese = Restaurant("Japan", "Japanese")
japanese.describe_restaurant()
