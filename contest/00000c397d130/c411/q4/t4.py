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
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        dic = defaultdict(int)
        res = [n-i for i in range(n)]
        l = 0 
        for i,a in enumerate(s):
            dic[a] +=1
            while dic["0"] > k and dic["1"]>k:
                res[l]=i-1
                dic[s[l]] -=1
                l +=1
        print(res)
        pre = [0]
        for a in res:
            pre.append(a+pre[-1])
        ret = []
        for a,b in queries:
            ret.append(pre[b+1]-pre[a])
        return ret




re =Solution().countKConstraintSubstrings(s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]])
print(re)