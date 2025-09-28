## Core Snippets

Quick Python techniques and approaches worth to remember.

- [core_snippets.py](core_snippets.py)

### Safe string slicing

Slice a string from a given index to the end.
If the index is beyond the string length, Python returns an empty string instead of raising an error.

```python
word = "hello"
print(word[999:])  # prints ""
```

## Dicts

Patterns for working with Python dict objects.

- [dict.py](dict.py)

### Sorting a dictionary by a custom value

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

## Libs

Useful standard-library functions and helpers.

### `math` lib

Use math.gcd(a, b) to get the greatest common divisor of two integers.
Helpful for problems with string repetition, ratios, or reducing fractions.

```python
from math import gcd

v1, v2 = 14, 7

print(gcd(v1, v2))  # 7

```