def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'


print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("munich", "germany"))
