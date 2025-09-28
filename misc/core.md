## Dict

[dict.py](dict.py)

### Sorting a Dictionary by a Custom Value

There is a way to **sort a dictionary by a custom value**: use `dict.items()` for `(key, value)` pairs,
`sorted(..., key=lambda item: ...)` to choose the sort field, and `reverse` to set order.

```python
people = {
    "Bob": {"age": 15, "country": "Canada"},
    "Alice": {"age": 30, "country": "USA"},
    "Charlie": {"age": 25, "country": "UK"},
    "Diana": {"age": 26, "country": "Germany"},
    "Ethan": {"age": 30, "country": "Australia"}
}

# sort and keep as an ordered dict
sorted_people = dict(
    sorted(people.items(), key=lambda item: item[1]["age"])
)
```
