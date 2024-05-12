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

def getKBitsArray(n):
    return [n//(1<<(k+1)) *(1<<k) + max(0, n %(1<<(k+1)) - (1<<k)+1) for k in range(50)]

def getBits(n):
    acc = 0
    for i in range(50):
        acc += n//(1<<(i+1)) *(1<<i) + max(0, n %(1<<(i+1)) - (1<<i)+1)
    return acc

class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        
        ret = []
        for f,t,m in queries:
            x = bisect_left(range(10**15),f,key=getBits)
            y = bisect_left(range(10**15),t+1,key=getBits) # 0 indexed ,need to add 1
            c1 = getKBitsArray(x-1)
            cnt1 = sum(c1)
            for i in range(50):
                if x &(1<<i):
                    if cnt1 <f:
                        c1[i] +=1
                        cnt1 +=1
            c2 = getKBitsArray(y)
            cnt2 = sum(c2)
            for i in range(49,-1,-1):
                if y &(1<<i):
                    if cnt2>t+1:
                        c2[i] -=1
                        cnt2 -=1
            c3 = [b-a for (b,a) in zip(c2,c1)]
            acc = 0
            for i,a in enumerate(c3):
                acc += i*a
            #print(acc,c3,c1,c2)
            ret.append(pow(2,acc,m))
        return ret




re =Solution().findProductsOfElements([[2,5,3],[7,7,4]])
print(re)