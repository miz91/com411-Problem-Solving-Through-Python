print("What's your name?")
#Variable is a container, which can store date for us in the memory such as string,integer,float,boolean)
name =input()
print ("What's your age?")
age = int (input())
print("What's your bank balance?")
balance = float (input())

print ("Welcome {},You are {} years old,Your bank balance is {:.2f}.".format (name,age,balance))
#:.2f is used to display two decimal number after 