from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf
from collections import Counter
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        c2 = Counter(nums2)
        c1 = Counter(nums1)
        ret = 10**10
        keys1 = list(c1.keys())
        keys1.sort()
        keys2 = list(c2.keys())
        keys2.sort()
        #print(keys1,keys2)
        for i in range(3):
            if len(keys1) >i:
                t = keys2[0]- keys1[i]
                isG = True
                for k in keys2:
                    if c1[k-t] < c2[k]:
                        isG = False
                        break
                #print(t,isG,nums1[i],keys2[0],i,t)
                if isG:
                    ret = min(ret,t)
        return ret


re =Solution().minimumAddedInteger([3,5,5,3],[7,7])
print(re)