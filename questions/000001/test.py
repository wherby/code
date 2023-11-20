#!/bin/python3

import sys
from bisect import bisect_right,insort_left,bisect_left
res=[]
a1,a2 =1,2
tmp = 0
while a2 <= 4*(10**16):
    if a2 %2 ==0:
        tmp += a2
        res.append((a2,tmp))
    a1,a2 = a2,a1+a2

# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     k = bisect_left(res,(n,0))
#     if res[k][0] != n:
#         k -=1
#     print(res[k][1])

print(len(res),res[-10:])
k = bisect_left(res,(97889062373143904,0))
if k>= len(res):
    k= len(res)-1
if res[k][0] != 37889062373143906:
    k -=1

print(res[k][1])