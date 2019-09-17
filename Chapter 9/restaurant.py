class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Name: {self.name} \nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open!")


def main():
    my_restaurant = Restaurant("Ravioli Ravioli", "Italian")
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

if __name__ == "__main__":
    main()
