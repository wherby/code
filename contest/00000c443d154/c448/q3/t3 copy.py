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
        
        @cache
        def dfs(k,idx,lst):
            ret = 10**10
            if idx >=n:
                return ret
            #print(idx,k)
            if k==0 and idx ==n-1:
                return 0 
            
            for i in range(k+1):
                if i+idx+1 >=n:continue
                t = dfs(k-i,idx+1+i,sum(time[idx+1:idx+2+i])) + lst*(position[i+idx+1] - position[idx])
                ret = min(ret,t)
            return ret
        return dfs(k,0,time[0])



re =Solution().minTravelTime(l = 5, n = 5, k = 1, position = [0,1,2,3,5], time = [8,3,9,3,3])
#re =Solution().minTravelTime(l = 5, n = 5, k = 2, position = [0,2,3,4,5], time =[1,1,3,2,1])
print(re)
