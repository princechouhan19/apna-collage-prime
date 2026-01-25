print("    Google    ")
User = input("Enter your UserName👤 : ")
Pass = input("Enter your Password🔑 : ")

if(User=="admin" and Pass=="admin123"):
    print("Log In Sucessfully ✅")
elif(User=="admin"):
    print("Wrong Password🔑")
elif(Pass=="admin123"):
    print("Wrong UserName👤")
else:
    print("Wrong Credentials , Access Denied⛔")