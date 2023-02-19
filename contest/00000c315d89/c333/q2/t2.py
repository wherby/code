from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minOperations(self, n: int) -> int:
        clen =len(bin(n))-2
        ls = bin(n)[2:] 
        for i in range(clen-1,0,-1):
            if ls[i]==ls[i-1] =="1":
                return 1+self.minOperations(n + (1<<(clen-i-1)))
        a = bin(n).count("1")
        return a





re =Solution().minOperations(54)
print(re)