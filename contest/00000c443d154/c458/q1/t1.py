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
    def processStr(self, s: str) -> str:
        st =[]
        for a in s:
            if a.isalpha():
                st.append(a)
            elif a == "*":
                if len(st):
                    st.pop()
            elif a == "#":
                st = st +st 
            elif a =="%":
                st = st[::-1]
        return "".join(st)




a = "jio"+"#"+"*g"
re =Solution().processStr(a)
print(re)