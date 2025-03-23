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
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        mx = max(skill)
        sks = sum(skill)
        n = len(skill)
        ps =[0]
        for a in skill:
            ps.append(a + ps[-1])
        k = skill.index(mx)
        start =lst =klst = lsta=0
        for m in mana:
            #print(m,klst, lst,lst-m*(sks-skill[-1]))
            start =max(klst-m*ps[k],lst-m*(sks-skill[-1]),0,lsta)
            
            lst =start + m* sks
            klst = start + ps[k+1]*m
            lsta = start + m*ps[1]
            print(start,klst)
        return lst





#re =Solution().minTime( skill = [1,5,2,4], mana = [5,1,4,2])
#re =Solution().minTime( skill = [1,2,3,4], mana = [1,2])
re =Solution().minTime( skill = [1,3,4], mana = [2,3,3,3])
print(re)