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
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        ops =[]
        for p,s in zip(position,speed):
            while len(ops)>0 and  p- ops[-1][0]<=distance:
                ops.pop()
            ops.append((p,s))
        st = []
        for _,a in ops:
            while len(st)>0 and a < st[-1]:
                st.pop()
            st.append(a)
        print(st)
        return len(st)



re =Solution().countGroups(position = [677,711,942,960], speed = [774,951,743,516], distance = 27)
print(re)