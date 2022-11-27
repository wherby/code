from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        idx = 0
        for a in  s:
            if idx <n and  a == t[idx]:
                idx +=1
        return n -min(idx,n)





re =Solution().appendCharacters(s = "coaching", t = "coding")
print(re)