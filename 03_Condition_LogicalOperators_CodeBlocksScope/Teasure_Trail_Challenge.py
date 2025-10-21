print(r'''
     /\____;;___\
      | /         /
      `. ())oo() .
       |\(%()*^^()^\
      %| |-%-------|
     % \ | %  ))   |
     %  \|%________|      
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("You're at a crossroad, where do you want to go? The left or right?\n").lower()
if left_right == "left":
   swim_wait = input("you've come to a lake. There is an island in the middle of the lake."
                     "\nType \"wait\" to wait for a boat. "
                     "Type \"swim\" to swim across.\n").lower()
   if swim_wait == "wait":
       which_door = input("You arrive at the island unharmed. There is a house with 3 doors."
                          "One red, one yellow and one blue. "
                          "Which colour do you choose?\n").lower()
       if which_door == "red":
           print("Burned by fire. Game Over. ")
       elif which_door == "yellow":
           print("You Win!")
       elif which_door == "blue":
           print("Eaten by beasts. Game Over. ")
       else:
           print("You choose a door that doesn't exist. Game Over.")
   else:
       print("Attacked by trout. Game Over.")
else:
   print("Fail into a hole. Game Over.")





