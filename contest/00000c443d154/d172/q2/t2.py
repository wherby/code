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
import itertools
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ret = 0
        dic = defaultdict(list)
        for a in nums:
            dic[a%3].append(a)
        cand =[]
        for k,vs in dic.items():
            vs.sort(reverse= True)
            cand.extend(vs[:3])
        for a,b,c in itertools.combinations(cand,3):
            d = a+b+c 
            if d%3 ==0:
                ret = max(ret,d)
        return ret




re =Solution().maximumSum([4,3,2,1])
print(re)