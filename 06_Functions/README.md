# 🧩 Day 6 – Python Functions & Karel

## 📘 Overview
In **Day 6**, I learned about **Python functions**, **code indentation**, and how to use **while loops** to control repetitive actions efficiently.  
The lessons also introduced **Reeborg’s World**, an interactive Python maze environment to practice logic and automation.

---

## 🧠 Key Concepts Learned

### 🔹 **Functions in Python**
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
✅ **Concepts learned:**
- Define a function using `def`.
- Call a function by its name followed by `()`.
- Keep indentation consistent for function bodies.

---

### 🧱 **Defining and Calling Functions**
Functions allow us to encapsulate logic that can be executed later.  
Example:

```python
def greet_user():
    name = input("What is your name? ")
    print("Hello, " + name)

print("Welcome!")
greet_user()
```
📤 **Output Example:**
```
Welcome!
What is your name? Angela
Hello, Angela
```

---

### ⚙️ **Code Indentation**
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
print("Hello")  # ❌ IndentationError
```

✅ Learned to structure blocks of code clearly inside functions, loops, and conditionals.

---

### 🔁 **For vs While Loops**
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

### 🧗 **Hurdles & Maze Challenges (Reeborg’s World)**
In **Reeborg’s World**, I practiced controlling a robot using logic, loops, and conditions to solve mazes.  
The environment reinforces the concept of **automation and logical control flow**.

#### Example Code:
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```
✅ **Concepts learned:**
- Created helper functions (`turn_right()`).
- Used `while not at_goal()` to loop until reaching the end.
- Combined conditionals (`if`, `elif`, `else`) to decide the robot’s movement.

---

### ⚡ **Common Challenges**
- **Hurdles Challenge:** Jumping over fixed and variable-height hurdles using loops.  
- **Maze Challenge:** Solving a maze with the **right-hand rule algorithm** (always keep the wall on your right).

---

## 🧩 Code Quiz Highlights

### Example 1: Indentation Error Check
```python
def my_function():
print("Hello")  # ❌ Missing indentation
```
💡 Fix: Indent properly inside the function.

---

### Example 2: Function Execution Order
```python
def my_function():
    print("This will run")
my_function()
```
✅ The code correctly defines and executes a function.

---

### Example 3: Nested Conditions Inside Functions
```python
def my_function():
    a = 3
    if a > 2:
        print("This will run")
my_function()
```
✅ Demonstrates indentation inside nested structures.

---

## 🧠 Summary

| Concept | Description |
|----------|--------------|
| **Function Definition** | Reusable block of organized code |
| **Function Call** | Executes the function’s statements |
| **Indentation** | Defines structure and scope of code |
| **While Loop** | Repeats until a condition becomes false |
| **Reeborg Maze Logic** | Demonstrates condition-based automation |

---

## 🏁 Reflection
Today’s focus was on **breaking problems into smaller parts** using functions and **automating repetitive logic** with loops.  
Learning to control indentation and structure logic cleanly was essential in avoiding errors and building scalable programs.

🚀 **Takeaway:**  
> Functions make code modular and easier to debug. Combining them with loops creates powerful automation workflows — from simple print statements to solving mazes step by step.
