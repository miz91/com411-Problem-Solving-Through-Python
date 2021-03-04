print ("What's your name?")
n = input()
# print("Do you have a dog? (Type True or False)")
# dog = input()

if len (n) > 9 :
  print ("You've a very long name!")
 
  #len is used to get the length of the variable
  #if statement is used to verify true or false
  
  print("Consider shorten it up")
  print("Your name contains {} letters." .format (len(n)))

#elif will only run when if is false

elif len(n) > 6 :
  print ("Your name is bit long")

elif len(n) < 3 :
  print ("Your name is very short") 
 

else:
    print ("Your name is ok")

print ("This is the END of the program!")