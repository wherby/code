from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:return 1
        acc = 1 
        tp =4
        idx =1 
        while idx < n:
            acc += tp 
            tp +=4
            idx +=1
        return acc 





re =Solution().coloredCells(4)
print(re)