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

        @cache
        def dfs(idx,res):
            if idx == n or res ==0:
                return 1 
            ret = 0
            for i in range(min(res,kstr[idx]-1) +1):
                ret += dfs(idx+1,res -i)
            return ret%mod
        ret =dfs(0,res)%mod
        dfs.cache_clear()
        return ret







re =Solution().possibleStringCount(word = "aaabbb", k = 3)
print(re)