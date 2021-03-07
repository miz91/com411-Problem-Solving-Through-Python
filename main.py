<<<<<<< HEAD
#program that displays a message and allow user to select an option 

print ("Please select an option\n\n1.Nice message\n2.Area of a rectangle.\n3.Area of a triangle.\n4.Times table")
option = int (input ())

if option == 1:
  print ("Programming is life")

elif option == 2:
  print ("Enter the length")
  l = int (input())
  print("Enter the width")
  w = int (input())
  area = l*w
  print ("The area of a rectangle is {}".format(area))

elif option == 3:
  print ("Enter the base")
  b = float (input())
  print ("Enter the height")
  h = float (input())
  area = 0.5*b*h
  print("The area of a triangle is {}:" .format (area))

elif option == 4:
  print ("What number timetable would you like to see?")
  n = int (input())
  for i in range (1,11,1):
    print ("{}*{}={}".format (n,i,n*i))

else:
  print ("You're so dumb")



=======
#Improving Beeps health
print ("Enter the number of lives")
lives = int (input ())
print ("Enter the energy level")
energy = int (input ())
print ("Enter the shield level")
shield = int (input ())

print ("Lives:" + "\u2764"*lives)
print ("Energy:" + "\u26E8"* energy)
print ("Shield:"+ "\uF64F"* shield)
>>>>>>> b3c2ff02b8a6d252cad2b104023d3d1a675efdc4
