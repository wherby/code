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
    def longestBalanced(self, s: str) -> int:
        dic = {}
        dic[(0,0,0)] = -1
        cur = [0,0,0]
        mx = 0
        for i,a in enumerate(s):
            t = ord(a) - ord('a')
            if cur[(t+1)%3] > 0 and cur[(t+2)%3] > 0:
                cur[(t+1)%3] -=1
                cur[(t+2)%3] -=1
            else:
                cur[t] +=1
            ct = tuple(cur)
            if ct in dic:
                print(ct,dic[ct],i)
                mx =max(mx,i- dic[ct])
            else:
                dic[ct] = i 
        return mx





re =Solution().longestBalanced("abbac")
print(re)