from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ls = sorted([(e,s,p) for s,e,p in zip(startTime,endTime,profit)])
        n = len(ls)
        dp=[0]*(n+1)
        
        for i,(e,s,p) in enumerate(ls):
            k = bisect_left(ls,(s+1,0,0))
            dp[i+1] = max(dp[i],dp[k] + p)
        return dp[-1]
re =Solution().jobScheduling([33,8,9,18,16,36,18,4,42,45,29,43],[40,16,32,39,46,43,28,13,44,46,39,44],[2,6,5,14,5,19,5,12,19,14,14,17])

print(re)