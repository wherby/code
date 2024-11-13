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
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 10**9+7
        cands =[]
        n = len(s)
        dp = [0]*(n+1)
        cands.append(1)
        for i in range(2,n+1):
            dp[i] = dp[bin(i).count("1")] +1
            if dp[i]<k:
                cands.append(i)
        #cands.sort()
        #print(cands[:10],n-1)
        @cache
        def f(i,mask,is_limit,is_num):
            if i ==len(s):
                #print(mask)
                return not int(is_limit) if mask==0 else 0
            res =0
            if not is_num:
                res = f(i+1,mask,False,False) ##计算 0-9，10-99，100-999，1000-9999
            up = int(s[i]) if is_limit else 1
            for d in range(0 if is_num else 1, up +1):
                if d == 1 and mask ==0: continue
                res += f(i+1,mask-d,is_limit and d ==up, True)
            return res
        acc = 0
        for a in cands:
            if a > n:continue
            acc += f(0,a,True,False)
        f.cache_clear()
        return (acc)%mod



#re =Solution().countKReducibleNumbers(s = "111", k = 1)
#re =Solution().countKReducibleNumbers(s = "1000", k = 2)
# re =Solution().countKReducibleNumbers(s = "11", k = 2)
# print(re,2)
re =Solution().countKReducibleNumbers(s = "111", k = 1)
print(re,3)
# print(re)
re =Solution().countKReducibleNumbers(s = "10010", k = 2)
print(re)

# for i in range(18):
#     if bin(i).count("1")>0 and bin(i).count("1")<=2:
#         print(i,bin(i))