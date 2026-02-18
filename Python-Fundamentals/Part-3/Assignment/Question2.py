# Question 2:  Given a list of integers compute the average of all numbers in the list.

list = [1, 2, 3, 4, 5]

sum = 0
for i in list:
    sum += i

print("Average of List = ", sum/len(list))