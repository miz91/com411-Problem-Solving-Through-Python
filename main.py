print("Where should i look?")
response = input()

if (response == "in the bedroom"):
  print("Where in the bedroom should i look?")
  location = input()
  if (location == "under the bed"):
    print("Found some shoes but no battery")
  else:
   print("Found some mess but no battery")

elif (response == "in the bathroom"):
  print("Where in the bathroom should i look?")
  location = input()
  if(location == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery")

elif (response == "in the lab"):
  print("Where in the lab should i look?")
  location = input ()
  if (location == "on the table"):
    print("Yes! I found my battery")
  else:
    print("Found some tools but no battery")

else:
  print("I do not know where that is but I will keep looking.")


# #Asking user for input
# print("Enter the cover type of the book. hard or soft?")
# cover = input()

# if (cover == "soft"):
#   print("Is the book perfect bound?")
#   perfect_bound = input()

#   #this will only run if the above condition is true

#   if(perfect_bound == "yes"):
#     print("Soft cover, perfect bound books are very popular!")
#   else:
#     print("Soft covers with coils or stitches are great for short books")

# else:
#   print("Books with hard covers can be more expensive!")