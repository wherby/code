from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        dic = defaultdict(int)
        n = len(word)
        for i in range(0,n,k):
            s1 = word[i:i+k]
            dic[s1] +=1
        return n//k - max(dic.values())





re =Solution()
print(re)