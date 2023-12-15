from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        cnt  =0
        ls =[a for a in word]
        for i in range(1,n):
            if abs(ord(ls[i]) - ord(ls[i-1]))<=1:
                cnt +=1
                ls[i] = 'Z'
        return cnt





re =Solution()
print(re)