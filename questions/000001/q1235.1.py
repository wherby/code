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
        sds = list(set(endTime +startTime))
        sds.sort()
        dic = {}
        for i,a in enumerate(sds,1):
            dic[a] = i 
        dic[0] =1
        n = len(sds)
        dp = [0]*(n+1)
        dic2 = defaultdict(list)
        for e,s,p in ls:
            dic2[dic[e]].append((dic[s],p))
        #print(sds)
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for s,p in dic2[i]:
                dp[i] = max(dp[i], dp[s] + p)
        #print(dp)
        return dp[-1]

re =Solution().jobScheduling([33,8,9,18,16,36,18,4,42,45,29,43],[40,16,32,39,46,43,28,13,44,46,39,44],[2,6,5,14,5,19,5,12,19,14,14,17])

print(re)