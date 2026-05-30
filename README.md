<div align="center">

# freecodecamp-python

A hands-on collection of Python projects built through the FreeCodeCamp curriculum. Each module progresses from fundamentals to advanced algorithms through practical exercises.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FreeCodeCamp](https://img.shields.io/badge/FreeCodeCamp-0A0A23?style=for-the-badge&logo=freecodecamp&logoColor=white)](https://freecodecamp.org)
[![License](https://img.shields.io/badge/License-MIT-22AA55?style=for-the-badge)](#license)
[![Progress](https://img.shields.io/badge/Progress-12.5%25-FF6F00?style=for-the-badge)](#progress-tracker)

</div>

---

## Table of Contents

| # | Module | Status |
|:-:|--------|--------|
| 01 | [Python Basics](#python-basics) | 2 / 7 projects |
| 02 | [Build a Budget App](#build-a-budget-app) | Pending |
| 03 | [Build a Hash Table](#build-a-hash-table) | Pending |
| 04 | [Build a Polygon Area Calculator](#build-a-polygon-area-calculator) | Pending |
| 05 | [Build a User Configuration Manager](#build-a-user-configuration-manager) | Pending |
| 06 | [Classes and Objects](#classes-and-objects) | Pending |
| 07 | [Dictionaries and Sets](#dictionaries-and-sets) | Pending |
| 08 | [Dynamic Programming](#dynamic-programming) | Pending |
| 09 | [Error Handling](#error-handling) | Pending |
| 10 | [Graphs and Trees](#graphs-and-trees) | Pending |
| 11 | [Implement the Tower of Hanoi Algorithm](#implement-the-tower-of-hanoi-algorithm) | Pending |
| 12 | [Linear Data Structures](#linear-data-structures) | Pending |
| 13 | [Loops and Sequences](#loops-and-sequences) | Pending |
| 14 | [Object-Oriented Programming (OOP)](#object-oriented-programming-oop) | Pending |
| 15 | [Python Review](#python-review) | Pending |
| 16 | [Algorithms](#algorithms) | Pending |

---

## Project Structure

```
freecodecamp-python/
|
+-- Python Basics/                              # 2 of 7 completed
|   +-- Build a Report Card Printer/            # 10 steps
|   +-- Build an Employee Profile Generator/    # 18 steps
|   +-- Build a Caesar Cipher/                  # Pending
|   +-- Build a Movie Ticket Booking Calculator/ # Pending
|   +-- Build a Travel Weather Planner/         # Pending
|   +-- Build an Apply Discount Function/       # Pending
|   +-- Build an RPG Character/                 # Pending
|
+-- Build a Budget App/                         # Pending
+-- Build a Hash Table/                         # Pending
+-- Build a Polygon Area Calculator/            # Pending
+-- Build a User Configuration Manager/         # Pending
+-- Classes and Objects/                        # Pending
+-- Dictionaries and Sets/                      # Pending
+-- Dynamic Programming/                        # Pending
+-- Error Handling/                             # Pending
+-- Graphs and Trees/                           # Pending
+-- Implement the Tower of Hanoi Algorithm/     # Pending
+-- Linear Data Structures/                     # Pending
+-- Loops and Sequences/                        # Pending
+-- Object-Oriented Programming (OOP)/          # Pending
+-- Python Review/                              # Pending
+-- Algorithms/                                 # Pending
|
+-- README.md
```

---

## Python Basics

**Topics:** Variables, Data Types, Type Conversion, String Operations, f-strings, String Slicing

<details open>
<summary><b>Project 1: Build a Report Card Printer</b> — 10 steps</summary>

A beginner-friendly introduction to Python's core data types. Each step builds on the last, from a simple variable to printing all four primitive types.

| Step | File | Concept | Code |
|:----:|------|---------|------|
| 01 | `step1.py` | String assignment | `name = 'Alice'` |
| 02 | `step2.py` | The `print()` function | `print(name)` |
| 03 | `step3.py` | The `type()` function | `print(type(name))` |
| 04 | `step4.py` | Boolean type | `is_student = True` |
| 05 | `step5.py` | Printing multiple items | `print(is_student, type(is_student))` |
| 06 | `step6.py` | Clean output formatting | Combine prints neatly |
| 07 | `step7.py` | Integer type | `age = 20` |
| 08 | `step8.py` | Float & `isinstance()` | `score = 80.5` |
| 09 | `step9.py` | Fixed type check | `isinstance(score, float)` |
| 10 | `step10.py` | Final solution | Complete type demonstration |

```python
# step10.py — Final Solution
name = 'Alice'
is_student = True
age = 20
score = 80.5

print(name, type(name))
print(is_student, type(is_student))
print(age, type(age))
print(isinstance(score, float))
print(score, type(score))
```

**Key Takeaways:**
- Python has 4 primitive data types: `str`, `bool`, `int`, `float`
- Use `type()` to inspect a variable's type at runtime
- Use `isinstance()` to check if a variable is a specific type
- `print()` accepts multiple arguments separated by commas

</details>

<details>
<summary><b>Project 2: Build an Employee Profile Generator</b> — 18 steps</summary>

A comprehensive deep-dive into string manipulation. Builds a full employee profile card while learning concatenation, type conversion, f-strings, and slicing.

| Step | File | Concept | Code |
|:----:|------|---------|------|
| 01 | `step1.py` | Multiple variables | `first_name`, `last_name` |
| 02 | `step2.py` | String concatenation | `full_name = first_name + last_name` |
| 03 | `step3.py` | Adding spaces | `first_name + ' ' + last_name` |
| 04 | `step4.py` | New string variable | `address = '123 Main Street'` |
| 05 | `step5.py` | `+=` operator | `address += ', Apartment 4B'` |
| 06 | `step6.py` | Cleanup | Remove debug prints |
| 07 | `step7.py` | Integer variable | `employee_age = 28` |
| 08 | `step8.py` | Building a string | `employee_info = full_name + ' is '` |
| 09 | `step9.py` | The TypeError trap | `str + int` — intentional error |
| 10 | `step10.py` | Type conversion | `str(employee_age)` |
| 11 | `step11.py` | Complete sentence | Print the employee info |
| 12 | `step12.py` | More string building | Experience info with `str()` |
| 13 | `step13.py` | Introduction to f-strings | `f'Employee: {full_name}'` |
| 14 | `step14.py` | Multiple f-string placeholders | `| Age: {employee_age}` |
| 15 | `step15.py` | Full employee card | Position, salary, f-string |
| 16 | `step16.py` | String slicing `[0:3]` | Department code from `employee_code` |
| 17 | `step17.py` | Multiple slices | Year `[4:8]`, initials `[9:11]` |
| 18 | `step18.py` | Negative slicing | `employee_code[-3:]` |

```python
# step18.py — Final Solution
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

address = '123 Main Street'
address += ', Apartment 4B'

employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Data Analyst'
salary = 75000

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

employee_code = 'DEV-2026-JD-001'
department_code = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
last_three = employee_code[-3:]

print(department_code)
print(year_code)
print(initials)
print(last_three)
```

| Concept | Example | Output |
|---------|---------|--------|
| Concatenation | `'Hello' + ' ' + 'World'` | `Hello World` |
| `str()` conversion | `str(28)` | `'28'` |
| f-strings | `f'Age: {age}'` | `Age: 28` |
| Positive slice | `'DEV-2026'[0:3]` | `DEV` |
| Negative slice | `'DEV-2026'[-3:]` | `026` |

**Key Takeaways:**
- Strings concatenate with `+`, but you can't mix `str + int` without conversion
- Use `str()` to convert numbers before concatenation
- f-strings (`f'...{var}...'`) are cleaner and more readable
- `str += 'more'` appends to an existing string
- String slicing: `string[start:stop]` extracts a substring
- Negative indices count from the end: `string[-3:]` gets the last 3 characters

</details>

<details>
<summary><b>Project 3: Build a Caesar Cipher</b> — Pending</summary>

Encryption and decryption with the classic Caesar cipher algorithm. Covers loops, string manipulation, and character encoding.

</details>

<details>
<summary><b>Project 4: Build a Movie Ticket Booking Calculator</b> — Pending</summary>

A practical calculator for movie ticket pricing. Covers conditionals, arithmetic, and user input.

</details>

<details>
<summary><b>Project 5: Build a Travel Weather Planner</b> — Pending</summary>

Weather-based travel recommendations. Covers conditionals, comparison operators, and decision trees.

</details>

<details>
<summary><b>Project 6: Build an Apply Discount Function</b> — Pending</summary>

Reusable discount calculation logic. Covers function definition, parameters, return values, and scope.

</details>

<details>
<summary><b>Project 7: Build an RPG Character</b> — Pending</summary>

A role-playing game character creator. Covers classes, attributes, methods, and object instantiation.

</details>

---

## Build a Budget App

**Topics:** Classes, Methods, String Formatting  
**Status:** Pending

<details>
<summary>Preview</summary>

A budget tracking application that teaches:
- Creating classes with `__init__`
- Implementing `deposit()`, `withdraw()`, and `transfer()` methods
- Formatting strings with `__repr__` or `__str__`
- Building a category-based expense tracker

</details>

---

## Build a Hash Table

**Topics:** Hashing, Dictionaries, Collision Resolution  
**Status:** Pending

<details>
<summary>Preview</summary>

Implement a hash table from scratch:
- Hash function implementation
- Handling collisions with chaining or open addressing
- `get()`, `set()`, and `delete()` operations

</details>

---

## Build a Polygon Area Calculator

**Topics:** OOP, Inheritance, Math  
**Status:** Pending

<details>
<summary>Preview</summary>

Calculate areas of polygons using OOP:
- Base `Rectangle` class with `width` and `height`
- Derived `Square` class
- Area and perimeter calculations
- String representation methods

</details>

---

## Build a User Configuration Manager

**Topics:** File I/O, JSON, Serialization  
**Status:** Pending

<details>
<summary>Preview</summary>

Manage user settings with persistence:
- Reading and writing JSON files
- User profile management
- Settings validation
- Default configurations

</details>

---

## Classes and Objects

**Topics:** OOP Fundamentals  
**Status:** Pending

<details>
<summary>Preview</summary>

The foundation of object-oriented programming in Python:
- Class definitions and instantiation
- Instance vs class variables
- Methods and `self`
- Magic methods (`__init__`, `__str__`, `__repr__`)

</details>

---

## Dictionaries and Sets

**Topics:** Hash Maps, Set Theory  
**Status:** Pending

<details>
<summary>Preview</summary>

Master Python's mapping and set types:
- Dictionary creation and manipulation
- Set operations (union, intersection, difference)
- When to use dicts vs lists vs sets
- Dictionary comprehensions

</details>

---

## Dynamic Programming

**Topics:** Memoization, Tabulation, Optimization  
**Status:** Pending

<details>
<summary>Preview</summary>

Optimize recursive solutions with DP:
- Fibonacci with memoization
- Knapsack problem
- Longest common subsequence
- Top-down vs bottom-up approaches

</details>

---

## Error Handling

**Topics:** Exceptions, Try/Except, Debugging  
**Status:** Pending

<details>
<summary>Preview</summary>

Write robust, error-resilient code:
- `try`/`except`/`else`/`finally` blocks
- Custom exception classes
- Common built-in exceptions
- Best practices for error handling

</details>

---

## Graphs and Trees

**Topics:** Graph Theory, Tree Traversals  
**Status:** Pending

<details>
<summary>Preview</summary>

Explore non-linear data structures:
- Graph representations (adjacency list/matrix)
- BFS and DFS traversals
- Binary trees and BSTs
- Tree traversals (inorder, preorder, postorder)

</details>

---

## Implement the Tower of Hanoi Algorithm

**Topics:** Recursion, Divide and Conquer  
**Status:** Pending

<details>
<summary>Preview</summary>

Solve the classic Tower of Hanoi puzzle:
- Recursive algorithm design
- Base case and recursive case
- Visualizing the call stack
- Time complexity analysis

</details>

---

## Linear Data Structures

**Topics:** Linked Lists, Stacks, Queues  
**Status:** Pending

<details>
<summary>Preview</summary>

Build the fundamental linear data structures:
- Singly and doubly linked lists
- Stack (LIFO) implementation
- Queue (FIFO) implementation
- Big-O analysis of operations

</details>

---

## Loops and Sequences

**Topics:** Iteration, Comprehensions, Generators  
**Status:** Pending

<details>
<summary>Preview</summary>

Master iteration in Python:
- `for` and `while` loops
- List comprehensions
- Generator expressions
- `enumerate()`, `zip()`, and `map()`

</details>

---

## Object-Oriented Programming (OOP)

**Topics:** Advanced OOP, Inheritance, Polymorphism  
**Status:** Pending

<details>
<summary>Preview</summary>

Deep dive into Python's OOP capabilities:
- Inheritance and method resolution order (MRO)
- Polymorphism and duck typing
- Abstract base classes
- Composition vs inheritance

</details>

---

## Python Review

**Topics:** Comprehensive Python Review  
**Status:** Pending

<details>
<summary>Preview</summary>

A cumulative review of all Python concepts covered:
- Mixed exercises combining multiple topics
- Mini-projects for portfolio
- Common interview questions
- Best practices and style guides

</details>

---

## Algorithms

**Topics:** Sorting, Searching, Algorithm Design  
**Status:** Pending

<details>
<summary>Preview</summary>

Classic algorithms implemented in Python:
- Sorting: Bubble, Merge, Quick, Heap
- Searching: Binary Search, BFS, DFS
- Algorithm complexity (Big-O notation)
- Problem-solving strategies

</details>

---

## Progress Tracker

| Module | Progress |
|--------|----------|
| Python Basics | `████████████████░░░░░░` 80% (2 of 7 sub-projects) |
| Build a Budget App | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Build a Hash Table | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Polygon Area Calculator | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| User Config Manager | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Classes and Objects | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Dictionaries and Sets | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Dynamic Programming | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Error Handling | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Graphs and Trees | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Tower of Hanoi | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Linear Data Structures | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Loops and Sequences | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| OOP | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Python Review | `░░░░░░░░░░░░░░░░░░░░░░` 0% |
| Algorithms | `░░░░░░░░░░░░░░░░░░░░░░` 0% |

<div align="center">

### Overall Progress

`████░░░░░░░░░░░░░░░░` 12.5% (2 of 16 modules)

---

## Prerequisites

- Python 3.x installed on your system
- Basic familiarity with the command line
- A text editor or IDE (VS Code, PyCharm, etc.)

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/freecodecamp-python.git

# Navigate to a project
cd "Python Basics/Build a Report Card Printer"

# Run a specific step
python step10.py
```

---

## Contributing

Contributions are welcome. If you have a better solution or an alternative approach:

1. Fork the repository
2. Create a new branch (`git checkout -b my-solution`)
3. Commit your changes (`git commit -m 'Add solution to X'`)
4. Push to the branch (`git push origin my-solution`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built for the FreeCodeCamp community
</p>

</div>
