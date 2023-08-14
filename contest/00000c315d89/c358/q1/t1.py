from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx =-1
        dic ={}
        for a in nums:
            b = max([int(c) for c in str(a)])
            if b not in dic:
                dic[b] = a 
            else:
                mx = max(mx,a+dic[b])
                dic[b]= max(a,dic[b])
        return mx





re =Solution()
print(re)