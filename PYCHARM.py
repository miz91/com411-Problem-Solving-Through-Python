def entity_details():
  print("Enter an entity e.g. Earth")
  entity = input()
  integar_column = []
  n = int(input ("Enter a list of column integer indexes\n"))

  for i in range (0,n):
    
  

entity_details()

'''
def entity_name():

 print("Enter an entity e.g. Earth")
 answer = input()
 print ("Your have put", answer)

entity_name()


def process_type():

 print("Choose from the menu\n 1. Retrieve entity\n 2. Retrieve entity details\n 3. Categorise entities by type\n 4. Categorise entities by gravity\n 5. Summarise entities by orbit ")

 answer = int(input())

 if answer == 1:
  return answer
 elif answer == 2:
  return answer
 elif answer == 3:
  return answer
 elif answer == 4:
  return answer
 elif answer == 5:
  return answer
 else:
  print("None! You must choose from the menu")

process_type()




def source_data_path():
  print ("Enter a csv file path")
  file_path = input()
  if file_path.endswith(".csv"):
    return file_path
  else:
    print("None")

print (source_data_path())











def student ():
  print("What's your name?")
  name = input()
  print ("What's your age?")
  age = int(input())
  print("Do you have a cat?")
  cat = input()
  if cat == "yes":
    cat_bool = True
  else:
    cat_bool = False
  return name,age,cat_bool  

print ("How many students to generate")
n = int(input())
count = 0
all_students = []
while (count < n):
  tuplex = student ()
  all_students.append(tuplex)
  count+=1
print(all_students)






person = ("Mizan", 30, True)
#Access elements via Index- Just like lists
print (person [1])
if person[2]:
  print("Yay- i am ok")
else:
  print ("I am not ok")

print("Which item to print")
n = int(input())
if n < len(person):
  print (person [n-1])

#you can not modify a tuple
#you can concotanate
print (person + (2000, "Black"))
print (person)

'''