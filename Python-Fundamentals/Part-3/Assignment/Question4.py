# Question 4: Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even = ()
odd = ()

for i in tuple:
    if i % 2 == 0:
        even += (i,)
    else:
        odd += (i,)

print("Even numbers = ", even)
print("Odd numbers = ", odd)