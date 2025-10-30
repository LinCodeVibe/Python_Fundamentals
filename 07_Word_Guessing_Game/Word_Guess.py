
import random
word_list = ["planet", "guitar", "coffee", "bridge", "forest",
           "butterfly", "rocket", "dream", "island", "camera"]
MAX_LIVES = 6
lives = MAX_LIVES
chosen_word = random.choice(word_list)
revealed_word = ["_"] * len(chosen_word)
correct_letters = set()
wrong_letters = set()
print("Word to guess: " + " ".join(revealed_word))
print(f"(You have {lives}/{MAX_LIVES} lives)\n")
game_over = False
while not game_over:
    print(f"============== {lives}/{MAX_LIVES} LIVES LEFT  ============== ")
    guess = input("Guess a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.\n")
        continue
    if guess in correct_letters or guess in wrong_letters:
        print(f"You've already guessed '{guess}'.")
        print("Word to guess: " + " ".join(revealed_word))
        if wrong_letters:
            print("Wrong letters so far: " + ", ".join(sorted(wrong_letters)))
        print()
        continue
    if guess in chosen_word:
        correct_letters.add(guess)
        # Show the positions of that letter
        for i, ch in enumerate(chosen_word):
            if ch == guess:
                revealed_word[i] = guess
        print(f"Good guess: '{guess}' is in the word.")
    else:
        wrong_letters.add(guess)
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word.")
    # Current status
    print("Word to guess: " + " ".join(revealed_word))
    if wrong_letters:
        print("Wrong letters: " + ", ".join(sorted(wrong_letters)))
    print()
    # Checks
    if "_" not in revealed_word:
        game_over = True
        print("==============   YOU WIN  ============== ")
        print(f"The word was: {chosen_word}")
    elif lives == 0:
        game_over = True
        print("==============   YOU LOSE  ============== ")
        print(f"The word was: {chosen_word}")
