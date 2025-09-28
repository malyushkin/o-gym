people = {
    "Bob": {"age": 15, "country": "Canada"},
    "Alice": {"age": 30, "country": "USA"},
    "Charlie": {"age": 25, "country": "UK"},
    "Diana": {"age": 26, "country": "Germany"},
    "Ethan": {"age": 30, "country": "Australia"}
}

# sort and keep as an ordered dict
sorted_people = dict(
    sorted(
        people.items(),
        key=lambda item: (item[1]["age"], item[1]["country"])
    )
)

print(sorted_people)
