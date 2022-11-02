from email.policy import default
from typing import DefaultDict, List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        ls = defaultdict(int)
        mxv = defaultdict(int)
        for i,a in enumerate(nums):
            b = a%space
            ls[b] += 1
            mxv[b] = min(mxv.get(b,10**10),a)
        ret = 10**10
        mx = 0
        #print(dic)
        for i in ls.keys():
            if ls[i] > mx:
                mx = ls[i]
                ret = mxv[i]
            if ls[i] == mx:
                ret = min(mxv.get(i,10**10),ret)
        
        return ret
            



re =Solution().destroyTargets(nums = [1,3,5,2,4,6], space = 2)
print(re)