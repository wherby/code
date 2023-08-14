from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        ret = -1
        n = len(nums)
        c  = Counter(nums)
        mx = 0
        cc =0
        for k,v in c.items():
            if v > mx:
                mx =v 
                cc =k 
        ls = [0]*n 
        for i,a in enumerate(nums):
            ls[i] = ls[i-1]+ (a == cc)
            if ls[i] *2 > i+1 and (mx-ls[i])*2 > n - i -1:
                return i 
        return ret
        





re =Solution().minimumIndex(nums = [1,2,2,2])
print(re)