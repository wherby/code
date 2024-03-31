from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minOperations(self, k: int) -> int:
        ls =1 
        cnt =1
        ret =0
        while ls*cnt <k:
            if ls <= cnt:
                ls +=1
                ret +=1
            else:
                cnt +=1
                ret +=1
        return ret




re =Solution()
print(re)