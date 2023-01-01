from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l,r = 0,price[-1]-price[0]
        n = len(price)
        def verify(mid):
            start=price[0]
            for _ in range(k-1):
                t =bisect_left(price,start+mid)
                if t == n:
                    return False
                start = price[t]
            return True
        while l<r:
            mid = (l+r+1)>>1
            if verify(mid):
                l=mid
            else:
                r = mid-1
        return l 





re =Solution().maximumTastiness([1,1,1,1],2)
print(re)