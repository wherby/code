from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        mx = 0 
        value =0
        cnt =0
        for i,a in enumerate(forts):
            if a == -1 or a == 1:
                if value*a <0:
                    mx = max(mx,cnt)
                cnt =0 
                value = a 
            else:
                cnt +=1
        return mx



re =Solution().captureForts([1,0,0,-1,0,0,0,0,1])
print(re)