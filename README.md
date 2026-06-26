# Python Training

This repository contains beginner-friendly Python training material and practice programs based on real-life problem statements. The examples and notes are designed to help learners understand Python basics, variables, data types, arithmetic operators, user input, basic output formatting, and conditional statements.

---

## What is Python?

Python is a **high-level, interpreted, general-purpose programming language** created by **Guido van Rossum** and first released in **1991**. It emphasises code readability and simplicity, making it one of the best languages for beginners.

### Key Features of Python

| Feature | Description |
| --- | --- |
| **Easy to Learn** | Simple, English-like syntax that is beginner-friendly |
| **Interpreted** | Code is executed line by line — no separate compilation step needed |
| **Dynamically Typed** | Variable types are determined at runtime; no need to declare types |
| **Platform Independent** | Runs on Windows, macOS, Linux, etc. without modification |
| **Open Source** | Free to download, use, and distribute |
| **Extensive Libraries** | Rich standard library and thousands of third-party packages |
| **Object-Oriented** | Supports classes, objects, inheritance, and polymorphism |
| **Community Support** | Large, active community with abundant learning resources |

---

## Core Python Concepts

### 1. Variables and Data Types

A **variable** is a named container that stores data in memory.

```python
name = "Kartik"       # str   — text
age = 20              # int   — whole number
marks = 85.5          # float — decimal number
passed = True         # bool  — True / False
```

Python is **dynamically typed**, so the same variable can hold different types at different times.

Common data types:

| Type | Example | Description |
| --- | --- | --- |
| `int` | `10`, `-3` | Whole numbers |
| `float` | `3.14`, `-0.5` | Decimal numbers |
| `str` | `"hello"` | Text / string |
| `bool` | `True`, `False` | Boolean values |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `dict` | `{"a": 1}` | Key-value pairs |

### 2. Keywords, Literals, and Identifiers

- **Keywords** — Reserved words with special meaning (e.g., `if`, `else`, `while`, `for`, `def`, `class`, `return`, `True`, `False`, `None`).
- **Literals** — Fixed values written directly in code (e.g., `42`, `3.14`, `"hello"`, `True`).
- **Identifiers** — Names given by the programmer to variables, functions, classes, etc. Rules:
  - Must start with a letter or underscore (`_`).
  - Cannot start with a digit.
  - Cannot be a keyword.
  - Case-sensitive (`age` ≠ `Age`).

### 3. Operators

| Category | Operators | Example |
| --- | --- | --- |
| **Arithmetic** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `5 + 3` → `8` |
| **Comparison** | `==`, `!=`, `>`, `<`, `>=`, `<=` | `5 > 3` → `True` |
| **Logical** | `and`, `or`, `not` | `True and False` → `False` |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=` | `x += 1` |

### 4. Input and Output

```python
# Taking input (always returns a string)
name = input("Enter your name: ")

# Converting input to a number
age = int(input("Enter your age: "))

# Printing output
print("Hello,", name)
print(f"You are {age} years old.")   # f-string formatting
```

### 5. Conditional Statements (Selection Statements)

Conditional statements let the program make **decisions** based on conditions.

#### `if` Statement

```python
age = 20
if age >= 18:
    print("You are an adult.")
```

#### `if ... else` Statement

```python
age = 15
if age >= 18:
    print("Eligible for voting.")
else:
    print("Not eligible for voting.")
```

#### `if ... elif ... else` (Ladder)

```python
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
```

#### Nested `if ... else`

```python
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Bring your ID.")
else:
    print("Entry denied.")
```

### 6. Type Conversion

```python
x = int("10")       # str → int
y = float("3.14")   # str → float
z = str(100)         # int → str
```

---

## Topics Covered

- Addition using `+`
- Subtraction using `-`
- Multiplication using `*`
- Division using `/`
- Floor division using `//`
- Modulus using `%`
- Exponentiation using `**`
- Taking input with `input()`
- Converting values using `int()` and `float()`
- Printing results with `print()`
- Features of Python
- Keywords, literals, and identifiers
- Variables and data types
- Conditional checking using `if`
- Decision making using `if ... else`
- Nested `if ... else` statements

## Folder Structure

```text
classwork/
  day-1 basics and operators_24th_June/
    features of Python.png
    keywords, Literals, Identifiers.png
    operators in python.png
    problems based on arithmetic operators.pdf
    variables and datatypes.png
  day-2 selection statement_25th_june/
  day-3 selection statement_26th_june/
labwork/
self-learning/
```

## Classwork Material

### Day 1: Basics and Operators

| No. | File | Topic |
| --- | --- | --- |
| 1 | `classwork/day-1 basics and operators_24th_June/features of Python.png` | Features of Python |
| 2 | `classwork/day-1 basics and operators_24th_June/keywords, Literals, Identifiers.png` | Keywords, literals, and identifiers |
| 3 | `classwork/day-1 basics and operators_24th_June/operators in python.png` | Operators in Python |
| 4 | `classwork/day-1 basics and operators_24th_June/problems based on arithmetic operators.pdf` | Arithmetic operator problem statements |
| 5 | `classwork/day-1 basics and operators_24th_June/variables and datatypes.png` | Variables and data types |

### Day 3: Selection Statement

| No. | File | Problem |
| --- | --- | --- |
| 1 | `classwork/day-3 selection statement_26th_june/01_atm_minimum_balance_check.py` | Check whether account balance is below the minimum required balance |
| 2 | `classwork/day-3 selection statement_26th_june/02_movie_ticket_eligibility.py` | Check whether a customer is eligible to watch a movie |
| 3 | `classwork/day-3 selection statement_26th_june/03_student_grade_calculator.py` | Display student grade based on marks using nested `if ... else` |
| 4 | `classwork/day-3 selection statement_26th_june/04_electricity_bill_discount.py` | Apply discount if the electricity bill amount is Rs. 5,000 or more |
| 5 | `classwork/day-3 selection statement_26th_june/05_parking_fee_waiver.py` | Waive or apply parking fee based on purchase amount |
| 6 | `classwork/day-3 selection statement_26th_june/06_loan_eligibility_check.py` | Check whether an applicant is eligible for a personal loan |
| 7 | `classwork/day-3 selection statement_26th_june/07_voting_eligiblity.py` | Check whether a person is eligible for voting based on age |
| 8 | `classwork/day-3 selection statement_26th_june/08_To_verify_if_a_number_is_natural_number_or_not.py` | Verify if a given number is a natural number or not |

Each Python file includes the question as comments at the top, followed by the solution code.

## How to Run

Make sure Python is installed, then open a terminal in this folder.

Run any program using:

```bash
python "folder_name/file_name.py"
```

Example:

```bash
python "classwork/day-3 selection statement_26th_june/02_movie_ticket_eligibility.py"
```

Then enter the requested input values and check the output.

To open Day 1 notes or problem statements, open the image or PDF files from:

```text
classwork/day-1 basics and operators_24th_June/
```

## Example

```text
Enter Your Age: 20
You are eligible to watch the movie.
```

## Goal

The goal of this training project is to build confidence with Python basics before moving to conditions, loops, functions, lists, and larger projects.
Day 1 focuses on Python fundamentals and operators. Day 3 focuses on writing decision-making logic using `if ... else` statements.
