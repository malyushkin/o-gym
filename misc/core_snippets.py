# Safe string slicing
word = "hello"
print(word[999:])  # prints empty string ("")

assert word[999:] == ""  # True
