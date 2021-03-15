import random

print ("Please enter the minimun value")
min =int(input())
print ("Please enter the maximum value")
max = int (input())

number = random.randrange (min,max)

print (f"I am thinking of a number between {min} and {max}.Can you guess?")

guess = 0
while (guess != number):
  guess = int (input())
  if guess < number:
    print ("your guess is too low")
  elif guess > number :
    print ("Your guess is too high")
  else:
    break
  print ("Try again")


print ("Congratulations")
