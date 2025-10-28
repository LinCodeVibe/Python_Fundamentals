# 6 – Python Functions 

## Overview
To focus on **Python functions**, **code indentation**, and how to use **while loops** to control repetitive actions efficiently.  

---

##  Key Concepts Learned

###  - **Functions in Python**
A function is a reusable block of code that performs a specific task. It helps organize programs and reduce repetition.

**Syntax:**
```python
def my_function():
    # Do something
    print("Hello")
    print("World")

# Calling the function
my_function()
```
**Concepts learned:**
- Define a function using `def`.
- Call a function by its name followed by `()`.
- Keep indentation consistent for function bodies.

---

### **Defining and Calling Functions**
Functions allow us to encapsulate logic that can be executed later.  
Example:

```python
def greet_user():
    name = input("What is your name? ")
    print("Hello, " + name)

print("Welcome!")
greet_user()
```
**Output Example:**
```
Welcome!
What is your name? Python
Hello, Python
```

---

### **Code Indentation**
Indentation defines which lines of code belong together. Without proper indentation, Python raises an **IndentationError**.

**Example (Correct):**
```python
def my_function():
    print("Hello")
my_function()
```

**Example (Error):**
```python
def my_function():
print("Hello")  # IndentationError
```

Learned to structure blocks of code clearly inside functions, loops, and conditionals.

---

### **For vs While Loops**
Loops repeat actions multiple times, but differ in purpose:

| Type | Usage | Example |
|------|--------|----------|
| **For Loop** | Iterates over a known sequence | `for item in list_of_items:` |
| **While Loop** | Runs *while* a condition is true | `while something_is_true:` |

**Examples:**
```python
# For loop
for number in range(1, 5):
    print(number)

# While loop
count = 1
while count <= 5:
    print(count)
    count += 1
```

---


## Code Highlights

### Example 1: Indentation Error Check
```python
def my_function():
print("Hello")  # Missing indentation
```
Fix: Indent properly inside the function.

---

### Example 2: Function Execution Order
```python
def my_function():
    print("This will run")
my_function()
```
The code correctly defines and executes a function.

---

### Example 3: Nested Conditions Inside Functions
```python
def my_function():
    a = 3
    if a > 2:
        print("This will run")
my_function()
```
Demonstrates indentation inside nested structures.

---

## Summary

| Concept | Description |
|----------|--------------|
| **Function Definition** | Reusable block of organized code |
| **Function Call** | Executes the function’s statements |
| **Indentation** | Defines structure and scope of code |
| **While Loop** | Repeats until a condition becomes false |


---
