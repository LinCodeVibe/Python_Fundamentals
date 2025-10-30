# 7 - Word Guessing Game (Python)

##   Overview
This project is a simple **Word Guessing Game** built using Python fundamentals.  
A random word is chosen from a list, and the player must guess its letters one by one before running out of lives.

---

##   How It Works

1. A word is selected randomly from a predefined list.
2. The player starts with **6 lives**.
3. The player guesses letters to reveal hidden characters in the word.
4. If the guessed letter is not in the word, they lose one life.
5. The game ends when the player either:
   - Reveals all letters (**You Win!**)
   - Runs out of lives (**You Lose!**)


---



##   Structure of the Word Guessing Game

The project was built step-by-step with **modular functions** that control different parts of the game — such as selecting a random word, checking guesses, updating the display, and tracking lives.

Below is a simplified breakdown of the project flow (see also the attached flowchart):

```
START
  ↓
Generate a random word
  ↓
Initialize blanks for each letter
  ↓
Ask the user to guess a letter
  ↓
Check the guessed letter → Update display or lose a life
  ↓
Repeat until all letters guessed or lives = 0
  ↓
GAME OVER
```


##   Concepts Used
- **Random module:** to select a random word.  
- **Loops:** to repeat guessing until the game ends.  
- **Conditionals:** to check if guesses are correct or not.  
- **Lists and Sets:** to track correct and wrong guesses.  
- **String manipulation:** for building and displaying the current progress.

---


##  Code explanation

**Random module:**
```
chosen_word = random.choice(word_list)
```
- `random.choice()` is a built-in function from Python’s `random` module.
- It selects one random element from the `word list`.
- The chosen value is stored in the variable `chosen_word`.


---
**Conditionals:**  

```
if len(guess) != 1 or not guess.isalpha():
    print("Please enter a single alphabetic character.\n")
    continue

if guess in correct_letters or guess in wrong_letters:
    print(f"You've already guessed '{guess}'.")
    continue

else:
    ...
```

- `if len(guess) != 1 or not guess.isalpha():`	Ensures input is a single letter
- `if guess in correct_letters or guess in wrong_letters:`  Prevents repeated guesses
- `if guess in chosen_word:`	Handles correct guesses
- `else:`	Handles incorrect guesses (reduces a life)
---

**Lists and Sets:**    
```
revealed_word = ["_"] * len(chosen_word)
correct_letters = set()
wrong_letters = set()
```
- **revealed_word (List):**
Stores the visible progress of the word, using underscores for unguessed letters.
Example: ['_', 'a', '_', '_', 'e']

- **correct_letters and wrong_letters (Sets):**
Track which letters the player has already guessed correctly or incorrectly.
Sets automatically prevent duplicates.

--- 


##   Output

```
Word to guess: _ _ _ _ _ _
(You have 6/6 lives)

============== 6/6 LIVES LEFT  ============== 
Guess a letter: e
You guessed 'e', that's not in the word.
Word to guess: _ _ _ _ _ _
Wrong letters: e

============== 5/6 LIVES LEFT  ============== 
Guess a letter: a
Good guess: 'a' is in the word.
Word to guess: _ a _ _ _ _
Wrong letters: e
```

---

##   Game Outcome
  **Win:** when all letters are revealed.  
  **Lose:** when lives reach zero.

---
 