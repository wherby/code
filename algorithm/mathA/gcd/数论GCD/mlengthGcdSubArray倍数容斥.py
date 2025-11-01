
from collections import Counter

import math
def getMlengthGcd(ls,m):
    c = Counter(ls)
    mx = max(ls)
    gcd_count = [0]*(mx+1)
    for i in range(1,mx+1):
        for j in range(i*2,mx+1,i):
            c[i] += c[j]

    for i in range(mx, 0,-1):
        gcd_count[i] = math.comb(c[i],m)
        for j in range(i*2,mx+1,i):
            gcd_count[i] -= gcd_count[j]
    return gcd_count

ls = [2,4,6,8,10,12]
print(getMlengthGcd(ls,3))
print(getMlengthGcd(ls,2))