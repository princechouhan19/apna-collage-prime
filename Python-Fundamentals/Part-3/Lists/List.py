# Mutable Sequence Of Values
# Indexing   0  1  2  3
#           [53,54,36,84]
# -ve index  -4 -3 -2 -1

marks = [99,36,85,82,89,23]
print(marks[4])
print(len(marks))

#Slicing in List
#word[Starting Index : Ending Index : Step ]
# BY DEFAULT : Starting Index = 0 and Ending Index = String Length

print(marks[0:5])
print(marks[:5])
print(marks[::2])
print(marks[-5:-2:2])