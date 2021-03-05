#Ask user to enter their name

print ("What is your name human?")
name = input()
print ("It's nice to meet you human " + name + ".")
# + operator combines the string without adding a space
# format function can be used to display the same message
# format function uses placeholders {} and then replaces these with the supplied values
#it can be rewritten as follows
print("Nice to meet you {}." .format (name))