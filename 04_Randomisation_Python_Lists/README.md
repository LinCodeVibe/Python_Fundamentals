# 4 – Python Randomisation and Lists

## Overview
To use **Python’s random module** and **list data structures** to build interactive, randomized programs such as *Banker Roulette* and *Rock, Paper, Scissors*.

---

##  Topics Covered

### 1. Randomisation in Python
Randomisation allows the program to introduce unpredictability, focus on perfect for games, quizzes, and simulations.

####   Key Functions
- **`random.randint(a, b)`** → returns a random integer between *a* and *b* (inclusive)
- **`random.random()`** → generates a random float between 0.0 and 1.0
- **`random.uniform(a, b)`** → generates a random float between *a* and *b*
- **`random.choice(list)`** → selects a random element from a list

#### Example
```python
import random

# Random integer between 1 and 10
random_int = random.randint(1, 10)
print(random_int)

# Random float between 0 and 1
random_float = random.random()
print(random_float)

# Random float between 1 and 5
random_float_custom = random.uniform(1, 5)
print(random_float_custom)
```

#### Heads or Tails Example
```python
import random

result = random.randint(0, 1)
if result == 0:
    print("Heads")
else:
    print("Tails")
```

---

### 2. Lists in Python

Lists store **multiple items** in a single variable, making them ideal for managing groups of data like names, fruits, or game options.

#### Key Concepts
- **Accessing items:** `my_list[index]`
- **Negative indices:** `my_list[-1]` → last item
- **Changing items:** `my_list[index] = new_value`
- **Adding items:**
  - `my_list.append(item)` → adds to end
  - `my_list.extend(list)` → adds multiple items
- **Length:** `len(my_list)`
- **Nested lists:** lists inside other lists

#### Example
```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])   # "Apple"
fruits.append("Orange")
print(fruits)      # ["Apple", "Banana", "Cherry", "Orange"]
```

#### 🧩 Nested List Example
```python
fruits = ["Strawberries", "Apples"]
vegetables = ["Spinach", "Celery"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][0])  # Output: "Spinach"
```

---

## Mini Python Project - Who Pays the Bill – A Random Friend Picker

### Description
Pick one random person from a list to pay the bill — a fun way to practice list indexing and random selection!

#### Code
```python
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payer = random.choice(friends)
print(f"{payer} is going to buy the meal today!")
```

---

## Mini Project - Rock, Paper, Scissors

### Description
Simulate the classic game between a user and the computer using lists and randomisation.

#### Code 
```python
import random

choices = ["Rock", "Paper", "Scissors"]
user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("Invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("It's a draw!")
```

---

## Key Takeaways
- Mastered Python **random module** and its functions (`randint`, `choice`, etc.)
- Practiced creating and manipulating **lists**
- Learned about **nested lists**
- Built two interactive projects combining both concepts

---

##  References
- [Python `random` module documentation](https://docs.python.org/3/library/random.html)

---

