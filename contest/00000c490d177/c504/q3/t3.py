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
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MX= max(i[0] for i in items)+1
        ls= [0]*MX

        for f,p in items:
            ls[f] +=1
        for i in range(1,MX):
            cur = 0 
            for j in range(i,MX,i):
                cur+= ls[j]
            ls[i] = cur 
        
        st = []
        mnp = min(i[1] for i in items)
        for f,p in items:
            if ls[f] -1>0:
                heappush(st, (p,ls[f]-1))
        #print(st,ls)
        cur = 0
        cnt =0
        while st and st[0][0] < mnp*2 and cur + st[0][0]<=budget:
            p,rest = heappop(st)
            cur  += p 
            cnt +=2 
            rest -=1 
            if rest >0:
                heappush(st,(p,rest))
            #print(cur,cnt,st)
        return cnt + (budget - cur)//mnp




re =Solution().maximumSaleItems(items = [[1,6],[2,4],[3,5]], budget = 19)
print(re)