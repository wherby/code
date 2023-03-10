from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def splitNum(self, num: int) -> int:
        ls = [int(i) for i in str(num)]
        ls.sort()
        a,b =0,0
        for i,c in enumerate(ls):
            if i%2 ==0:
                a=a*10+c 
            else:
                b = b*10+c 
        return a+b





re =Solution().splitNum(4325)
print(re)