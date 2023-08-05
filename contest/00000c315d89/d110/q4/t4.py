from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        l,r =1,n
        ls2 = [(nums2[i],i) for i in range(n)]
        ls2.sort()
        def verify(mid):
            cnt =0
            ret = []
            for i in range(n):
                ret.append((nums1[i] + mid*nums2[i],i))
            ret.sort()
            for i in range(n-mid):
                cnt += ret[i][0]
            ls1 = []
            for i in range(n-mid,n):
                ls1.append(nums2[ret[i][1]])
            ls1.sort(reverse=True)
            for i in range(mid):
                cnt += ls1[i]*i
            return cnt <=x
        for i in range(0,n+1):
            if verify(i):
                return i 
        return -1
        





re =Solution().minimumTime([1,7,6,2,9],[4,2,3,3,0],23)
print(re)