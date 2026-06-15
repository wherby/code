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
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        n = len(nums)

        maxN = max(max(nums),maxVal)+1
        cnt = [0]*maxN
        for x in nums:
            cnt[x]+=1
        
        fcnt = [0]*maxN
        
        pls = [True]*maxN
        for i in range(2,maxN):
            if pls[i]:
                acc =0
                for j in range(i,maxN,i):
                    acc+= cnt[j]
                    pls[i] = False
                for j in range(i,maxN,i):
                    fcnt[j] = max(fcnt[j],acc)
        #print(fcnt)
        ans = -n 

        for i in range(1,maxN):
            if cnt[i]>=1:
                ans = max(ans,i-max(fcnt[i],cnt[i]) +1)
            else:
                if i <= maxVal:
                    ans = max(ans,i-1)
            print(i,ans,cnt,fcnt)
        return ans




re =Solution().maxScore( nums =[3,4,6], maxVal = 5)
print(re)