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
    def countCoprime(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        dp = [0]*151
        for i in range(n):
            dp[mat[0][i]] +=1
        mod = 10**9+7
        for i in range(1,m):
            ndp = [0]*151
            for a in mat[i]:
                for k,d in enumerate(dp[1:],1):
                    c = math.gcd(k,a)
                    ndp[c] +=d
                    ndp[c] %=mod 
            dp = ndp
        return dp[1]






re =Solution().countCoprime([[1,2],[3,4]])
print(re)