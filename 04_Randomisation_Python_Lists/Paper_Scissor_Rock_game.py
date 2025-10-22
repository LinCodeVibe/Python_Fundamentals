import random

rock = '''
   _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
'''
paper = '''
   _______
---'   ____)____
         ______)
         _______)
        _______)
---.__________)
'''
scissors = '''
   _______
---'   ____)____
         ______)
      __________)
     (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

# Rock wins against scissors.  0 > 2
# Scissors wins against paper.  2 > 1
# Paper wins against rock.   1 > 0

user_choice = int(input("what to you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
if user_choice >= 0 and user_choice <= 3:
   print(game_image[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
print(game_image[computer_choice])

if user_choice >= 3 or user_choice < 0:
   print("You type an invalid number. You lose! ")
elif user_choice == 0 and computer_choice == 2:
   print("You win!")
elif user_choice == 2 and computer_choice == 0:
   print ("You loose!")
elif user_choice < computer_choice:
   print("You lose!")
elif user_choice > computer_choice:
   print("You win!")
elif user_choice == computer_choice:
   print("It's a draw")





