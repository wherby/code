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
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = [10**10] * (sum+1)
        dp[0] = 0 
        for a in nums:
            dic = {}
            cur = a 
            cst = 0 
            
            dic[a] = cst 
            while cur*2 <=sum:
                cur =cur*2
                cst +=1
                dic[cur] = cst 
            cur = a 
            cst = 0
            while cur //2 >0:
                cur =cur //2 
                cst +=1
                dic[cur] =cst 
            ndp =list(dp)
            for k,v in dic.items():
                for f in range(sum, k-1,-1):
                    if dp[f-k] <10**10:
                        ndp[f] = min(ndp[f],dp[f-k]+v)
            dp =ndp 
        return -1 if dp[sum] ==10**10 else dp[sum]
        
        




re =Solution()
print(re)