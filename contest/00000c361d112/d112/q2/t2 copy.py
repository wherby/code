from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2] ) == Counter(s2[::2]) and Counter(s1[1::2]) ==Counter(s2[1::2])
        




re =Solution().checkStrings(s1 = "abe", s2 = "bea")
print(re)