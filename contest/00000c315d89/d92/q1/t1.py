from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n ==1:return 0
        cnt =n 
        ls = []
        for i in range(n):
            ls.append(720/n *i)
        for i in range(n//2):
            k = bisect_left(ls,(720/n)*i + 360-0.001)
            if abs(ls[k] - ls[i]-360)<0.01:
                cnt -=1
        return cnt 





re =Solution().numberOfCuts(6)
print(re)