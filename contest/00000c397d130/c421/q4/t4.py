from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

mod = 10**9+7
def mutliply(m1,m2):
    n = len(m1)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t =0 
            for k in range(n):
                t += m1[i][k]*m2[k][j]
            ret[i][j] = t %mod
    return ret
def matrixPow(mx,y):
    n = len(mx)
    ret =[[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] =1
    cur = mx 
    while y>0:
        if y & 1:
            ret = mutliply(ret,cur)
        cur = mutliply(cur,cur)
        y = y //2
    return ret

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7
        ls= [0]*26
        for a in s:
            ls[ord(a) - ord('a')] +=1
        
        tls= [[0]*26 for _ in range(26)]
        for i in range(25):
            tls[i][i+1]=1
        tls[25][0]=1
        tls[25][1]=1

        #print(tls)
        #print(matrixPow(tls,200))
        tlss = matrixPow(tls,t)
        acc = 0
        #print(tlss)
        #print(ls)
        for i,a in enumerate(ls):
            acc += sum([b*a for b in tlss[i]])
            #print(i,a,acc,tlss[i])
            
        return acc%mod





re =Solution().lengthAfterTransformations( s = "abcyy", t = 2)
print(re)