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
        
        ret2 = ["A" for a in caption]
        dp = [10**10 for _ in range(n)]
        atoz = 'abcdefghijklmnopqrstuvwxyz'
        ordz = {}
        for i,a in enumerate(atoz):
            ordz[a] = i 
        #)
        tot= 10**10
        retv = ""
        
        
        def dfs(i,p1,p2,p3,acc):
            nonlocal tot,retv
            if i == n:
                print(acc,ret)
                if acc< tot:
                    tot = acc
                    retv = "".join(ret)
                return 
            
            dfs(i+1,p1,p1,p2,acc + abs(ordz[caption[i]]-ordz[p1]))
            if p1==p2==p3 and i<=n-3:
                for j,a in enumerate(atoz):
                    t= acc + abs(j-ordz[caption[i]])
                    if a ==p1:
                        if t <dp[i] or (dp[i]== t and p1 <ret[i]) :
                            dp[i] =t 
                            ret[i]=ret[i-1]=ret[i-2] = p1
                        
                    dfs(i+1,a,p1,p2,t) 
            t =acc + abs(ordz[caption[i]]-ordz[p1])
            if p1 ==p2 :
                if t <dp[i] or (dp[i]== t and p1 <ret[i]):
                    dp[i] = t
                    ret[i] =ret[i-1]=ret[i-2]=p1

            
            
        res = 10**10
        for a in atoz:
            dp = [10**10 for _ in range(n)]
            ret = ["A" for a in caption]
            ret[0]=ret[1]=ret[2]=a
            acc = 0
            for i in range(3):
                acc += abs(ordz[a]-ordz[caption[i]])
            dp[2]=acc
            #print(ret)
            dfs(3,a,a,a,acc)
            #print(a,ret,dp)
            # if dp[-1] < res :
            #     #print("*")
            #     res = dp[-1] 
            #     ret2 = list(ret)
                #print(ret)
        return retv



# FILEDEBUG =True
# if FILEDEBUG:
#     import os

#     abspath = os.path.abspath(__file__)
#     dname = os.path.dirname(abspath)
#     os.chdir(dname)

#     import sys

#     orig_stdout = sys.stdout
#     f = open('./.tmp/outt4.fist.txt', 'w')
#     sys.stdout = f

#     #Start print
#     #print(ret2)
#     #ret2[1]=[1]
re =Solution().minCostGoodCaption(caption ="qviioqk")
print(re)

# if FILEDEBUG:
#     sys.stdout = orig_stdout
#     f.close()
#     print("finished")

