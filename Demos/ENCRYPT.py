
#finding prime numbers using encrypt

def isPrime(x):
  for i in range (2,x):
    if x%i == 0:
      return False
  return True

def findPrime(beginning,finish):
  for j in range(beginning,finish):
    if isPrime(j):
      return j

# firs number has to be smaller for loop

def encrypt():
  print("Provide two integers")
  x = int(input())
  y = int(input())
  prime1 = findPrime(x,y)
  print("Provide two more integers")
  x = int(input())
  y = int(input())
  prime2 = findPrime(x,y)
  return prime1*prime2


print(encrypt(), encrypt())


