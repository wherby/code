from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def minMaxDifference(self, num: int) -> int:
        ls = [i for i in str(num)]
        def changeToMax(ls):
            tls = list(ls)
            for a in ls:
                if a != '9':
                    tls = [i if i !=a else '9' for i in tls ]
                    break
            return tls
        def changeToMin(ls):
            tls = list(ls)
            tls = [i if i != ls[0] else '0' for i in tls]
            return tls
        #print(changeToMax(ls))
        mx = int("".join(changeToMax(ls)))
        mn = int("".join(changeToMin(ls)))
        return mx-mn
            





re =Solution().minMaxDifference(98)
print(re)