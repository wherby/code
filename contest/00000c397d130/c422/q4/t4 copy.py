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
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 +7
        n = len(num)
        ls = [0]*10
        for a in num:
            ls[int(a)]+=1
        sm = sum([int(a) for a in num])
        hfn = n //2
        hsm = sm //2
        if sm%2 ==1:
            return 0
        
        def getComb(s1):
            sm = sum(s1)
            acc =1 
            for a in s1:
                acc*= math.comb(sm,a)
                sm -= a 
            return acc
        
        def cont(state):
            rstate = [a-b for a,b in zip(ls,state)]
            return getComb(state) * getComb(rstate)
        
        #print(cont([0]*10))

        @cache
        def dfs(state,idx,acc):
            if idx == hfn:
                if acc == hsm:
                    print(state,cont(state))
                    return cont(state)
                return 0 
            ret =0
            for i in range(10):
                if state[i] < ls[i]:
                    ns = list(state)
                    ns[i] +=1
                    ns = tuple(ns)
                    ret += dfs(ns,idx +1,acc +i)
            return ret
        
        return dfs(tuple([0]*10),0,0)%mod





re =Solution().countBalancedPermutations("4567")
print(re)