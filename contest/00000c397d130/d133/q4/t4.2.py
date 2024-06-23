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
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10**9+7
        requirements.sort()
        rd ={}
        for a,b in requirements:
            rd[a] = b
        dp =defaultdict(int)
        mxk= 0
        dp[0] =1 
        for i in range(n):
            dp2 = defaultdict(int)
            acc=0
            for j in range(mxk + i+1):
                acc += dp[j]
                if j > i:
                    acc-= dp[j-i-1]
                dp2[j] = acc%mod
            mxk= mxk+i
            
            if i in rd:
                #mxk = rd[i]
                #print(dp2,rd[i])
                for k in dp2.keys():
                    if k != rd[i]:
                        dp2[k] = 0
            dp= dp2
            #print(dp,i)
        return dp[requirements[-1][1]]%mod 



re =Solution().numberOfPermutations(n = 5, requirements =[[0,0],[1,0],[4,6],[3,4]])
print(re)