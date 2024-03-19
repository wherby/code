from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        dic = defaultdict(int)
        for a in s:
            dic[a] +=1
        return dic[c]*(dic[c]+1)//2





re =Solution()
print(re)