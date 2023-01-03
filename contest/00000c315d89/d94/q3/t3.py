from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l,r= uniqueCnt1+uniqueCnt2, (uniqueCnt2+uniqueCnt1)*(divisor1+divisor2)*10
        def verify(mid):
            k1 = mid - (mid // math.lcm(divisor1,divisor2))
            #print(k1,mid)
            return k1 < uniqueCnt1 + uniqueCnt2 or mid -mid //divisor1< uniqueCnt1 or mid -mid //divisor2 < uniqueCnt2
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                l = mid +1
            else:
                r = mid 
        return l





re =Solution().minimizeSet(41,59,6148,1460)
print(re)