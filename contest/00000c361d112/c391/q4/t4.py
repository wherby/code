from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        mxd,ret =10**10,10**10
        sl =SortedList([])
        dic ={}
        
        def findD1(ls,x,y,a):
            idx = sl.bisect_right(y)
            ret = []
            ret.append(abs(x-a)+abs(y-sl[idx-1]))
            if idx != len(ls):
                ret.append(abs(x-a)+ abs(y-sl[idx]))
            return ret
        
        for x,y in points:
            if len(sl) !=0:
                tmp =[]
                idx = sl.bisect_right(x)
                tmp.extend(findD1( dic[sl[idx-1]],x,y,sl[idx-1]))
                if idx != len(sl):
                    tmp.extend(findD1(dic[sl[idx]],x,y,sl[idx]))
                tmp.sort()
                if tmp[0]<mxd:
                    ret = mxd
                    mxd=tmp[0]
                elif tmp[0]<ret:
                    ret =tmp[0]
            if x not in dic:
                dic[x] = SortedList([])
                sl.add(x)
            dic[x].add(y)
            print(x,y,ret,mxd)
        return ret
                
            





re =Solution().minimumDistance(points = [[3,10],[5,15],[10,2],[4,4]])
print(re)