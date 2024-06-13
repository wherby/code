from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def modifiedMatrix(self, mx: List[List[int]]) -> List[List[int]]:
        mls = list([max(a) for a in zip(*mx)])
        m,n = len(mx),len(mx[0])
        for i in range(m):
            for j in range(n):
                if mx[i][j] == -1:
                    mx[i][j] = mls[j]
        return mx





re =Solution().modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]])
print(re)