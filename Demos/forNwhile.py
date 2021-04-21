#While loop to countdown of numbers from user defined value e.g. if user gives me 5 my code will print 5,4,3,2,1 BOOM

print ("What's your starting number")
start = int(input()) #control variable/counter
start_copy = start

while (start >=1): #condition that needs to be satisfied for loop to continue
  print (start)
  start -=1 #modification to counter variable to avoid infinite loop
print ("BOOM!")

#we can use the for loop to do the same program

for counter in range(star_copy,1,-1):
  print (counter)
print ("BOOM")

