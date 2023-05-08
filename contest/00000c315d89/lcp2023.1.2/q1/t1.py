from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        mx= 1 
        acc =1
        n = len(runes)
        for i in range(1,n):
            if runes[i]- runes[i-1]>1:
                acc =1
            else:
                acc +=1 
                mx = max(acc,mx)
        return mx





re =Solution().runeReserve(runes = [1,3,5,4,1,7])
print(re)