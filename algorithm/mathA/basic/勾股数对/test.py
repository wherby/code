c = (7**2 + 3**2) //2
print(c)
import math
for a in range(1,50):
    for b in range(1,50):
        if a**2+ b**2== int(math.sqrt(a**2+b**2))**2:
            print(a,b,int(math.sqrt(a**2+b**2)))