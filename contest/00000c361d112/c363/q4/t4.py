from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList


def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        n  = len(nums)
        pls = get_prime(n+1)
        dp = [i for i in range(n+2)]
        for i in pls:
            for j in range(i,n+1,i):
                while dp[j]%(i*i) ==0:
                    dp[j] =dp[j]//(i*i)
        #print(dp)
        for i in range(1,n+1):
            dic[dp[i]].append(i)
        mx = 0 
        #print(dic)
        for k,v in dic.items():
            mx = max(mx,sum([nums[i-1] for i in v ]))
        return mx





re =Solution().maximumSum(nums = [1,100,100,1])
print(re)