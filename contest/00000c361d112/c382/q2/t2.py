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
    def maximumLength(self, nums: List[int]) -> int:
        c=Counter(nums)
        keys = list(c.keys())
        
        ret = 1
        for k in keys:
            if k == 1:
                ret = max(ret,(c[1]-1)//2*2+1)
                continue
            #print(k)
            acc =1
            cur =k
            while int(math.sqrt(cur))**2 == cur and c[int(math.sqrt(cur))]>=2:
                acc +=2
                cur  = math.sqrt(cur)
            ret = max(ret,acc)
        return ret 






re =Solution().maximumLength([5,4,1,2,2])
print(re)