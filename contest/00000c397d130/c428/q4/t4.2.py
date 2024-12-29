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
from collections import Counter
from itertools import pairwise
class Solution:
    def makeStringGood(self, s: str) -> int:
        c =Counter(s)
        ls = [0]*26
        AtoZ= 'abcdefghijklmnopqrstuvwxyz'
        for i,a in enumerate(AtoZ):
            ls[i] = c[a]
        #print(ls)
        mn = len(s)
        ret = len(s)
        for ts in range(mn,0,-1):
                # rm  add/rm
        
            dp=[[0,0],[0,0]]
            for j in range(26):
                dp2=[[-1,-1],[-1,-1]]
                dp2[0][0] = min(dp[0][0],dp[1][0]) + ls[j]
                dp2[0][1] = ls[j]
                dp2[1][0] =dp[1][0] + max(0,ls[j]-ts,ts -ls[j] -dp[1][1])
                dp2[1][0] =min(dp2[1][0], dp[0][0] + max( 0, ts- dp[0][1] - ls[j],ls[j]-ts))
                dp2[1][1] = max(0,ls[j] -ts)
                dp = dp2
                #print(dp,j)
            ret = min(ret,dp[0][0],dp[1][0])
            #print(dp,ts,mn,ret)
        return ret
        




re =Solution().makeStringGood(s = "gigigjjggjjgg")
print(re)