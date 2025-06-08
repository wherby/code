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
    def maximumProfit(self, prices: List[int], k: int) -> int:
        state = -1 
        n = len(prices)
        st = [prices[0]]
        for i in range(1,n):
            if prices[i]>st[-1]:
                if state ==1:
                    st.pop()
                state = 1
                st.append(prices[i])
            elif prices[i]< st[-1]:
                






re =Solution()
print(re)