rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Rhine": "Germany"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
