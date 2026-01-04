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
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        diff = 0
        s1 = t1 =0
        for a,b in zip(s,t):
            if a !=b:
                diff +=1 
                if a =="1":
                    s1 +=1
                if b == "1":
                    t1 +=1
        cost = 0 
        if diff %2 ==1:
            diff -=1 
            cost += flipCost
        k =abs(s1-t1)//2 
        if flipCost*2 <= crossCost+swapCost:
            cost += k*2 *flipCost
            diff -= k*2 
        else:
            cost += (crossCost +swapCost)*k
            diff -= k*2
        if flipCost *2 <= swapCost:
            cost += diff *flipCost
        else:
            cost += diff//2*swapCost
        return cost 




re =Solution().minimumCost(s = "0", t = "1", flipCost = 4, swapCost = 2, crossCost = 2)
print(re)