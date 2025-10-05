# Greatest common divisor
def my_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

assert my_gcd(21, 7) == 7
assert my_gcd(7, 21) == 7
assert my_gcd(12, 6) == 4 ## AssertionError