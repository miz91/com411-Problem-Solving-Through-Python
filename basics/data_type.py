print ("Whats your name")
name = str (input ())
print ("Whats your age in years")
age = int (input ())
print ("Whats your weight in kg")
weight = float (input ())
print ("Whats your height in cm")
height = float (input ())

bmi = weight/(height**2)

print ("{} you are {} years old and your bmi is {:.2f}" .format (name,age,bmi))