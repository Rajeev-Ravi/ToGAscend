from random import *

#Requests dice parameters, amount of dice, dice face, modifier to apply to the dice as a collective.
dice_amount = int(input("How many dice? "))
dice_face = int(input("How many faces? "))
modifier = int(input("Sum of modifiers? "))
print(" ")

#main loop to determine the rolls from the parameter above. Prints critical successes and failures.
while dice_amount > 0:
  rolled_number = randint(1, dice_face)
  
  print (rolled_number+ modifier)
  
  if rolled_number == dice_face:
    print("Critical success!")
  else:
    pass
  if rolled_number == 1:
    print("Critical Fail!")
  else: 
    pass
  
  print (" ")
  
  dice_amount -= 1
  
