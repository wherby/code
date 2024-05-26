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
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        dic =defaultdict(int)
        for a in nums1:
            dic[a] +=1
        c = Counter(nums2)
        mx = max(nums1)
        ret = 0
        for k1,v in c.items():
            k2 = k1*k
            for j in range(k2,mx+1,k2):
                ret += v*dic[j]
        return ret




re =Solution().numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1)
print(re)