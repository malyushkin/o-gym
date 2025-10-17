# Checking small `int` interning in Python
# ------------------------------------------------------------
# Python "interns" (caches) integers from -5 to 256.
# This means that when the same values are created in this range,
# both variables will point to the same object in memory (a is b → True).

num_from = -30
num_to = 300

true_list = []  # numbers where a is b == True (interned)
false_list = []  # numbers where a is b == False (not interned)

for i in range(num_from, num_to + 1):
    # Using "+ 1" to avoid both variables pointing to the same existing object.
    # This creates a new value, but small ints are still interned by Python.
    a = i + 1
    b = i + 1

    # Check whether a and b reference the same object
    if a is b:
        true_list.append(a)
    else:
        false_list.append(a)

# Print results
print("Interned (a is b):", "\t", true_list[:5], "\t", true_list[-5:])  # expected: around -5 to 256
print("Not interned:", "\t", false_list[:5], "\t", false_list[-5:])  # numbers outside the interned range
