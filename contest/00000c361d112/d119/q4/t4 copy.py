# 
# https://leetcode.cn/contest/biweekly-contest-119/problems/number-of-possible-sets-of-closing-branches/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        dic={}
        MX =10**20
        for a,b,c in roads:
            if a >b:
                a,b = b,a
            dic[(a,b)] = min(dic.get((a,b),MX),c)
        for a,b,c in roads:
            if a >b:
                a,b = b,a
            g[a].append((b,dic[(a,b)]))
            g[b].append((a,dic[(a,b)]))
        #print(g,dic)
        def verify(state):
            lef =set()
            for i in range(n):
                if state &(1<<i):
                    lef.add(i)
            
            # if start ==-1:
            #     return True
            dp = [[MX]*n for _ in range(n)]
            for i in range(n):
                dp[i][i] =0

            for i in lef:
                for b,c in g[i]:
                    if b in lef:
                        dp[i][b] =c 
                        dp[b][i] = c
            #print(dp,lef)
            for k in range(n):  ## a,b,k顺序错，结果不对
                for a in range(n):
                    for b in range(n):
                        #if (a in lef) and (b in lef) and (k in lef):
                        dp[a][b] = min(dp[a][b], dp[a][k]+dp[k][b])
            #print(dp)
            for a in range(n):
                for b in range(n):
                    if (a in lef) and (b in lef):
                        if dp[a][b] > maxDistance:
                            #print(a,b,dp[a][b])
                            return False
            return True
        
        ret = 0
        for state in range(1<<n):
            if verify(state):
                #print(state)
                ret +=1
        #verify(15)
        return ret




re =Solution().numberOfSets(10,430,[[3,2,237],[3,1,79],[6,1,84],[6,1,103],[9,6,453],[3,1,342],[3,1,201],[8,0,439],[7,5,467],[4,3,99],[8,7,146],[8,7,335],[6,1,512],[1,0,498],[5,3,241],[5,2,202],[4,1,443],[2,0,69],[2,1,450],[6,3,352],[2,0,438],[4,0,95],[6,1,257],[5,1,271],[8,1,80],[9,1,452],[3,1,57],[9,7,361],[8,4,105]])
print(re)