def combine(city, country, population=""):
    return f"{city.title()}, {country.title()}{('' if population == '' else ' - population ' + str(population))}"

