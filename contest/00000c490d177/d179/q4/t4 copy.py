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
    def countArrays(self, digitSum: list[int]) -> int:
        mod = 10**9+7
        dic =defaultdict(list)
        for a in range(0,5001):
            t= sum([int(b) for b in str(a) ])
            dic[t].append(a)
        
        n = len(digitSum)

        dp = [0] * 5001
        for v in dic[digitSum[0]]:
            dp[v] = 1
            
        for i in range(1, n):
            prefix_sum = [0] * 5002
            for j in range(5001):
                prefix_sum[j+1] = (prefix_sum[j] + dp[j]) % mod
            
            new_dp = [0] * 5001
            for v in dic[digitSum[i]]:
                new_dp[v] = prefix_sum[v+1]
            dp = new_dp
            
        return sum(dp) % mod


ls = [2,7,10,10,14,6,12,8,9,11,11,6,11,7,9,18,12,8,12,15,11,16,20,21,7,17,19,20,22,20,17,19,19,18,23,13,18,16,16,23,6,10,8,11,14,18,13,7,11,15,22,16,11,19,17,16,19,9,18,15,21,19,19,15,18,22,16,13,15,12,18,4,16,10,13,4,7,15,20,14,13,14,15,23,14,12,16,13,17,10,16,16,16,18,17,19,20,23,22,23,25,12,23,14,19,21,22,20,11,9,12,19,11,16,18,9,10,24,13,21,14,24,23,21,26,26,16,16,20,23,19,13,17,26,10,7,13,12,19,21,8,9,10,16,15,18,17,9,24,15,17,17,20,14,21,25,22,28,14,13,15,23,23,16,28]

re =Solution().countArrays(ls)
print(re)