import math
num=[]
for i in range(2,100000):
   k = int(math.sqrt(i))
   for j in range(2,k):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)