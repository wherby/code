from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        acc = 0
        dic=defaultdict(int)
        dic[0]=1
        cnt =0
        for a in nums:
            acc= acc ^a 
            t = dic[acc]
            cnt += t
            dic[acc]+=1
        return cnt





re =Solution().beautifulSubarrays([4,3,1,2,4])
print(re)