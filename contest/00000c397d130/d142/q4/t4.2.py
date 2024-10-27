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
        ways = 1
        for x in kstr:
            ways = ways*(x)%mod
        dp =[0]*(k)
        dp[0] = 1
        for a in kstr:
            tmp = [0]*(k)
            acc = 0
            for j in range(1,k):
                acc += dp[j-1] if j-1 >=0 else 0 
                acc -= dp[j-a-1] if j-a-1 >=0 else 0 
                tmp[j] = acc%mod  
         
            dp =tmp
            #print(dp)
        #print(dp,ways)
        return (ways-sum(dp))%mod









re =Solution().possibleStringCount("aabbccdd", k = 7)
print(re)