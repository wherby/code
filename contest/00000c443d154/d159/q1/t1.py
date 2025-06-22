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
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        odd = len([a for a in nums if a%2 ==1])
        even = len([a for a in nums if a%2 ==0])
        if abs(odd -even)>1:
            return -1
        ods = [i for i in range(0,n,2)]
        
        def getDiss(ls1,ls2):
            acc = sum(abs(a-b) for a,b in zip(ls1,ls2))
            return acc
        lso,lse = [i for i,a in enumerate(nums) if a %2 ==1],[i for i,a in enumerate(nums) if a %2 ==0] 
        if odd > even:
            return getDiss(ods,lso)
        if even > odd:
            return getDiss(ods,lse)
        return min(getDiss(ods,lse),getDiss(ods,lso))
            
        





re =Solution().minSwaps([2,4,6,5,7])
print(re)