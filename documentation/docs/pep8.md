# PEP8 - Python Style Guide

## 📝 What is PEP8?

PEP8 is the **Python Enhancement Proposal 8**, which defines the official style guide for writing Python code. It provides a set of conventions and best practices to make Python code more readable, consistent, and maintainable across projects and teams.

---

## ❓ Why Use PEP8?

- **👀 Improves readability:** Code that follows a consistent style is easier to read and understand.
- **🤝 Enhances maintainability:** Uniform code style helps teams collaborate and maintain projects more efficiently.
- **🛡️ Reduces errors:** Clear formatting helps prevent bugs caused by confusing or unclear code structure.
- **⭐ Promotes best practices:** Following widely accepted standards ensures code quality and professional development habits.

## ⚙️ How to Use PEP8?

- Follow the naming conventions, indentation, spacing, and line length rules described in PEP8.
- Use tools like `flake8`, `pylint`, or `black` to automatically check and format your code.
- Review PEP8 guidelines regularly to improve code style.

You can read the official PEP8 document here:  
https://peps.python.org/pep-0008/

---

## 📚 Basic PEP8 Guidelines with Examples

### 1. 🔤 Variable Naming

- Use **lowercase** words separated by underscores (`snake_case`).
- Avoid single character names except for counters or iterators.

```python
user_name = "John"
total_amount = 100
counter = 0
```

### 2. ⚙️ Function Naming

- Use lowercase words separated by underscores (snake_case).
- Function names should be descriptive of their purpose.

```python
def calculate_total(price, tax_rate):
    total = price + price * tax_rate
    return total
```

### 3. 🏷️ Class Naming
- Use CapWords (also called PascalCase or CamelCase) convention.
- Class names should be nouns and describe the object.

```python
class UserProfile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### 4. ↪️ Indentation and Spacing
- Use 4 spaces per indentation level.
- Limit lines to a maximum of 79 characters.
- Surround top-level functions and classes with two blank lines.
- Use one blank line inside functions to separate logical sections.

```python
def greet_user(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Guest!")
```

---

## 📌 Summary

Following PEP8 is a standard way to write clean, readable, and professional Python code. It makes your code easier for others (and yourself) to read, understand, and maintain.