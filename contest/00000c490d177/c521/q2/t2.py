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
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        n = len(nums)
        base = 0
        cnt = Counter()
        
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            if a == b:
                base += 1
            else:
                cnt[(a, b)] += 1
                cnt[(b, a)] += 1
                
        max_gain = max(cnt.values()) if cnt else 0
        
        return base + max_gain





re =Solution()
print(re)