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
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        acc =rewardValues[-1]
        ls = rewardValues[:-1]
        ls = set(ls)
        ls = list(ls)
        ls.sort()
        sl = SortedList([i for i in range(1,acc)])
        dic= {}
        dic[0] =1
        for a in ls:
            l = sl.bisect_left(a)
            r = min(sl.bisect_left(a*2-1),len(sl)-1)
            rm =[]
            for i in range(l, r+1):
                if sl[i] -a in dic and sl[i]-a <a:
                    rm.append(sl[i])
            for a in rm:
                sl.remove(a)
                dic[a] =1
            #print(a,dic)
            print(sl,dic)
        for i in range(acc-1,-1,-1):
            if i in dic:
                return acc+i




re =Solution().maxTotalReward(rewardValues = [1,6,4,3,2])
print(re)