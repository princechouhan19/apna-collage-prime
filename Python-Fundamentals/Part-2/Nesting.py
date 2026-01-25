print("        ZOHO")
User = input("Enter your UserName👤 : ")
Pass = input("Enter your Password🔑 : ")

if(User=="admin" and Pass=="admin123"):
    print("Log In Sucessfully ✅")
else:
    if(User!="admin"):
        print("Wrong UserName👤")
    else:
        print("Wrong Password🔑")
