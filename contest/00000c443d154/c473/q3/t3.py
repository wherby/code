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
from itertools import pairwise
class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        pls = [0]
        dic =defaultdict(list)
        for i,a in enumerate(capacity):
            pls.append(pls[-1] + a)
            dic[a].append(i)
        cnt = 0
        for k,v in dic.items():
            if len(v) <2:
                continue
            c = defaultdict(int)
            for i,idx in enumerate(dic[k]):
                b = pls[idx+1]- k*2
                cnt += c[b]
                c[pls[idx+1]] +=1
            if k == 0:
                for a,b in pairwise(dic[k]):
                    if a+1 ==b:
                        cnt -=1
            #print(k,cnt,c,dic[k])
        return cnt
        




re =Solution().countStableSubarrays([-4,4,0,0,-8,-4])
print(re)