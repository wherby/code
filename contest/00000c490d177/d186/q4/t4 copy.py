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
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        mod = 10**9+7 
        L= len(target)
        def get_ways(w1,w2):
            n,m =len(w1),len(w2)
            
            @cache 
            def dfs(idx,i,j):
                if idx == L:
                    return 1 
                res = 0
                ch = target[idx]
                for ni in range(i,n):
                    if w1[ni] == ch:
                        res = (res+dfs(idx+1,ni+1,j))%mod 
                for nj in range(j,m):
                    if w2[nj] == ch:
                        res =(res +dfs(idx+1,i,nj+1))%mod 
                return res 
            ret = dfs(0,0,0)
            dfs.cache_clear()
            return ret
        tot = get_ways(word1,word2)
        t1 = get_ways(word1,"")
        t2 = get_ways(word2,"")
        return (tot-t1-t2)%mod
        





re =Solution().interleaveCharacters( word1 = "abc", word2 = "bac", target = "abc")
print(re)