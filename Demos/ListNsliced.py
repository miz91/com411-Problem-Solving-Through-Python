# getting input from user using function and for loop

def get_fruits():
  fruits = []
  print("How many fruits you want?")
  n = int(input())

  #in loop it goes from 0 to 3
  for i in range (n):
    print ("Type your fruits")
    fruits.append(input())
  print("Your fruits are {}" .format(fruits))

  #print only itmes by slicing
  #here it starts from 0 to 4 and every second item

  print(f"Your Sliced list: {fruits[0:5:2]}")
 
#print few itemss using negative index

  print(f"Negative index:{fruits[-2:0:-1]}")

get_fruits()
