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
            dp = [[0]*(m+1) for _ in range(n+1)]
            dp[0][0] =1 
            for ch in target:
                ndp = [[0]*(m+1) for _ in range(n+1)]
                row = [0]*(m+1)
                for j in range(n+1):
                    col  = 0 
                    for k in range(m+1):
                        if j >0 and w1[j-1] ==ch:
                            ndp[j][k] = (ndp[j][k] +  row[k])%mod 
                        if k >0 and w2[k-1] == ch:
                            ndp[j][k] = (ndp[j][k] + col) %mod 
                        row[k] = (row[k] + dp[j][k]) % mod 
                        col = (col + dp[j][k])%mod 
                dp = ndp 
            
            return sum(sum(row) for row in dp) %mod
        tot = get_ways(word1,word2)
        t1 = get_ways(word1,"")
        t2 = get_ways(word2,"")
        return (tot-t1-t2)%mod
        





re =Solution().interleaveCharacters( word1 = "abc", word2 = "bac", target = "abc")
print(re)