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
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            c = Counter()
            nx = 1
            acc = 0 
            ks = []
            for j in range(i,n):
                c[nums[j]] +=1
                if c[nums[j]] ==1:
                    ks.append(nums[j])
                if j-i +1 == acc +nx:
                    acc =acc+nx 
                    nx +=1
                    vs = list(c.values())
                    if len(set(vs)) == nx-1:
                        tls=[(v,k) for k,v in c.items()]
                        tls.sort()
                        tks = [a[1] for a in tls]
                        if tks == ks:
                            ans+=1
                            #print(i,j)
        return ans




re =Solution().countStaircase([5,8,8,2,2,2])
print(re)