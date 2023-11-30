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
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        re =[i for i,a in enumerate(words) if a.find(x)>=0]





re =Solution()
print(re)