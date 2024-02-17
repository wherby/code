from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        msk = (1<<30) -1 
        cur = 0
        ans = 0
        n = len(nums)
        for i in range(29,-1,-1):
            cur = ans | (1<<i)
            cc = cur
            cnt = 0
            for a in nums:
                cc = cc&a 
                if cc ==0:
                    cnt +=1
                    cc = cur 
            if cnt >=n- k:
                ans = cur
            #print(ans,cnt)
        return msk - ans




re =Solution().minOrAfterOperations(nums = [37,6,46,32,23],k=3)
re =Solution().minOrAfterOperations([7,3,15,14,2,8] ,4)
print(re)