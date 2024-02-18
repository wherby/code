from typing import List, Tuple, Optional

from collections import defaultdict,deque
#from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        dic = defaultdict(int)
        for a in arr1:
            while a >0:
                dic[a] =len(str(a))
                a = a //10 
        mx = 0 
        for b in arr2:
            while b >0:
                if b in dic:
                    mx = max(mx,dic[b])
                b = b //10 
        return mx





re =Solution().longestCommonPrefix([16],[17])
print(re)