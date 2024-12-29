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
    def checkValidCuts(self, n: int, rs: List[List[int]]) -> bool:
        
        def check(lss):
            lss.sort()
            n = len(lss)
            cnt =0
            end = lss[0][1]
            for i in range(n):
                if lss[i][0]<end:
                    end = max(end,lss[i][1])
                else:
                    cnt +=1
                    end = lss[i][1]
            return cnt
        xss,yss =[],[]
        m = len(rs)
        for i in range(m):
            xss.append((rs[i][0],rs[i][2]))
            yss.append((rs[i][1],rs[i][3]))
        cntx,cnty =check(xss),check(yss)
        #print(xss,yss)
        return cntx >=2 or cnty>=2


re =Solution().checkValidCuts(n = 5, rs = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]])
print(re)