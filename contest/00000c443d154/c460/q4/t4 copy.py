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
import itertools

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        g = defaultdict(list)
        for a in nums:
            x= len(str(bin(a))[2:])
            g[x].append(a)
        mxk = max(g.keys())
        mxv = 0

        def getXor(key, ls ,a ):
            m = len(ls)
            t = [i for i in range(m)]
            ret =[]
            if (1<<key)&a:
                for j in range(0,m+1,2):
                    chooseIDXs = itertools.combinations(t,j)
                    for chooseIdx in chooseIDXs:
                        chooseIdx = set(chooseIdx)
                        acc = a 
                        tmp = []
                        for k in range(m):
                            if k in chooseIdx:
                                acc =acc ^ls[k]
                            else:
                                tmp.append(ls[k])
                        ret.append([acc,list(tmp)])
            else:
                for j in range(1,m+1,2):
                    chooseIDXs = itertools.combinations(t,j)
                    for chooseIdx in chooseIDXs:
                        chooseIdx = set(chooseIdx)
                        acc = a 
                        tmp = []
                        for k in range(m):
                            if k in chooseIdx:
                                acc =acc ^ls[k]
                            else:
                                tmp.append(ls[k])
                        ret.append([acc,list(tmp)])
            return ret
        def getXor2(key, ls ,a ):
            m = len(ls)
            t = [i for i in range(m)]
            ret =[]
  
            for j in range(0,m+1):
                chooseIDXs = itertools.combinations(t,j)
                for chooseIdx in chooseIDXs:
                    chooseIdx = set(chooseIdx)
                    acc = a 
                    tmp = []
                    for k in range(m):
                        if k in chooseIdx:
                            acc =acc ^ls[k]
                        else:
                            tmp.append(ls[k])
                    ret.append([acc,list(tmp)])
            return ret
        def getAnd(ls,b):
            acc = b
            if b == 0:
                if len(ls):
                    acc = ls.pop()
            for a in ls:
                acc = acc&a 
            return acc
        @cache
        def dfs(key,a,b,c):
            nonlocal mxv
            if key == -1:
                #print(a,b,c,"a")
                return a+b+c
            ret = dfs(key-1,a,getAnd(list(g[key]),b),c)
            ls = list(g[key])
            tmp1 = getXor(key,ls,a)
            for a1,ls1 in tmp1:
                tmp2 = getXor2(key,ls1,c)
                for c1,ls2 in tmp2:
                    b1 = getAnd(ls2,b)
                    #print(a1,b1,c1,ls1,ls2,ls)
                    ret = max(ret,dfs(key-1,a1,b1,c1))
            return ret

        mxv =  dfs(mxk,0,0,0)
        return mxv





re =Solution().maximizeXorAndXor( [14,162,43])
print(re)