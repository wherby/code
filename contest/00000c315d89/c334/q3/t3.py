from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        sl =SortedList([])
        for i in nums:
            sl.add(i)
        idx = 0
        cnt =0
        while idx < len(sl):
            n = len(sl)
            a = sl[idx]
            k = sl.bisect_left(a*2)
            if k <n//2:
                k = n//2
            if k < n:
                b = sl[k]
                sl.remove(a)
                sl.remove(b)
                cnt +=2
            else:
                idx +=1
        return cnt
        
        





re =Solution().maxNumOfMarkedIndices( [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40])
print(re)