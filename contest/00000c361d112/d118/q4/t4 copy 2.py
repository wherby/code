from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        pls =[0]
        for a in nums:
            pls.append(pls[-1] +a)
        n = len(nums)
        dp=[0]*(n+1)
        st = [(0,0,0)]
        for i in range(n):
            for a,b,c in st:
                if a +c <=pls[i+1]:
                    while st and st[-1][2]==pls[i+1] and st[-1][1]<=b+1   and st[-1][0]> pls[i+1]-c:
                        st.pop()
                    st.append((pls[i+1]-c,b+1,pls[i+1]))
            #print(st)
        mx = 0
        for a,b,c in st:
            mx = max(mx,b)
        return mx





re =Solution().findMaximumLength([546,575,247,650,178,752,356,318,131,438])
print(re)