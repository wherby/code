from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from collections import Counter
import math

mod  = 10**9+7

class Solution:
    def countAnagrams(self, s: str) -> int:
        mod  = 10**9+7
        ls = s.split(" ")
        acc =1 

        #print(len(ls))
        for a in ls:
            n = len(a)
            c = Counter(a)
            for i,n1 in c.items():
                acc = acc* math.comb(n,n1) %mod
                n = n-n1
        return acc


re =Solution().countAnagrams( "a"*50000+"b"*20000+"c"*20000+"d"*20000)
print(re)