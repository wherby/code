from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ret =[]

        st  =[]

        def dfs(i,res,is1):
            if i == n:
                ret.append("".join(st))
                return
            st.append("0")
            dfs(i+1,res,False)
            st.pop()
            if is1 == False and i<=res:
                st.append("1")
                dfs(i+1,res-i,True)
                st.pop()
        dfs(0,k,False)
        return ret





re =Solution().generateValidStrings(3,1)
print(re)