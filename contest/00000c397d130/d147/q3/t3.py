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
    def longestSubsequence(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        ret =0
        for a in nums:

            acc =0
            for j in range(300,-1,-1):
                if a +j <=300:
                    acc = max(acc,dp[(a+j,j)])
                if a -j >=1:
                    acc = max(acc,dp[(a-j,j)])
                dp[(a,j)] = max( acc+1,dp[(a,j)])

            ret = max(ret, max(dp.values()))
            
        return ret

re =Solution().longestSubsequence([6,5,3,4,2,1])
print(re)
            