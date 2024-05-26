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
    def compressedString(self, word: str) -> str:
        ret =""
        state =0
        pre = ""
        for a in word:
            if a != pre:
                if state !=0:
                    ret += str(state) + pre
                pre = a
                state = 1 
            else:
                state +=1
                if state == 9:
                    ret += str(state) + pre
                    pre = ""
                    state =0
        if state !=0:
            ret += str(state) + pre
        return ret





re =Solution()
print(re)