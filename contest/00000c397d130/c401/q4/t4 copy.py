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
        sl = SortedList([])
        dic= {}
        dic[0] =1
        lst =0
        for a in ls:
            for i in range(max(a,lst),2*a):
                sl.add(i)
            #print(sl,a)
            rm = []
            l = 0
            while l < len(sl) and sl[l]<a:
                rm.append(sl[l])
                l+=1

            for b in rm:
                sl.remove(b)
            lst =a*2-1
            rm = []
            
            for j in sl:
                if j-a in dic:
                    dic[j] =1
                    rm.append(j)
            
            for b in rm:
                sl.remove(b)
            #print(sl,dic)
        for i in range(acc-1,-1,-1):
            if i in dic:
                return acc+i




re =Solution().maxTotalReward(rewardValues =  [2,17,12])
print(re)