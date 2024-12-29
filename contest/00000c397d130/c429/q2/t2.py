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
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        visit={}
        startP= -k + nums[0]
        for a in nums:
            for j in range(max(startP,a-k),k+1+a):
                if j not in visit:
                    visit[j] =a
                    startP =j+1
                    break
                else:
                    startP = j+1
        #print(visit)
                
                    

        return len(visit.keys())





re =Solution().maxDistinctElements([8]*10000 + [7]*10000 ,1000)
print(re)