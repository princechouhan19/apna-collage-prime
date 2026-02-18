# Python Fundamentals (Part 3)

**Concepts:** Data Structures (Strings, Lists, Tuples, Dictionaries, Sets) & Formatting

---

## 1. Strings
Strings are **immutable** sequences of characters.

### Key Concepts
*   **Slicing**: Accessing parts of a string using indices `[start:stop:step]`.
*   **Methods**:
    *   `upper()`, `lower()`: Case conversion.
    *   `strip()`: Removing whitespace.
    *   `replace()`: Replacing substrings.
    *   `find()`, `count()`: Searching and counting.

---

## 2. Lists
Lists are **mutable**, ordered sequences used to store multiple items in a single variable.

### Key Concepts
*   **Looping**: Iterating over elements using `for` loops.
*   **Methods**:
    *   `append()`, `insert()`: Adding elements.
    *   `remove()`, `pop()`: Removing elements.
    *   `sort()`, `reverse()`: Ordering elements.
    *   `copy()`: Creating duplicates.

---

## 3. Tuples
Tuples are **immutable**, ordered sequences. Once created, they cannot be changed.

### Key Concepts
*   **Usage**: Storing data that shouldn't change (e.g., coordinates).
*   **Methods**:
    *   `count()`: Returns the number of times a value occurs.
    *   `index()`: Searches for a value and returns its position.

---

## 4. Dictionaries
Dictionaries store data values in **key:value pairs**. They are ordered (Python 3.7+), mutable, and do not allow duplicates.

### Key Concepts
*   **Accessing Items**: Using keys to retrieve values.
*   **Methods**:
    *   `keys()`, `values()`, `items()`: View keys, values, or pairs.
    *   `get()`: Safe way to access values.
    *   `update()`: Insert or modify items.
    *   `pop()`: Remove items.

---

## 5. Sets
Sets are **unordered**, **unchangeable** (items cannot be changed, but can be added/removed), and unindexed. No duplicate members allowed.

### Key Concepts
*   **Operations**:
    *   `add()`, `remove()`: Modifying the set.
    *   `union()`: Combining sets.
    *   `intersection()`: Finding common elements.
    *   `difference()`: Finding unique elements.

---

## 6. String Formatting
Techniques to format strings dynamically.

*   **f-strings**: `f"Hello {name}"` (Recommended)
*   `format()` method.

---

## Example Projects
*   **StudentEnroll.py**: Demonstrates using these data structures to manage student data.