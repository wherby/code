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
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ret = []
        n = len(nums)
        for i in range(n-k+1):
            tls = nums[i:i+k]

            c = Counter(tls)
            #print(tls,c)
            tm = []
            for k1,v in c.items():
                tm.append((v,k1))
            tm.sort()
            acc =0
            m = x 
            #print(tm,m)
            while tm and m:
                a,b= tm.pop()
                acc += a*b
                m -= 1 
            #print(acc,ret,c)
            ret.append(acc)
        return ret





re =Solution().findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2)
print(re)