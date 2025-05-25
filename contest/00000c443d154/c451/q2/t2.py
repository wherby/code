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
    def resultingString(self, s: str) -> str:
        st =[]
        for a in s:
            st.append(a)
            while len(st) >=2 and (abs(ord(st[-1]) -ord(st[-2])) ==1 or abs(ord(st[-1]) -ord(st[-2])) ==25) :
                st.pop()
                st.pop()
        return "".join(st)





re =Solution()
print(re)