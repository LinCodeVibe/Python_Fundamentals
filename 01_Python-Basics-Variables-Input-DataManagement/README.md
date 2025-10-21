# 🧾 1_Python Basics: Variables, Input, and Data Management
**Topic:** Working with Variables in Python to Manage Data  

This covered Python fundamentals focusing on how to print, collect user input, manipulate strings, and store values in variables.  
 

---

---

## 🧩 Summary of Concepts

| Concept | Function | Purpose |
|----------|-----------|----------|
| Printing | `print()` | Display text or variables |
| String Manipulation | `"A" + "B"`, `\n` | Combine or format text |
| User Input | `input()` | Get data from the user |
| Variable | `x = value` | Store information |
| Length | `len()` | Count characters |
| Conversion | `str()`, `int()` | Change data type |
| Naming Rules | — | Write clear, valid variable names |

---

## 🖨️ Printing

### Description
Use the `print()` function to display text or variables in the console.

```python
print("Hello world!")
```

### Notes
- Text should always be enclosed in quotes `" "`.
- You can print multiple lines or combine strings and variables.


### Example
```python
print("Hello world!")
print("Welcome to Python!")
```

**Output**
```
Hello world!
Welcome to Python!
```

---

## 🧵 String Manipulation

### Description
Strings can be joined (concatenated) and formatted using escape sequences like `\n` for new lines.

### Example 1 – New Lines
```python
print("Hello world!\nHello world!\nHello world!")
```
**Output**
```
Hello world!
Hello world!
Hello world!
```

### Example 2 – Add Spaces
```python
print("Hello" + " " + "Python")
```
**Output**
```
Hello Python
```

✅ **Key Idea:**  
`+` joins strings, and `\n` creates a new line.

---

## ⌨️ Inputs

### Description
The `input()` function collects user input during program execution.  
It You can store the input in a variable and reuse it later.

```python
name = input("What is your name? ")
print("Hello " + name + "!")
```

**Output**
```
What is your name? Python
Hello Python!
```

✅ **Key Idea:**  
`input()` always returns a string (even if you type numbers).

---

## 📦 Variables

### Description
Variables act as containers that store data for later use.

### Example 1 – Count Characters
```python
username = input("Enter your name: ")
length = len(username)
print(length)
```

### Example 2 – Use Variables Together
```python
username = input("Enter your name: ")
length = len(username)
print("Your name has " + str(length) + " characters.")
```

**Output**
```
Enter your name: Python
Your name has 6 characters.
```

✅ **Key Idea:**  
Use `len()` to count characters and `str()` to convert numbers to strings for printing.

---

## 🏷️ Variable Naming Rules

Follow these rules for clear, professional Python code:

1. Use **descriptive** names (e.g., `user_name`, not `x`).  
2. Don’t include **spaces** — use underscores `_` instead.  
3. Don’t start names with **numbers**.  
4. Avoid Python **keywords** such as `print`, `input`, `len`.  
5. Use **lowercase letters** for normal variables.  
6. Follow **company or project style guides** when applicable.

✅ **Good Example**
```python
city_name = "San Francisco"
```

🚫 **Bad Example**
```python
3city = "San Francisco"     # starts with a number
print = "Hello"        # overwrites built-in function
```

---

## 🎵 Mini Project: Creative Name Generator

### Goal
Combine user input and variables to create a fun, personalized name.

### Steps
1. Create a greeting message.  
2. Ask for the **city** where the user grew up.  
3. Ask for the **name of a pet**.  
4. Combine both names and display the result.  
5. Ensure the cursor appears on a new line for each prompt.

### Code
```python
print("Welcome to the Creative Name Generator!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your creative name could be " + city + " " + pet)
```

**Output**
```
Welcome to the Creative Name Generator!
What's the name of the city you grew up in?
> San Jose
What's your pet's name?
> Whiskers
Your creative name could be San Jose Whiskers
```



 
