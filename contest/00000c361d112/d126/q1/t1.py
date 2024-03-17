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
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            mx =max(int(a) for a in str(num))
            ret +=int(str(mx)*len(str(num)))
        return ret





re =Solution().sumOfEncryptedInt([10,21,31])
print(re)