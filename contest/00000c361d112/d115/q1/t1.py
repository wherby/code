from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        st =[]
        idx = 0
        ret =[]
        for a in words:
            if a == "prev":
                if idx==0:
                    ret.append(-1)
                else:
                    idx -=1
                    ret.append(st[idx])
            else:
                st.append(int(a))
                idx = len(st)
        return ret





re =Solution()
print(re)