# Concepts: Object-Oriented Programming in Python

## Object-Oriented Programming

Suppose we need to build software to store all information related to students studying in a college.

These students can have many properties, such as:
- Name
- Parent's name
- Address
- Graduation year
- CGPA

They can also have behaviors, such as:
- Fee payment
- Scholarship calculation
- Checking attendance criteria

Without custom Python types, we could store this in lists or dictionaries, but that becomes inefficient as complexity grows.

- With many properties, we would need too many lists.
- With dictionaries, we'd repeat keys again and again.
- Behaviors are not naturally grouped with data.

To solve this, we use **Object-Oriented Programming (OOP)** with **classes** and **objects**.

## What is OOP?

Object-Oriented Programming (OOP) in Python is a paradigm centered around organizing code into objects:
- **Data** (attributes)
- **Behavior** (methods)

It helps create programs that are:
- Modular
- Reusable
- Easier to maintain

> Note: OOP is not mandatory for every problem, but it is very useful in many real-world scenarios.

OOP models software as interacting objects, similar to real-world entities (user, car, bank account, game enemy, etc.).

In Python, OOP is based on **classes**, which are blueprints for creating objects.

## Classes and Objects

### Class

A class is a blueprint/template for creating objects.

```python
class Car:
    brand = "Toyota"
```

### Object

An object (instance) is a real entity created from a class.

```python
car1 = Car()
car2 = Car()

print(car1.brand)
print(car2.brand)
# Toyota
# Toyota
```

Use the `.` (dot operator) to access object properties and methods.

### Class vs Object

| Class | Object |
|---|---|
| Blueprint/template | Concrete instance |
| Does not hold per-instance data | Holds actual data |
| One class can create many objects | Each object is independent |

## Attributes and Methods

- **Attributes** are variables inside a class/object.
- **Methods** are functions inside a class.

## Constructor in OOP

In Python, a constructor initializes a newly created object.

The constructor method is `__init__(self, ...)`. Python calls it automatically on object creation.

```python
class Student:
    def __init__(self):
        print("constructor was called")

stu1 = Student()
# constructor was called
```

`self` refers to the current object instance and is passed automatically.

Constructor with values:

```python
class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student("Rahul")
stu2 = Student("Harshita")
print(stu1.name, stu2.name)  # Rahul Harshita
```

### Types of Constructors

1. **Default constructor**: no extra parameters except `self`.
2. **Parameterized constructor**: takes parameters for custom object data.

> Note: Python does not support constructor overloading like Java/C++ in the same way. If multiple `__init__` methods are defined, the last one wins.

## Attributes in OOP

Attributes store object/class state.

### 1. Class Attributes

- Belong to the class
- Shared by all objects
- Defined directly in class body

```python
class Student:
    college = "ABC College"  # class attribute

stu1 = Student()
print(stu1.college)
print(Student.college)
```

### 2. Instance Attributes

- Belong to each object individually
- Defined inside `__init__` using `self`
- Each object has its own copy

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

stu1 = Student("Rahul", 8.7)
print(stu1.name, stu1.gpa)
```

## Methods in OOP

Methods define object behavior.

### 1. Instance Methods

- First parameter is `self`
- Can access instance and class attributes

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
```

### 2. Class Methods

- Use `@classmethod`
- First parameter is `cls`
- Work with class-level data

```python
class Student:
    school_name = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
```

### 3. Static Methods

- Use `@staticmethod`
- Do not take `self` or `cls`
- Utility functions grouped under class namespace

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

## Four Pillars of OOP

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

## Encapsulation

Encapsulation bundles data and methods in one unit (class) and controls access.

Python access levels:

### 1. Public members

Accessible everywhere.

```python
class Student:
    def __init__(self, name):
        self.name = name  # public

s = Student("Rahul")
print(s.name)
```

### 2. Protected members

Single underscore prefix (`_var`) indicates internal use by convention.

```python
class Person:
    def __init__(self):
        self._age = 20  # protected by convention

p = Person()
print(p._age)  # technically allowed
```

### 3. Private members

Double underscore prefix (`__var`) triggers name mangling.

```python
class Bank:
    def __init__(self, balance):
        self.__balance = balance

b = Bank(5000)
# print(b.__balance)  # AttributeError
print(b._Bank__balance)  # name-mangled access
```

> Python uses conventions and name mangling, not strict access enforcement like Java/C++.

### Getters and Setters

Use methods to read/update private data.

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary


e = Employee(50000)
print(e.get_salary())
e.set_salary(60000)
```

## Inheritance

Inheritance allows a child class to reuse properties and methods of a parent class.

- Parent/Base/Superclass: class being inherited from
- Child/Derived/Subclass: class that inherits

```python
class Employee:
    start_time = "9AM"
    end_time = "5PM"


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


t1 = Teacher("Data Science")
print(t1.subject, t1.start_time, t1.end_time)
```

Benefits:
- Code reuse
- Extensibility
- Cleaner design
- Supports polymorphism

### Types of Inheritance

#### 1. Single Inheritance

```python
class Parent:
    def display(self):
        print("Parent class")


class Child(Parent):
    pass


c = Child()
c.display()  # Parent class
```

#### 2. Multi-level Inheritance

```python
class Employee:
    start_time = "9AM"
    end_time = "5PM"


class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary


acc1 = Accountant(50_000, "CA")
print(acc1.salary, acc1.role, acc1.start_time, acc1.end_time)
```

#### 3. Multiple Inheritance

```python
class Teacher:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(Teacher, Student):
    def __init__(self, name, salary, gpa):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name


ta = TA("Rahul", 50_000, 7.5)
print(ta.name, ta.salary, ta.gpa)
```

`super()` is used to call parent class methods from child class.

## Abstraction

Abstraction hides implementation details and exposes only essential behavior.

Example: While driving, you use brakes without knowing hydraulic internals.

In Python, abstraction is commonly implemented using abstract classes and methods.

### Abstract Class

- Cannot be instantiated directly
- Can contain abstract and normal methods
- Serves as a blueprint

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```

### Abstract Method

Declared but not implemented in base class; child classes must override.

```python
@abstractmethod
def method_name(self):
    pass
```

### Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("Roar!")


class Cow(Animal):
    def make_sound(self):
        print("Moo!")


lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()
```

## Polymorphism

Polymorphism means one interface can have many forms.

- Same method name, different behavior for different objects
- Same operator, different behavior depending on data type

```python
print(1 + 2)      # addition
print("1" + "2")  # concatenation
```

This is operator overloading.

### 1. Method Overriding

Child class redefines a parent class method with the same name.

```python
class Animal:
    def sound(self):
        print("Some generic sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


a = Animal()
dog = Dog()

a.sound()    # Some generic sound
dog.sound()  # Bark
```

### 2. Duck Typing

"If it looks like a duck and quacks like a duck, it is a duck."

```python
class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


class Robot:
    def speak(self):
        print("Beep Boop")


def make_it_speak(entity):
    entity.speak()


d = Dog()
c = Cat()
r = Robot()

for e in [d, c, r]:
    make_it_speak(e)
```