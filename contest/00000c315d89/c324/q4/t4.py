from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def getCnt(a,b):
            if len(bin(a)) > len(bin(b)):
                return 1 + getCnt(a//2,b)
            elif len(bin(a)) < len(bin(b)):
                return 1 + getCnt(a,b//2)
            else:
                if a ==b :
                    return 0
                else:
                    return 2+ getCnt(a//2 ,b//2)
        ret =[]
        for a,b in queries:
            ret.append(getCnt(a,b)+1)
        return ret
        



re =Solution().cycleLengthQueries(n = 3, queries = [[5,3],[4,7],[2,3]])
print(re)