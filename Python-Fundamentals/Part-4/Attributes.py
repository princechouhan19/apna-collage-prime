#class and instance attributes

class Student:
    school = "ABC School" #class attribute
    pi = 3.14 #class attribute

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age #instance attribute
        pi = 3.14159 #local variable, not a class attribute

#creating instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

#accessing class attribute
print(student1.school) #Output: ABC School
print(student2.school) #Output: ABC School

#accessing instance attributes
print(student1.name) #Output: Alice
print(student1.age) #Output: 20
print(student2.name) #Output: Bob
print(student2.age) #Output: 22

#modifying class attribute
Student.school = "XYZ School"
print(student1.school) #Output: XYZ School

#modifying instance attribute
student1.name = "Charlie"
print(student1.name) #Output: Charlie

#modifying local variable does not affect class attribute
print(Student.pi) #Output: 3.14