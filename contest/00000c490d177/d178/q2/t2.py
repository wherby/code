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
    def gcdSum(self, nums: list[int]) -> int:
        ls = []
        mx =0
        for a in nums:
            mx = max(mx,a)
            ls.append(math.gcd(a,mx))
        ls.sort()
        ans = 0 
        for i in range(len(ls)//2):
            ans += math.gcd(ls[i],ls[len(ls)-1-i])
        return ans





re =Solution()
print(re)