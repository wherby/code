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
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        ret = ["A" for a in caption]
        ret2 = [a for a in caption]
        dp = [10**10 for _ in range(n)]
        atoz = 'abcdefghijklmnopqrstuvwxyz'
        ordz = {}
        for i,a in enumerate(atoz):
            ordz[a] = i 
        #)
        @cache
        def dfs(i,p1,p2,p3):
            if i == n:
                return 0
            res = 10**10 
            rev =""
            if p1==p2==p3:
                for j,a in enumerate(atoz):
                    if a ==p1:
                        t = dfs(i+1,a,p1,p2) + abs(j-ordz[caption[i]])
                    else:
                        t = dfs(i+1,a,p1,p2) + abs(j-ordz[caption[i]]) +10**10
                    res = min(res,t)
                    if res< dp[i] :
                        dp[i] =res
                        rev = a 
                        ret[i] =ret[i-1]=ret[i-2]=p1
            t = dfs(i+1,p1,p1,p2) + abs(ordz[caption[i]]-ordz[p1])
            res = min(res,t)
            if p1 ==p2 :
                if res <dp[i] or (dp[i]== res and p1 <ret[i]):
                    dp[i] = res 
                    ret[i] =ret[i-1]=ret[i-2]=p1
            dp[i]= res 
            #ret[i] = rev
            #print(res,rev,i)
            return res
        res = 10**10
        for a in atoz:
            ret[0]=ret[1]=ret[2]=a
            c1 = dfs(3,a,a,a) +abs(ordz[a] - ordz[ caption[0]]) +abs(ordz[a] - ordz[ caption[1]])+abs(ordz[a] - ordz[ caption[2]])
            #print(c1,a,ret)
            if c1 < res :
                res = c1 
                ret2 = list(ret)
                ret2[0]=ret2[1]=ret2[2] =a 
                #print(ret)
        return "".join(ret2)





re =Solution().minCostGoodCaption(caption = "owsjeo")
print(re)