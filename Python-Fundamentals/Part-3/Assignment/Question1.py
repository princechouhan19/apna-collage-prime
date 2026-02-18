# Question 1:  Ask the user for a string and check whether it is a palindrome or not. 
# A palindrome is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.

str = input("Enter a string: ")

if str == str[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome") 