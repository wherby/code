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
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        N  = max(max(groups),max(elements)) +2
        ls = [-1]*(N+2)
        visit ={}
        for i,a in enumerate(elements):
            if a in visit:continue
            visit[a] =1
            for j in range(a,N+1,a):
                if ls[j] == -1:
                    ls[j] = i 
        ret = []
        for a in groups:
            ret.append(ls[a])
        return ret 





re =Solution().assignElements(groups = [8,4,3,2,4], elements = [4,2])
print(re)