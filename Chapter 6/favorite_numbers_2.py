favorite_numbers = {
    "Dylan": [1, 2, 3],
    "Luke": [2, 4],
    "Alec": [3, 9, 20],
    "Greg": [4, 17],
    "Mike": [5, 88]
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are: {str(numbers).strip('[]')}")
