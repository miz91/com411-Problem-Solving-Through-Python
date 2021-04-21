#defining my own function to calculate the area of a triangle

def calculate_area ():
  h = 10
  b = 5
  area = 0.5*h*b
  print (area)

 #need to call the function
 
calculate_area()

#Parameter is a value you plug into a function
#Lets put parameter into the function

def calculate_area (h,b):
  area = 0.5*h*b
  print(area)

calculate_area (10,10)

#to get the value from user

def calculate_are (h,b):
  area = 0.5*h*b
  print(area)

print("Enter the height and base")
h = float (input())
b = float (input())

calculate_area (h,b)

#we can replace the value of the parameter

def calculate_area (h=10,b=5):
  area = 0.5*h*b
  print (area)

calculate_area ()
calculate_area (4) 
#by default function will change the first value
calculate_area (b=20)

#returning value

def calculate_area (h=10,b=15):
  area = 0.5*h*b
  return area

print (calculate_area ())
x= calculate_area (12,3)
print (x+1)

#lets call another function

def calculate_area (h=10,b=5):
  area = 0.5*h*b
  return area

def run ():
  x = calculate_area(4)
  x += 1 #x = x+1
  print (f"The area of the triangle is {x}")
  #call for the function
run()