print("What's your name?")
#Variable is a container, which can store date for us in the memory such as string,integer,float,boolean)
name =input()
#input is used to get the data from the user

print ("What's your age?")
age = int (input())
#Casting is used to specify variable

print("What's your bank balance?")
balance = float (input())

print ("Welcome {},You are {} years old,Your bank balance is {:.2f}.".format (name,age,balance))
# .format is used to pull the data of variable
#:.2f is used to display two decimal number after 