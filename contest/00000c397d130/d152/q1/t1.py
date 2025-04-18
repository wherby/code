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
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = 0
        st =set()
        for i,a in enumerate(digits):
            for j,b in enumerate(digits):
                for k,c in enumerate(digits):
                    if a >0 and c%2 ==0 and i!=j and i!=k and j!=k:
                        st.add((a,b,c))
        return len(st)






re =Solution()
print(re)