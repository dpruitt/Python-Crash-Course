people = {
    "dpruitt": {
        "first_name": "Dylan",
        "last_name": "Pruitt",
        "age": 27,
        "city": "Lansing"
    },
    "jbrown": {
        "first_name": "Jack",
        "last_name": "Brown",
        "age": 33,
        "city": "Grand Rapids"
    },
    "jbourne": {
        "first_name": "Jason",
        "last_name": "Bourne",
        "age": 90,
        "city": "Detroit"
    }
}

for person in people.values():
    for info in person.values():
        print(info)


