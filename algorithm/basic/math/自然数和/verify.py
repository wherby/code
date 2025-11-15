# (-1 + (1+8*m)**(1/2)) //2  == k 

ls = [0]
M = 30
for i in range(1,M):
    ls.append(ls[-1] + i )

print(ls)

import math
from bisect import bisect_right,insort_left,bisect_left
for i in range(1,ls[-1]):
    k = int((-1 +math.sqrt(1 + 8*i)) /2) 
    #print(k ,bisect_right(ls,i)-1)
    if k != bisect_right(ls,i)-1:
        print(k)




