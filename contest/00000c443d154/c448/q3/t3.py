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
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:

        def dfs(n,k,position,time):
            sm = 0
            for i in range(n-1):
                sm += time[i]*(position[i+1] -position[i])
            if k ==0:
                return sm
            st = []
            for i in range(1,n-2):
                delta = (position[i+1] - position[i]) * (time[i-1] - time[i]) + (position[i+2] - position[i+1]) * time[i]
                heapq.heappush(st, (delta, i))
            if n - 2 >= 1:
                i = n - 2
                delta = (position[i+1] - position[i]) * (time[i-1] - time[i])
                heapq.heappush(st, (delta, i))
            #print(k,st)
            mn = st[0][0]
            ret = 10**30
            while st and st[0][0]==mn:
                delta,i = heapq.heappop(st)
                newP = position[:i] + position[i+1:]
                newTime = time[:i] + [time[i] + time[i+1]] + time[i+2:]
                #print(newP,newTime)
                ret= min(ret, dfs(n-1,k-1,newP,newTime))
            return ret
        return dfs(n,k,position,time)





#re =Solution().minTravelTime(l = 5, n = 5, k = 1, position = [0,1,2,3,5], time = [8,3,9,3,3])
re =Solution().minTravelTime(l = 5, n = 5, k = 2, position = [0,2,3,4,5], time =[1,1,3,2,1])
print(re)
