from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        ls = [int(i) for i in str(n)]
        if sum(ls)<= target:
            return 0 
        m = len(ls)
        j =0
        tn =n 
        idx =0
        while  n > 0:
            idx +=1
            n= n //10 +1
            ls = [int(i) for i in str(n)]
            if sum(ls)<= target:
                return 10**(idx) - tn%(10**idx)
            



re =Solution().makeIntegerBeautiful(n = 1, target = 1)
print(re)