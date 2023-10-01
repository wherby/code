from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        n = len(nums)
        res = target%sm
        ls = nums + nums
        dic ={}
        dic[0]= -1
        acc =0
        k =10**10
        if res ==0:
            return  n* (target//sm)
        for i,a in enumerate(ls):
            acc +=a
            if acc-res in dic:
                k = min(k,i-dic[acc-res])
            dic[acc] = i
        return k + n* (target//sm) if k != 10**10 else -1





re =Solution().minSizeSubarray([1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6],56)
print(re)