from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def toInt(st):
            ls = st.split(":")
            return int(ls[0]) *60+ int(ls[1])
        s1,e1 = toInt(event1[0]),toInt(event1[1])
        s2,e2 = toInt(event2[0]),toInt(event2[1])
        for i in range(s1,e1+1):
            for j in range(s2,e2+1):
                if i==j:
                    return True
        return False





re =Solution().haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"])
print(re)