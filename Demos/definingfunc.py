def room_area (width,length):
  return width*length

def room_name():
  print("What's the name of the room?")
  return input()

def price (name,area):
  if name == "bathroom":
    return 20*area

  elif name == "kitchen":
    return 10*area

  elif name == "bedroom":
    return 5*area

  else:
    return 7*area

def run ():
  name = room_name()
  print ("What's the width of the room?")
  w = float (input())
  print ("What's the length of the room?")
  l = float(input())
  print (f"You should pay £{price(name,room_area(w,l))}")


#run()