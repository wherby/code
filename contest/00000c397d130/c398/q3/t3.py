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
class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        m = len(str(nums[0]))
        n = len(nums)
        for i in range(m):
            c = Counter()
            for a in nums:
                c[str(a)[i:i+1]]+=1
            for _,v in c.items():
                ret += (n-v)*v
        return ret//2




re =Solution().sumDigitDifferences(nums = [13,23,12])
print(re)