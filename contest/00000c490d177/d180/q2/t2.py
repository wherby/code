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
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        cnt = 0 
        for a in nums:
            for b in str(a):
                if b == str(digit):
                    cnt+=1
        return cnt





re =Solution()
print(re)