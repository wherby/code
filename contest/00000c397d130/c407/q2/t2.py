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
    def doesAliceWin(self, s: str) -> bool:
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        cnt = len([a  for a in s if a in vowls])
        #print(cnt)
        return cnt >0




re =Solution().doesAliceWin("ifld")
print(re)