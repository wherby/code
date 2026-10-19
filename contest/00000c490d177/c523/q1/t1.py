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

st =set()
a ,b = 0,1
ls = []
while a < 10**9:
    ls.append(a)
    a,b = b, a+b 
n = len(ls)
for i in range(2,n+1):
    st.add(sum(ls[i-2:i+1]))


class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        return n in st





re =Solution().threeFibonacciSum(16)
print(re)