from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
        
        def verify(mid):
            last = -10**10
            for x,x1 in rampart:
                if last > x:
                    return False
                if last + mid<= x:
                    last = x1
                else:
                    last=x1 + mid- (x-last)
            return True
        l,r  =0,10**9
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                l=mid+1
            else:
                r = mid
        return l-1





re =Solution().rampartDefensiveLine(rampart = [[0,3],[4,5],[7,9]])
print(re)