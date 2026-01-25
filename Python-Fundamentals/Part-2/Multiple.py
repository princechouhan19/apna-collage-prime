n = int(input("Enter a Number : "))

if(n%2==0):
    print(n , "is a multiple of 2")
elif(n%3==0):
    print(n , "is a multiple of 3")
elif(n%5==0):
    print(n , "is a multiple of 5")
else:
    print("It could be an Prime No or Negative")