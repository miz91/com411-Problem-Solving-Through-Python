#Asking user for input
print("Enter the cover type of the book. hard or soft?")
cover = input()

if (cover == "soft"):
  print("Is the book perfect bound?")
  perfect_bound = input()

  #this will only run if the above condition is true

  if(perfect_bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")

else:
  print("Books with hard covers can be more expensive!")