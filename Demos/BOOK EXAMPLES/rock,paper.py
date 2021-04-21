#playing a game of rock paper n scissors with computer

import random

random_choice= random.randint(0,2)
# print("The computer chooses",random_choice)

if random_choice == 0:
  computer_choice = "Rock"
elif random_choice == 1:
  computer_choice = "Paper"
else:
  computer_choice = "Scissors"

user_choice = input("Rock,Paper,Scissors\n")
print ("You choose", user_choice, "and the Computer choose", computer_choice)

# print ("The computer choice is", computer_choice)



# if bank_balance >= ferrrari_cost:
#   print("Why not!")
#   print("Go aheaa and buy it")

# else:
#   print("Sorry")
#   print("Try again next week")