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
    def maximumWidth(self, planks: list[int]) -> int:
        n = len(planks)
        planks.sort()
        cand = set(planks)
        for i in range(n):
            for j in range(i):
                cand.add(planks[i] + planks[j])
        ret = 0 
        
        for h in cand:
            l =0 
            r = n-1
            cur = 0
            while l <=r:
                if planks[l]>h:
                    break
                if l ==r:
                    if planks[l] == h:
                        cur +=1
                    break
                curS = planks[l] + planks[r]
                if planks[r] ==h:
                    cur +=1
                    r -=1
                elif planks[l] ==h:
                    cur +=1
                    l +=1
                elif curS ==h:
                    cur +=1
                    r -=1 
                    l +=1
                elif curS < h :
                    l +=1
                else :
                    r -=1
            ret = max(ret,cur )
        return ret
                    
            
        





re =Solution().maximumWidth(planks = [1,3,2,5,7,5,4,2,1]
)
print(re)