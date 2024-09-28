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
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bd = set(bannedWords)
        return len([a for a in message if a in bd])>=2





re =Solution()
print(re)