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
from collections import Counter
class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        c = Counter(s)
        st = []

        for a in s:
            while st and a <st[-1] and c[st[-1]]>1:
                d = st.pop()
                c[d] -=1
            st.append(a)
        while st and c[st[-1]]>1:
            d=st.pop()
            c[d] -=1
        return "".join(st)





re =Solution().lexSmallestAfterDeletion("aabcdfdbcbk")
print(re)