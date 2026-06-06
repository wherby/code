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
    def maximumMEX(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        cur = 0
        res = []
        n = len(nums)
        while cur <n:
            cur_mex = 0 
            while c[cur_mex] >0:
                cur_mex +=1
            if cur_mex ==0 :
                return res + [0]*(n-cur +1)
            st = set()
            while cur < n:
                a= nums[cur]
                c[a] -=1
                if a < cur_mex:
                    st.add(a)
                cur +=1
                if len(st) == cur_mex:
                    break
            res.append(cur_mex)
        return res





re =Solution()
print(re)