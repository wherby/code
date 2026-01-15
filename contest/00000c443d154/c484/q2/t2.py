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
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            dic = defaultdict(int)
            acc = 0 
            for j in range(i,n):
                acc += nums[j]
                dic[nums[j]] +=1
                if acc in dic:
                    cnt +=1
        return cnt



re =Solution().centeredSubarrays([-1,1,0])
print(re)