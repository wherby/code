from tkinter import N
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1]*n
        sl = SortedList()
        cnt =[0]*n 
        for i,a in enumerate(nums):
            k = sl.bisect_left((a,0))
            for j in range(k-1,-1,-1):
                v,idx = sl[j]
                cnt[idx] +=1
                if cnt[idx] ==2:
                    ret[idx] = a 
                    sl.remove((v,idx))
            sl.add((a,i))
        return ret





re =Solution().secondGreaterElement([2,4,0,9,6])
print(re)