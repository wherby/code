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
            if (1<<a)&key:
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
            return ret
        @cache
        def dfs(key,a,b,c):
            nonlocal mxv
            if key == -1:
               
                return a+b+c
            
            ret = 0
            ls1 = [0,0] + g[key]
            print(key,a,b,c,ls1)
            m = len(ls1)
            for i in range(m):
                for j in range(i+1,m):
                    acc =  b
                    ls2 = []
                    for k in range(m):
                        if (k != i  and k !=j) and ls1[k] != 0:
                            ls2.append(ls1[k])
                    print(ls2,ls1[i],ls1[j],ls1)
                    for b in ls2:
                        acc = acc&b
                    ret = max(ret,dfs(key-1, a^ls1[i],acc,c ^ls1[j]))
            return ret

        mxv = max(mxv, dfs(mxk,0,(1<<30)-1,0))
        return mxv





re =Solution().maximizeXorAndXor( [2,3])
print(re)