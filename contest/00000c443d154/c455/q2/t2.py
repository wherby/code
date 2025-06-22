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

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        ret = []
        
        n = len(numWays)
        isGood = True
        def dfs():
            nonlocal isGood
            tmp = list(numWays)
            tdp = [0]*(n+1)
            tdp[0] = 1 
            for a in ret:
                for i in range(a,n+1):
                    tdp[i] += tdp[i-a]
            tdp = tdp[1:]
            
            tmp = [(a-b) for a,b in zip(tmp,tdp) ]
            #print(tdp,ret,tmp)
            if any(a < 0 for a in tmp):
                isGood =False
            for i in range(1,n+1):
                if tmp[i-1] ==1:
                    ret.append(i)
                    return True 
            if any(a != 0 for a in tmp):
                isGood =False
            return False
        cnt = 0
        while isGood and dfs():
            cnt +=1
        return ret if isGood else []





re =Solution().findCoins([0,1,0,2,0,3,0,4,0,5])
print(re)