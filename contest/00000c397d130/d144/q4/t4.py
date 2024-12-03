#OT
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
        def dfs(i,a,b):
            if a <0 or b<0:
                return -10**10
            if i == n-1:
                if a ==0 and b == 0:
                    return 0
                return -10**19
            ret = -10**10
            if (i,n-1-a) != (n-1-b,i):
                t= fs[i][n-1-a] + fs[n-1-b][i]
                for i1 in range(-1,2):
                    for j1 in range(-1,2):
                        ret= max(ret,dfs(i+1,a+i1,b+j1) +t)
            else:
                t= fs[i][n-1-a]
                for i1 in range(-1,2):
                    for j1 in range(-1,2):
                        ret= max(ret,dfs(i+1,a+i1,b+j1) +t)
            return ret
        return dfs(0,0,0)+sm



re =Solution().maxCollectedFruits(fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]])
print(re)