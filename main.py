#while loop and for loop is used to have a repetition of a procedure in our code

print ("How many times to print the symbol?")
x = int (input()) #x = 3

# i is a counter- it keeps track of how many times we went through the loop

i = 0

while i < x : #condition for repeating the loop as long as i lower than x
  print ("\u27BD", i) #i is used to get the number
  i = i+1 #new value of counter is +1

print("We left the loop")