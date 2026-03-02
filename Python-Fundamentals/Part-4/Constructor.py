#__init_Method
#def __init__(self):
#    print("This is a constructor")

class Student:
    #name = "Python"
    def __init__(self,name,cgpa):
        print("Constructor is called...")
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Prince",8.5)
stu2 = Student("Rohit",7.5)
stu3 = Student("Suresh",8.0)

print("----------------------------------------")
print(stu1.name + " has CGPA " + str(stu1.cgpa))
print(stu2.name + " has CGPA " + str(stu2.cgpa))
print(stu3.name + " has CGPA " + str(stu3.cgpa))
print("----------------------------------------")

print(f"{stu1.name} has {stu1.get_cgpa()} CGPA")