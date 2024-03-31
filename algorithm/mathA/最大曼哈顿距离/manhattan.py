# https://leetcode.cn/contest/weekly-contest-391/problems/minimize-manhattan-distances/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf




def maxManhattan(ps):
    ls = []
    for i,(x,y) in enumerate(ps):
        ls.append((x+y,x-y,y-x,-x-y,i))
    mx =-1
    ret =[]
    for i in range(4):
        ls.sort(key=lambda x:x[i])
        #print(ls)
        a,b = ls[0][4],ls[-1][4]
        tmp = abs(ps[a][0] -ps[b][0]) + abs(ps[a][1] -ps[b][1])
        if tmp>mx:
            ret = [a,b]
            mx = tmp 
    return (mx,ret)

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        mx,ret = maxManhattan(points)
        res = 10**10
        a,b = ret 
        #print(a,b,mx)
        ps1 = points[:a] + points[a+1:]
        ps2 =points[:b] + points[b+1:]
        for ps in ps1,ps2:
            mx,ret = maxManhattan(ps)
            if mx <res:
                res =mx
        return res
                
            





re =Solution().minimumDistance(points = [[3,10],[5,15],[10,2],[4,4]])
print(re)