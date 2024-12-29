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
    def minLength(self, s: str, numOps: int) -> int:
        s = [int(a) for a in s]
        def getN(s,numOps):
            n = len(s)
            
            def verify(mid):
                state = 1
                lstV = s[0]
                cnt =0
                for i in range(1,n):
                    if s[i] == lstV:
                        state +=1
                        if state>mid:
                            state=1
                            lstV = 1- lstV
                            cnt +=1
                            if cnt >numOps:
                                return False
                    else:
                        lstV = s[i]
                        state =1
                return True
            l,r =1,n
            while l<r:
                mid = (l+r)>>1
                if verify(mid):
                    r=mid 
                else:
                    l= mid+1
            return l
        
        ret = min(getN(s,numOps),getN(s[::-1],numOps))
        if numOps >0:
            s1= list(s)
            s1[0] = 1- s1[0]
            s2 = list(s)[::-1]
            s2[0] = 1 -s2[0]
            numOps -=1
            ret =min(ret,getN(s1,numOps),getN(s2,numOps))
        return ret


re =Solution().minLength("00100",2)
print(re)