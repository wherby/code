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
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st =[]
        for x in nums:
            cur =x
            while st and st[-1] == cur:
                st.pop()
                cur=cur*2
            
            st.append(cur)
        return st





re =Solution().mergeAdjacent([2,1,1,4])
print(re)