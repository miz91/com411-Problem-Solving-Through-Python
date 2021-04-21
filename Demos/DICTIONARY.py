# #defining a dictionary

# dict1 = {}

# dict2 ={"Name":"Piotr","age:",26,"allergy": ["coffee","hard working"]}

# dict2["siblings"] = 2
# print (dict2["allergy"])

phonebook ={}

while True:
  name =input("Enter the name ")
  number =input("Enter the number: ")
  phonebook[name]=number
  if input("Type x to stop")== 'x':
    break

def calling(n,book = {}):
  print(f"Calling {n} with a phone number {book[n]}")


calling("Piotr",phonebook)
#print (phonebook)
