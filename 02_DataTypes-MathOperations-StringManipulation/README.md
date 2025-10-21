# 🧮 2 – Data Types, Math Operations, and String Manipulation

## 📘 Overview
Focused on mastering **Python’s primitive data types**, **mathematical operations**, and **string manipulation** techniques. It concluded with two mini projects: a **BMI Calculator** and a **Tip Calculator** — applying math, user input, and formatted output. 

---

## 🧠 Summary of Concepts

| Topic | Key Function | Purpose |
|--------|---------------|----------|
| **Strings** | `"Hello"[0]`, `len()` | Manipulate text |
| **Type Checking** | `type()` | Identify variable type |
| **Type Conversion** | `int()`, `float()`, `str()` | Change between data types |
| **Math Operators** | `+ - * / // **` | Perform calculations |
| **Rounding** | `round(number, n)` | Limit decimal places |
| **f-Strings** | `f"{var}"` | Combine text and variables |
| **Project** | BMI & Tip Calculator | Apply all learned concepts |

---

## 🔢 Python Primitive Data Types

### **1. Strings**
```python
print(len("Hello"))       # Output: 5
print("Hello"[0])         # H
print("Hello"[-1])        # o
print("123" + "345")      # String concatenation → 123345
```
✅ **Key Concept:** Strings are text values enclosed in quotes. They support slicing, concatenation, and indexing.

---

### **2. Integers**
```python
print(123 + 345)
print(123_456_789)  # Underscores improve readability
```
✅ Whole numbers — used for counting and arithmetic. Underscores don’t affect the value.

---

### **3. Floats**
```python
print(3.14159)
```
✅ Numbers with decimals — used for precise mathematical operations.

---

### **4. Booleans**
```python
print(True)
print(False)
```
✅ Represent truth values, commonly used in conditionals and comparisons.

---

## ⚠️ Type Errors, Checking, and Conversion

### **TypeError**
Occurs when a function receives an incompatible data type.
```python
len(12345)   # ❌ TypeError: object of type 'int' has no len()
```
✅ Fix:
```python
print(len("12345"))   # ✅ Works with strings
```

---

### **Type Checking**
```python
print(type("Hello"))   # <class 'str'>
print(type(123))       # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
```

---

### **Type Conversion**
Convert between types with:
| Function | Converts To | Example | Output |
|-----------|--------------|---------|---------|
| `int()`   | Integer | `int("123")` | 123 |
| `float()` | Float | `float("3.14")` | 3.14 |
| `str()`   | String | `str(456)` | "456" |
| `bool()`  | Boolean | `bool(0)` | False |

Example:
```python
print(int("123") + int("456"))  # 579
```

---

### **Challenge: Fix the TypeError**
```python
# ❌ Incorrect
print("Number of letters in your name: " + len(input("Enter your name: ")))

# ✅ Fixed
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
```

---

## ➗ Mathematical Operations

### **Basic Operators**
| Operator | Meaning | Example | Result |
|-----------|----------|----------|---------|
| `+` | Addition | `3 + 2` | 5 |
| `-` | Subtraction | `5 - 2` | 3 |
| `*` | Multiplication | `3 * 3` | 9 |
| `/` | Division | `5 / 2` | 2.5 |
| `//` | Floor Division | `5 // 2` | 2 |
| `**` | Exponent | `2 ** 3` | 8 |

### **PEMDAS Rule**
Parentheses → Exponents → Multiplication/Division → Addition/Subtraction

```python
print(3 * 3 + 3 / 3 - 3)   # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0
```

---

## ⚖️ Coding Exercise 1: Weight & Height Ratio Tool

### **Goal**
Calculate Body Mass Index using user input.

**Formula:**  
> BMI = weight / (height ** 2)

### **Code**
```python
height = 1.65
weight = 84
bmi = weight / (height ** 2)
print(bmi)
```

✅ Output:
```
30.82750582750583
```
✅ **Key Concept:**  
Exponentiation (`**`) squares the height value. BMI helps determine if someone is underweight, normal, or overweight.

---

## 🔢 Number Manipulation & f-Strings

### **Flooring and Rounding**
```python
print(int(3.73849))    # 3 → removes decimal
print(round(3.14159))  # 3 → rounds to nearest whole
print(round(3.14159, 2))  # 3.14 → 2 decimal places
```

### **Assignment Operators**
```python
score = 0
score += 1   # Adds 1
score -= 1   # Subtracts 1
```

### **f-Strings (String Interpolation)**
```python
score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}, your height is {height}, you are winning: {is_winning}")
```
✅ Output:
```
Your score is 0, your height is 1.8, you are winning: True
```
✅ **Key Concept:**  
`f"Text {variable}"` allows inserting values directly into strings.

---

## 💰 Coding Project: Tip Calculator

### **Goal**
Split a restaurant bill evenly with tips included.

### **Code**
```python
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = bill * tip / 100
each_person_pay = round((bill + total_tip) / people, 2)

print(f"Each person should pay: ${each_person_pay}")
```

✅ **Example Output**
```
Welcome to the tip calculator!
What was the total bill? $153.45
What percentage tip would you like to give? 12
How many people to split the bill? 5
Each person should pay: $34.37
```

✅ **Concepts Practiced**
- `float()` and `int()` conversions for user input  
- Arithmetic operations and rounding  
- `f-string` for formatted output  

 

