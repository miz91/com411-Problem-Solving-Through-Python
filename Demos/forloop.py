#program that displays a message and allow user to select an option 
# use while loop to display the message again n again
option = 1
while (option != 9):
  print ("Please select an option\n\n1.Nice message\n2.Area of a rectangle.\n3.Area of a triangle.\n4.Times table.\n9.Exit")
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
    for i in range (1,11,2):
      print ("{}*{}={}".format (n,i,n*i))

  else:
    print ("You're so dumb")

    ##get fetch --all is used for error