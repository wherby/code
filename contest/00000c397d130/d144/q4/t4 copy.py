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
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        sm = 0
        fs =fruits
        n = len(fs)
        for i in range(n):
            sm+= fs[i][i]
            fs[i][i] =0
        
        @cache
        def dfs(i,a,j):
            if a <0 :
                return -10**10
            if i == n-1:
                if a ==0 :
                    return 0
                return -10**19
            ret = -10**10
            for i1 in range(-1,2):
                if j ==0:
                    t=fs[i][n-1-a]
                else:
                    t = fs[n-1-a][i]
                ret=max(ret,dfs(i+1,a+i1,j)+t) 
            return ret
        #print(dfs(0,0,0),dfs(0,0,1))
        return dfs(0,0,1) +dfs(0,0,0)+sm



re =Solution().maxCollectedFruits(fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]])
print(re)