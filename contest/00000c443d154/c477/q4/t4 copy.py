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
    def countEffective(self, nums: List[int]) -> int:
        mod = 10**9+7
        sm = 0 
        n = len(nums)
        for a in nums:
            sm = sm| a 
        idx = [i for i in range(32) if (1<<i)&sm]
        m = len(idx)
        dic = defaultdict(int)
        for num in nums:
            acc = 0 
            for i,a  in enumerate(idx):
                if (1<<a)&num:
                    acc|= 1<<i
            dic[acc] +=1
        dp = [0]*(1<<m)
        for k,v in dic.items():
            dp[k] = v
        u = 1<<m
        for i in range(m):
            bit = 1<<i
            s = 0 
            while s <u:
                s |= bit  # 快速跳到第 i 位是 1 的 s
                dp[s] += dp[s^bit]
                s +=1
        ret = pow(2,n,mod)
        all=u-1
        for t in range(1<<m):
            op = bin(t).count("1")%2 
            op = 1 if op else -1 
    
            ret += pow(2,dp[t^all],mod)*op
            #print(op,t,dp[t])
        return ret%mod



re =Solution().countEffective([1,2,3])
print(re)