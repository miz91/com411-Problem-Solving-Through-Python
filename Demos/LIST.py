#define an empty list

fruits = [] #defining a list

#defining a list with items

vegetables = ["Carrot", "Peas"]

#to add items we can use .append method

fruits.append ("Apple")
fruits.append ("Banana")
fruits.append ("Tomatoe")
fruits.append ("Banana")

#we can remove an item using .remove

fruits.remove("Apple")
print(fruits)

#we can also remove item by index. index starts from 0. we use del function for that
del fruits[1]

print(fruits)
#insert a value not at the end

fruits.insert(1, "Pineapple")
print(fruits)



#print(vegetables)