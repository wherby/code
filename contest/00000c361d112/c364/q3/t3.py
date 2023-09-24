from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maximumSumOfHeights(self, hs: List[int]) -> int:
        
        n = len(hs)
        
        def getLS(hs):
            ls = []
            st =[]
            for i,a in enumerate(hs):
                while st and a <hs[st[-1][0]]:
                    st.pop()
                if st:
                    st.append((i,st[-1][1] +a*(i-st[-1][0])))
                else:
                    st.append((i,a*(i+1)))
                ls.append(st[-1][1])
                #print(st,a)
            #print(ls)
            return ls
        left = getLS(hs)
        right =getLS(hs[::-1])[::-1]
        mx = 0
        for i in range(n):
            tp = left[i] + right[i] - hs[i]
            mx = max(tp,mx)
        return mx
        
        




re =Solution().maximumSumOfHeights([2,4,1,3,5])
print(re)