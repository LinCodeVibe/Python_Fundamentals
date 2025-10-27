# 5 – Python Loops

## Overview
To use **for loops** in Python to automate repetitive tasks.  
Loops are essential for working with collections like **lists** and **ranges**, and they make code more efficient by removing the need for manual repetition. It focused on building a strong foundation for iteration, working with numerical sequences, and combining logic with loops to solve real-world problems.

---

##  Key Topics Covered

### **For Loops**
A `for` loop allows us to execute a block of code multiple times — once for each element in a list or range.

```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)
```

 **Concept:** The variable `fruit` represents each item in the list as the loop iterates through it.

---

### **Highest Score Exercise**
This exercise simulated how the built-in `sum()` and `max()` functions work internally.

```python
student_scores = [150, 142, 185, 120, 171, 184, 149]

# Sum using loop
total_score = 0
for score in student_scores:
    total_score += score
print(f"Total score: {total_score}")

# Find highest score without using max()
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"Highest score: {highest_score}")
```

 **Concepts learned:**
- Using `for` loops to iterate through lists.
- Comparing elements using conditionals.
- Understanding how built-in functions work behind the scenes.

---

### **For Loops with Range**
The `range()` function is used to generate a sequence of numbers that can be looped through.

```python
for number in range(1, 10):
    print(number)

# Step through every 2 numbers
for number in range(1, 11, 2):
    print(number)

# Gauss Challenge – sum 1 to 100
total = 0
for num in range(1, 101):
    total += num
print(total)  # Output: 5050
```

 **Concepts learned:**
- Using `range(start, stop, step)`.
- Summing sequences.
- Practicing logic through mathematical patterns.

---

### **FizzBuzz Challenge**
A classic logic challenge combining loops and conditionals.

```python
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

 **Concepts learned:**
- Modular arithmetic (`%`).
- Multiple condition checking using `if`, `elif`, and `else`.
- Applying control flow to iteration.

---

### **Password Generator Project**
A fun final project combining loops, lists, and randomness.

```python
import random

letters = ['a', 'b', 'c', ..., 'z']
numbers = ['0', '1', '2', ..., '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like?"))
nr_symbols = int(input("How many symbols would you like?"))
nr_numbers = int(input("How many numbers would you like?"))

# Easy Version
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

# Hard Version (shuffled)
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

final_password = ""
for char in password_list:
    final_password += char
print(f"Your password is: {final_password}")
```

```
# Output:
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
3

['C', 'a', '3', '*', 'b', '&', '9', 'D', '7']
['9', '3', 'b', '&', 'a', 'D', 'C', '7', '*']
Your password is: 93b&aDC7*
```

  **Concepts learned:**
- Combining `for` loops with `random.choice()`.
- Using `random.shuffle()` to randomize order.
- Building step-by-step logic from user input to final output.

---

## **Summary**
| Concept | Description |
|----------|--------------|
| **For Loop** | Repeats actions over lists or ranges |
| **Range Function** | Generates numeric sequences |
| **Sum & Max Simulation** | Demonstrated loops for aggregation and comparison |
| **FizzBuzz** | Practiced combining logic and iteration |
| **Password Generator** | Applied loops, randomization, and lists in a creative project |

