# Question10 : Ask the user for a string and print:
# All unique characters
# The count of unique characters

string = input("Enter a string: ")

unique_chars = set(string)

print("Unique characters:", list(unique_chars))
print("Count of unique characters:", len(unique_chars))
