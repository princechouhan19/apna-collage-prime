# Python Fundamentals (Part 2)

**Concepts:** Conditional Statements, Loops & Functions

---

## Conditional Statements

Conditional statements let our program decide what to do based on conditions
(i.e. true or false expressions).

There are **3 main conditional statements in Python**:

1. `if` – used to test a condition. If it’s True, the indented block runs.
2. `else` – else block runs if all above conditions are false.
3. `elif` – (“else if”) used when we have multiple conditions to check.

---

### Example 1

```python
age = int(input("enter age: "))
if age >= 18: # if true/false, entire block of code is executed
    print("you can vote")
    print("you can drive")
else:
    print("you can't vote")
    print("you can't drive")
```

---

### Example 2 – Traffic Lights

```python
color = input("enter color: ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("wrong color")
```

**Note:**
We can have standalone & multiple `if` statements but `elif` & `else`
can’t be used without an `if` statement preceding them.

---

## Logical Operators in Conditions

Operators used:

* `and`
* `or`
* `not`

---

### Example 3 – Logical Operators

```python
age = int(input("enter age: "))
if age < 13:
    print("child")
elif (age >= 13 and age < 18):
    print("teenager")
else:
    print("adult")
```

---

### Login System (Nesting)

```python
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("log in successful!")
else:
    if username != "admin": # NESTING
        print("wrong user name, try again.")
    else:
        print("wrong password, try again.")
```

---

## Ternary Statements

Ternary statements (or conditional expressions) are a compact way to write
conditions in one line.

**Syntax:**

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 18
status = "Adult" if age >= 18 else "Not Adult"
print(status)
```

**Note:**
Everything written using ternary statements can be done using normal `if-else`.
Ternary statements are not recommended for nested or complex conditions.

---

## Match Case Statements (Python 3.10+)

Alternative to long `if-elif-else` chains.

### Syntax

```python
match variable:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
```

### Example – Traffic Lights

```python
color = input("enter color: ")
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case "green":
        print("Go")
    case _:
        print("wrong color")
```

---

## Loops

A loop lets us execute a block of code multiple times.

Python has **2 types of loops**:

1. `while` loop – repeats while a condition is True
2. `for` loop – iterates over a sequence

---

## While Loop

### Syntax

```python
while condition:
    # code block
```

### Example 1 – Print 1 to 5

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### Example 2 – Print 5 to 1

```python
i = 5
while i > 0:
    print(i)
    i -= 1
```

**Infinite Loop:**
If condition always evaluates to True, the loop never stops.

---

### Practice Problems (Set 1)

1. For a given number `n`, print if it’s a multiple of 5 or not.
2. For a given number `n`, print if it’s Odd or Even.

---

## Loop Control Statements

### `break`

Stops the loop immediately.

```python
i = 1
while i <= 10:
    if i % 6 == 0:
        break
    print(i)
    i += 1
```

**Output:** `1 2 3 4 5`

---

### `continue`

Skips current iteration.

```python
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
```

**Output:** `1 2 4 5 7 8 10`

---

### Infinite Loop Example (Do NOT run)

```python
while True:
    print("Prime")
```

---

## For Loop

Used to iterate over sequences.

### Syntax

```python
for variable in sequence:
    # code
```

### Example

```python
for i in range(5):
    print(i)
```

---

### Looping over a String

```python
word = "Prime"
for ch in word:
    print(ch)
```

---

### Check if Character Exists

```python
if 'i' in word:
    print("letter exists")
```

---

### Count Characters

```python
word = "artificial intelligence"
count = 0
for ch in word:
    if ch == 'i':
        count += 1
print(f"i occurs {count} times.")
```

---

### Nested Loop

```python
for i in range(1, 3):
    for j in range(1, 3):
        print(f"({i}, {j})")
```

---

## `range()` Function

Generates a sequence of numbers.

### Examples

```python
for i in range(5):
    print(i)
```

```python
for i in range(1, 6):
    print(i)
```

```python
for i in range(1, 10, 2):
    print(i)
```

---

### Practice Problems (Set 2)

1. Multiplication table (using `while`)
2. Odd numbers from 1 to 10 (using `continue`)
3. Count vowels
4. Sum of first natural numbers

---

## Functions

Functions are reusable blocks of code.

### Function Definition

```python
def hello():
    print("hello from Prime")
```

### Function Call

```python
hello()
```

---

### Function with Parameters

```python
def sum(a, b):
    print(a + b)

print(sum(5, 10))
```

---

### Return Statement

```python
def avg(a, b, c):
    return (a + b + c) / 3

print(avg(1, 2, 3))
```

---

### Default Parameters

```python
def sum(a, b=1):
    return a + b

print(sum(5))
```

---

## Lambda Functions

Short, one-line anonymous functions.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x
print(square(5))
```

---

## Built-in Functions Used

```python
print()
input()
type()
range()
```

---

## Practice Problems (Set 3)

1. Factorial of a number
2. Largest of 3 numbers

---

## Solutions

### Multiple of 5

```python
num = int(input("enter number: "))
if num % 5 == 0:
    print("multiple of 5")
else:
    print("NOT a multiple of 5")
```

---

### Odd or Even

```python
num = int(input("enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### Multiplication Table

```python
n = int(input("enter n: "))
i = 1
while i <= 10:
    print(i * n)
    i += 1
```

---

### Factorial of N

```python
n = int(input("enter n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial = ", fact)
```

---

### Largest of 3 Numbers

```python
def get_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(get_largest(3, 10, 5))
```

---