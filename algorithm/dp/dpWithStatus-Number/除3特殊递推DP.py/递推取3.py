# https://codeforces.com/gym/105940/problem/A
# 返回counter 累积 状态
from collections import defaultdict,deque
from functools import cache
from collections import Counter
n= 6


mod = 10**9+7

@cache
def dfs(idx,n0,n1,n2,cur):
    if idx == n: 
        c = Counter()
        c[(n0,n1,n2,cur)] =1
        return c
    start = 0
    if idx == 0 :
        start =1
    ret = Counter() 
    for i in range(start,10):
        nn0,nn1,nn2,ncur = n0  ,n1,n2,(cur+i)%3
        nn0 += int(ncur==0)
        nn1 += int(ncur ==1)
        nn2 += int(ncur ==2)
        nn0 = nn0%3 
        nn1 = nn1%3 
        nn2 = nn2%3 
        ret +=  dfs(idx+1,nn0,nn1,nn2,ncur)
    return ret
import math
ans= 0
ret = dfs(0,1,0,0,0)
for n0 in range(3):
    for n1 in range(3):
        for n2 in range(3):
            for cur in range(3):
                if (math.comb(n0,2) + math.comb(n1,2) + math.comb(n2,2))%3 ==0 :
                    ans += ret[(n0,n1,n2,cur)]%mod
print(ans%mod)