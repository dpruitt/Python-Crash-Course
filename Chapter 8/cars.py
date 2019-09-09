def make_car(manufacturer, model, **car):
    car["manufacturer"] = manufacturer
    car["model"] = model
    return car


car = make_car("Subaru", "Forester", year=2010, color="black")
print(car)