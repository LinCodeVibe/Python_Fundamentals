# 🧩 3 – Conditional Statements, Logical Operators, and Projects

## 📘 Overview
Exploring **decision-making in Python** — using `if`, `elif`, and `else` to make programs react differently based on conditions.  
Also **logical operators**, **nested conditions**, and applied them in real-world projects like **Rollercoaster Ticket System**, **BMI Interpreter**, and **Treasure Trail Challenge Game**

---


## 🧮 Key Concepts

| Concept | Description | Example |
|----------|--------------|----------|
| `if / else` | Runs code based on condition | `if age > 18:` |
| `elif` | Adds more conditions | `elif age > 12:` |
| Nested Conditions | Conditions inside other conditions | Multiple checks |
| Modulo (%) | Finds remainder | `num % 2` |
| Logical Operators | Combine multiple conditions | `and`, `or`, `not` |
| Scope | Variable accessibility | Inside/outside block |

---

## 🔹 1. Conditional Statements (`if / else`)

### Example
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

**Concept:**  
- `if` executes when the condition is **True**  
- `else` executes when the condition is **False**

### 🧭 Flowchart
```
Start
 └─> Height > 120?
       ├─ Yes → Can ride
       └─ No  → Can't ride
```

---

## 🔹 2. Modulo Operator (%)

The modulo operator gives the **remainder** of a division.

### Example
```python
print(10 % 3)  # Output: 1
```

### Odd or Even Checker
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
```

✅ **Key Idea:**  
If a number is divisible by 2 (remainder = 0), it’s even.

---

## 🔹 3. Nested `if` / `elif` / `else`

You can put conditional statements inside each other.

### Example
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    
    if age <= 12:
        print("Child tickets are $5.")
    elif age <= 18:
        print("Teen tickets are $7.")
    else:
        print("Adult tickets are $12.")
else:
    print("Sorry, you must grow taller before you can ride.")
```

### 🎡 Flowchart
```
Start
 └─> Height > 120?
       ├─ No → Can't ride
       └─ Yes → Ask Age
                ├─ Under 12 → $5
                ├─ 12–18 → $7
                └─ Over 18 → $12
```

✅ **Concepts Learned:**
- Nested logic for multiple decisions  
- Age-based ticket pricing  
- Readability via indentation and scope

---

## 🔹 4. BMI Calculator with Interpretation

Expanding on the previous BMI calculator, it added **if/elif/else** logic to interpret results.

### Example
```python
weight = 85
height = 1.85
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
else:
    print("Overweight")
```

### BMI Ranges
| Category | BMI Range |
|-----------|------------|
| Underweight | < 18.5 |
| Normal Weight | 18.5 – 24.9 |
| Overweight | ≥ 25 |

 

---

## 🔹 5. Logical Operators

| Operator | Meaning | Example |
|-----------|----------|----------|
| `and` | Both conditions must be True | `if age > 18 and height > 120:` |
| `or` | At least one condition is True | `if is_student or is_member:` |
| `not` | Inverts True ↔ False | `if not raining:` |

Example:
```python
if age > 18 and height > 120:
    print("You can ride the rollercoaster!")
```

---

## 🧩 6. Code Blocks & Scope
- Code inside an `if` statement is **indented** → part of that code block.  
- Variables defined inside a block have **local scope** (only exist inside it).  
- Variables outside a block have **global scope**.

Example:
```python
score = 10

def add_points():
    bonus = 5   # local variable
    print(score + bonus)

add_points()  # ✅ Works
print(bonus)  # ❌ Error: bonus is not defined
```

---




### 7. `if / elif / else` vs. Multiple `if`
| Type | Description | Behavior |
|------|--------------|-----------|
| `if / elif / else` | Used when conditions are **mutually exclusive** | Only one branch runs |
| Multiple `if` | Used when conditions are **independent** | All true conditions execute |

```python
# if / elif / else --> Only one block runs. 
if condition1:
    do_A()
elif condition2:
    do_B()
else:
    do_C()

# Multiple if statements --> multiple blocks can run if conditions are true.
if condition1:
    do_A()
if condition2:
    do_B()
if condition3:
    do_C()
```

---

### 8. Nested Conditions – Rollercoaster Example
We applied **nested `if` statements** to check both height and age before allowing someone to ride a rollercoaster.

#### 🧮 Example Code
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

#### 🎡 Flowchart
```
Start → Height > 120cm?
   ├─ No → Can't ride
   └─ Yes → Ask age
             ├─ <12 → $5
             ├─ 12–18 → $7
             ├─ ≥18 → $12
             ↓
             Ask for photos (+$3 if yes)
             ↓
             Show total bill
```

---

### 9. Logical Operators
Python allows combining multiple conditions using **`and`**, **`or`**, and **`not`**.

| Operator | Meaning | Example |
|-----------|----------|----------|
| `and` | Both must be True | `if age > 18 and height > 120:` |
| `or` | At least one is True | `if is_student or is_member:` |
| `not` | Reverses a condition | `if not raining:` |

#### Example: Free Ride for Age 45–55
```python
if age >= 45 and age <= 55:
    print("You ride for free!")
```

---

### 10. Rollercoaster Billing System
**Goal:** Decide ride eligibility and calculate ticket price based on height, age, and photo preference.

**Concepts Used:**  
- Nested `if` statements  
- Logical operators  
- Variable updates and condition chaining

**Flowchart:**  
Includes checks for:
1. Height requirement (≥120 cm)  
2. Age groups and ticket prices  
3. Optional photo cost (+$3)

---

### 11.  Python Pizza Order
**Goal:** Build a pizza ordering system that calculates price based on user preferences.

#### Example Code
```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

pizza_bill = 0

if size == "S":
    pizza_bill += 15
elif size == "M":
    pizza_bill += 20
elif size == "L":
    pizza_bill += 25

if pepperoni == "Y":
    if size == "S":
        pizza_bill += 2
    else:
        pizza_bill += 3

if extra_cheese == "Y":
    pizza_bill += 1

print(f"Your final bill is: ${pizza_bill}")
```

✅ **Output Example**
```
Welcome to Python Pizza Deliveries!
Size: L
Pepperoni: Y
Extra Cheese: N
Your final bill is: $28
```

---

### 12. Mini Project – Treasure Trail Challenge Game

In this adventure, the player’s goal is to **find hidden treasure** by making a series of choices.  
Each decision leads to a different outcome — from glorious victory to humorous **Game Over** moments.  
This exercise reinforces how to structure decision trees and manage multiple conditional paths in code.

---

## 🧭 Flow Summary

```
Welcome to Treasure Island.
Your mission is to find the treasure.
↓
Left or Right?
 ├── Right → Fall into a hole → Game Over
 └── Left → Swim or Wait?
       ├── Swim → Attacked by trout → Game Over
       └── Wait → Which door?
             ├── Red → Burned by fire → Game Over
             ├── Blue → Eaten by beasts → Game Over
             ├── Yellow → You Win!
             └── Else → Game Over
```

---

## 💻  Code

```python
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right':\n").lower()

if left_right == "left":
    swim_wait = input("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across:\n").lower()
    if swim_wait == "wait":
        which_door = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow, and one blue. Which color do you choose?\n").lower()
        if which_door == "red":
            print("Burned by fire. Game Over.")
        elif which_door == "yellow":
            print("You Win!")
        elif which_door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("You chose a door that doesn’t exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
```

---

## 🎮 Output

```
Welcome to Treasure Island.
Your mission is to find the treasure.

You're at a crossroad. Where do you want to go? left or right?
> left
You've come to a lake. Type "wait" to wait for a boat or "swim" to swim across.
> wait
You arrive at the island unharmed. There is a house with 3 doors: red, yellow, and blue.
> yellow
You Win!
```

---

## ✅ Key Takeaways
- Practice **nested `if` / `elif` / `else`** structures  
- Use `.lower()` to normalize user input  
- Apply **logical operators** (`and`, `or`, `not`) for combined conditions  
- Learn **flow control through decision trees**  
- Build a text-based game using simple Python input/output  
 

---

## 🧩 Summary
| Topic | Description | Example Project |
|--------|--------------|----------------|
| Conditional Statements | Making code react to decisions | Rollercoaster |
| Nested `if` Blocks | Multi-level logic | Rollercoaster 2.0 |
| Logical Operators | Combine multiple checks | Age 45–55 modifier |
| Independent `if`s | Allow multiple actions | Pizza toppings |
| Control Flow Design | Logical sequence in decisions | Treasure Trail Challenge Game  |

---

## ✅ Reflection
By the end of Day 3, we learned how to:  
- Control program flow with conditional logic.  
- Use nested and multiple `if` statements for real-world decision logic.  
- Combine conditions using logical operators (`and`, `or`, `not`).  
- Translate logic into flowcharts to design clear program structures.  

Projects like **Rollercoaster**, **Pizza Order**, and **Treasure Island** showcased how control flow allows Python programs to make intelligent choices. 🧠✨
