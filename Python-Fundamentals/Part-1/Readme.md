# Python Fundamentals

This Module contains well-structured notes on core Python concepts, suitable for
learning, revision, exams, and interviews.

---

## Contents
1. Operators
2. Keywords
3. Operator Precedence
4. Type Conversion & Type Casting

---

# 1. Operators

Operators are symbols used to perform operations on values or variables.

## 1.1 Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `//` Floor Division
- `%` Modulus
- `**` Exponentiation

---

## 1.2 Relational (Comparison) Operators
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

---

## 1.3 Assignment Operators
- `=`
- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
- `//=`
- `**=`

---

## 1.4 Logical Operators
- `and`
- `or`
- `not`

---

# 2. Keywords

Python keywords are **reserved words** that have special meaning in the language.  
They **cannot be used** as identifiers.

> Python Version: **3.10+**

---

## Boolean & Null
- `True`
- `False`
- `None`

---

## Control Flow
- `if`
- `elif`
- `else`
- `match`
- `case`

---

## Loops
- `for`
- `while`
- `break`
- `continue`
- `pass`

---

## Functions
- `def`
- `return`
- `yield`
- `lambda`

---

## Exception Handling
- `try`
- `except`
- `finally`
- `raise`
- `assert`

---

## Import & Scope
- `import`
- `from`
- `as`
- `global`
- `nonlocal`

---

## Async Programming
- `async`
- `await`

---

## OOP & Others
- `class`
- `del`
- `in`
- `is`
- `with`
- `not`
- `and`
- `or`

---

Total Keywords: **35**

```python
import keyword
print(keyword.kwlist)
```

---

# 3. Operator Precedence

Operator precedence determines the **order in which operators are evaluated** in an expression.  
Operators with **higher precedence** are evaluated before operators with **lower precedence**.

If operators have the same precedence, **associativity** decides the evaluation order.

---

## Operator Precedence Diagram

![Python Operator Precedence](https://miro.medium.com/v2/resize:fit:1122/1*7F11ueHaVNzYH7h_ugUzjA.jpeg)

---

## Operator Precedence Table (High → Low)

| Precedence | Operators | Description |
|-----------|----------|-------------|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 | `or` | Logical OR |
| 14 | `if ... else` | Conditional expression |
| 15 | `lambda` | Lambda expression |

---

## Associativity Rules

| Operator | Associativity |
|--------|--------------|
| `**` | Right to Left |
| `=` | Right to Left |
| Most others | Left to Right |

---

## Examples

### Example 1
```python
result = 10 + 3 * 2
# Output: 16 (multiplication evaluated first)
```

### Example 2
```python
result = (10 + 3) * 2
# Output: 26 (parentheses override precedence)
```

### Example 3
```python
result = not True and False
# Output: False
# Explanation: 'not' evaluated before 'and'
```

### Example 4
```python
result = 2 ** 3 ** 2
# Output: 512
# Explanation: Exponentiation is right-associative
```

### Key Notes
- Always use parentheses for clarity in complex expressions
- Do not rely solely on precedence for readability
- Operator precedence is critical for debugging logical errors

### Best Practice
```python
# Bad (hard to read)
result = a + b * c ** d and e

# Good (clear and safe)
result = (a + (b * (c ** d))) and e
```

---

# 4. Type Conversion & Type Casting

Python supports two ways of converting data types:
1. **Type Conversion (Implicit / Automatic)**
2. **Type Casting (Explicit / Developer-controlled)**

Understanding the difference is essential for writing correct and predictable programs.

## 4.1 Type Conversion (Implicit / Automatic)

### Definition
Type conversion is performed **automatically by Python** when there is **no risk of data loss**.  
The developer does **not** explicitly write conversion code.

### Characteristics
- Done automatically by Python
- Occurs during expression evaluation
- Safe (no loss of information)
- Happens mostly with numeric types

### Common Implicit Conversions
| From | To |
|----|----|
| `int` | `float` |
| `int` | `complex` |
| `float` | `complex` |

### Examples

#### Example 1: Integer to Float
```python
a = 10        # int
b = 2.5       # float

result = a + b
print(result)        # 12.5
print(type(result)) # <class 'float'>
# Explanation: Python automatically converts int -> float before addition.
```

#### Example 2: Integer to Complex
```python
x = 5
y = 3 + 2j

z = x + y
print(z)
print(type(z))
# Output:
# (8+2j)
# <class 'complex'>
```

---

## 4.2 Type Casting (Explicit / Developer-Controlled)

### Definition
Type casting is performed explicitly by the developer using built-in conversion functions.

### Characteristics
- Manual conversion
- Developer has full control
- May cause data loss
- Required when converting incompatible types

### Common Type Casting Functions
| Function | Converts To |
|----------|-------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `complex()` | Complex |
| `bool()` | Boolean |
| `list()` | List |
| `tuple()` | Tuple |
| `set()` | Set |

### Examples

#### Example 1: Integer to Float
```python
a = 10
b = float(a)

print(b)
print(type(b))
```

#### Example 2: Float to Integer (Data Loss)
```python
x = 10.9
y = int(x)

print(y)  # 10
```

#### Example 3: String to Integer
```python
num = "100"
value = int(num)

print(value + 20)  # 120
```

#### Example 4: Explicit Conversion Required
```python
a = "10"
b = 5

# result = a + b  # TypeError
result = int(a) + b  # Correct

print(result)
```

---

## 4.3 Implicit vs Explicit Conversion

| Feature | Type Conversion (Implicit) | Type Casting (Explicit) |
|---------|----------------------------|-------------------------|
| Who performs it | Python | Developer |
| Control | Automatic | Manual |
| Risk of data loss | No | Possible |
| Functions used | No | Yes |
| Example | `int` -> `float` | `int("10")` |

### Key Notes
- Python never performs implicit conversion between unrelated types
- Use explicit casting when working with:
    - User input
    - Files
    - Databases
- Always validate data before casting

### Best Practice
```python
# Always be explicit when clarity matters
total = int(price) + int(tax)
```
