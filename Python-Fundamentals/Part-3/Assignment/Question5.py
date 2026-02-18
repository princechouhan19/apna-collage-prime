# Question5 : Create a dictionary :  
# Keys = student names
# Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
# depending on the operation they want to perform on the dictionary:
# 1. - Add a student
# 2. - Update marks
# 3. - Search for a student
# 4. - Display all students and marks  

d = {}

while True:
    print("\nMenu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")
    
    choice = input("Enter your choice: ").upper()
    
    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        d[name] = marks
        print("Student added successfully.")
    
    elif choice == 'B':
        name = input("Enter student name: ")
        if name in d:
            marks = int(input("Enter new marks: "))
            d[name] = marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")
    
    elif choice == 'C':
        name = input("Enter student name: ")
        if name in d:
            print("Marks: ", d[name])
        else:
            print("Student not found.")
    
    elif choice == 'D':
        print("Students and marks:")
        for name, marks in d.items():
            print(name, ":", marks)
    
    elif choice == 'E':
        break
    
    else:
        print("Invalid choice. Please try again.")