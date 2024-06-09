from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        ls= [0]*4
        state =0
        for a in nums:
            if a ==1:
                if state == 0:
                    state +=1
                elif state ==1:
                    state +=1
                elif state ==2:
                    ls[3] +=1
                    state = 0
            else:
                ls[state] +=1
                state =0
        c = sum(ls[1:])
        k-= min(c,maxChanges)
        lss = []
        lss =  [2]*ls[3] + [1]*ls[2]
        lss = lss[:maxChanges] 
        cnt =0
        m = sum(lss[:maxChanges])
        m1 = min(m,k)
        k -= m1 
        cnt += m1 
        cnt += 2*k
        return cnt





re =Solution().minimumMoves([1,0,1,0,1],3,0)
print(re)