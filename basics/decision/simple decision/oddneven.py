# Asking user for number 
print("Please enter the first number?")
first_number = int(input())

print("Please enter the second  number?")
second_number = int(input())

print("Please enter the third number?")
third_number = int(input()) 

even_numbers = 0
odd_numbers = 0 

# Determine which numbers are even and which are odd
if (first_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (second_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (third_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# Display result
print("There were {} even and {} odd numbers.".format(even_numbers, odd_numbers))