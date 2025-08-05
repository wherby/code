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

from itertools import pairwise
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        def isInc(ls):
            for a,b in pairwise(ls):
                if b <=a:
                    return False
            return True
        n = len(nums)
        for i in range(1,n-1):
            for j in range(i+1,n-1):
                #print(i,j,isInc(nums[:i+1]) , isInc(nums[i:j][::-1]) , isInc(nums[j:]),nums[:i+1],nums[j:])
                if isInc(nums[:i+1]) and isInc(nums[i:j+1][::-1]) and isInc(nums[j:]):
                    return True
        return False





re =Solution().isTrionic([1,4,8,9])
print(re)