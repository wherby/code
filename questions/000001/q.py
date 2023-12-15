a = 187225577
import math
ls =[]
idx = 2
while idx<= int(math.sqrt(a)) +1 :
    while a %idx ==0:
        ls.append(idx )
        a = a//idx
    idx +=1
if a != 1:
    ls.append(a)
print(ls)
print(2431501*11*7)