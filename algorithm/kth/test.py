
import math
ls = [5,6,7]

def per(ls):
    sm = sum(ls)
    acc = 1
    for a in ls:
        acc *=math.comb(sm,a)
        sm -=a 
    return acc 

print(per(ls))
ls1 =list(ls)
ls2 =list(ls)
ls3 = list(ls)
ls1[0] -=1
ls2[1] -=1
ls3[2] -=1
print(per(ls1) + per(ls2) +per(ls3))

