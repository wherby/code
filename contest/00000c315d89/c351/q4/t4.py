from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ls = []
        n = len(positions)
        for i in range(n):
            ls.append((positions[i],healths[i],directions[i],i))
        ls.sort()
        ret =[]
        st = []
        for i in range(n):
            p,h,d,idx =ls[i]
            if d == "L":
                if len(st) ==0:
                    ret.append((idx,h))
                else:
                    while st:
                        if st[-1][1]<h:
                            h-=1
                            st.pop()
                        elif st[-1][1]==h:
                            st.pop()
                            h=0
                            break
                        else:
                            p1,h1,d1,idx1 = st.pop()
                            st.append((p1,h1-1,d1,idx1))
                            break
                    if len(st) ==0 and h !=0:
                        ret.append((idx,h))
            else:
                st.append((p,h,d,idx))
        for p,h,d,idx in st:
            ret.append((idx,h))
        ret.sort()
        res =[]
        for _,h in ret:
            res.append(h)
        return res

        
        





re =Solution().survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL")
print(re)