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
from collections import defaultdict,deque
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        ls = deque([])
        for a in s:
            if a =="(":
                ls.append(1)
            else:
                ls.append(-1)
        
        def handlemer(ls):
            st = []
            while ls:
                a= ls.popleft()
                if len(st) == 0:
                    st.append(a)
                else:
                    if a *st[-1] <0:
                        if a <=-k and st[-1]>=k:
                            t = a +st[-1]
                            st.pop()
                            if t !=0:
                                ls.appendleft(t)
                        else:
                            st.append(a)
                    else:
                        b = st.pop()
                        t = a+b 
                        ls.appendleft(t)
                #print(st,ls)
            return deque(st)
        m = len(ls)
        willMerge = True
        while willMerge:
            ls = handlemer(ls)
            if len(ls) == m :
                willMerge = False
            m = len(ls)
        ret = []
        for a in ls:
            if a >0:
                ret.append("("*a)
            else:
                ret.append(")"*(-a))
        return "".join(ret)







re =Solution().removeSubstring( s = ")(((()))", k = 2)
print(re)