# TDK gcd
def gcd(a,b):
    while b:
        a,b = b,a %b
    return a

# https://www.geeksforgeeks.org/gcd-in-python/

# Python code to demonstrate naive
# method to compute gcd ( recursion )
  
def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

print(hcfnaive(12,60))
print(hcfnaive(60,12))


import math
  
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (math.gcd(60,48))