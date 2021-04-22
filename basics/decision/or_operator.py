
#asking user for input
print ("Enter the type of adventure")
type = input ()

#the program will run if either one is true
if ((type == "scary") or (type == "short")):
  print("Entering the dark forest!")
elif ((type == "safe") or (type == "long")):
  print("Taking the safe route!")

else:
  print("Not sure which route to take")