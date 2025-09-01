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


def getAllDiv(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    def getAllComb(pls,n):
        ret =[]
        for p in pls:
            while n%p ==0:
                ret.append(p)
                n = n//p 
        return ret
    allC = getAllComb(res,n)
    ret =set([])
    for i in range(2<<len(allC)):
        acc =1
        for j in range(len(allC)):
            if (1<<j) &i :
                acc *= allC[j]
        ret.add(acc)
    return ret

class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        mx = max(nums)
        dp = [0]*(mx+1)
 
        mod = 10**9+7
        for a in nums:
            
            for j in range(a,mx +1,a):
                dp[a] += (1<<dp[j])-1
            
            da = getAllDiv(a)
            for j in da:
                dp[j] *= 1<<dp[a] 
            dp[a] +=1
        acc =0
        for i,a in enumerate(dp):
            acc +=a*i
        return acc%mod





re =Solution().totalBeauty([4,6])
print(re)