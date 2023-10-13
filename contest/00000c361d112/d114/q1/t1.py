from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        dic ={}
        for i,a in enumerate(nums[::-1]):
            dic[a] = 1
            isG = True
            for j in range(1,k+1):
                if j not in dic:
                    isG = False
            if isG:
                return i +1





re =Solution()
print(re)