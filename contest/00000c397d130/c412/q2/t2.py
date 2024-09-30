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
    def countPairs(self, nums: List[int]) -> int:
        sm = 0

        def verify(a,b):
            if a <b:
                a,b = b,a
            astr,bstr =str(a),str(b)
            bstr= "0"*(len(astr) -len(bstr)) + bstr
            if astr == bstr:
                return True
            idx = []
            for i,a in enumerate(astr):
                if a != bstr[i]:
                    idx.append(i)
            if len(idx) == 2 and astr[idx[0]] ==bstr[idx[1]] and astr[idx[1]] == bstr[idx[0]]:
                return True
            return False

        n = len(nums)
        for i,a in enumerate(nums):
            for b in nums[:i]:
                if verify(a,b):
                    sm +=1
        return sm





re =Solution()
print(re)