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
    def possibleStringCount(self, word: str, k: int) -> int:
        mod= 10**9+7
        n = len(word)
        res = n - k 
        lst = ""
        cnt = 0
        kstr = []
        word += "*"
        for a in word:
            if a ==lst:
                cnt +=1
            else:
                if cnt >0:
                    kstr.append(cnt)
                    cnt = 1
                    lst = a 
                else:
                    cnt = 1
                    lst =a
        #print(kstr)
        n = len(kstr)
        ways = 1 
        for a in kstr:
            ways= ways*a %mod 
        if len(kstr) >=k:
            return ways

        @cache
        def dfs(idx,res):
            if idx == n :
                if res >=k:
                    return 1 
                else:
                    return 0 
            if res>=k:
                return (kstr[idx])*dfs(idx+1,k)%mod
            ret = 0
            for i in range(1,kstr[idx]+1):
                ret += dfs(idx+1,min(i+res,k))
            return ret%mod
        ret =dfs(0,0)%mod
        dfs.cache_clear()
        return ret







re =Solution().possibleStringCount(word = "aaabbb", k = 3)
print(re)