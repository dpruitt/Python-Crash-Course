class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name: {self.name} \nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served = self.number_served + increment


my_restaurant = Restaurant("Ravioli Ravioli", "Italian")
my_restaurant.set_number_served(10)
my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)
