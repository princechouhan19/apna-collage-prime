# Question9 : - Given a list, print all elements that appear more than once in the list.
# Hint- [use sets]

list1 = [1, 2, 3, 4, 2, 3, 5, 6, 5]

seen = set()
duplicates = set()

for item in list1:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Elements that appear more than once:", list(duplicates))