from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        dp = [[0]*1000 for _ in range(6)]
        dp[0][0] = 1
        for a in s:
            #print(a)
            a = int(a)
            mod =10**9+7
            for j in range(5,0,-1):
                for m in range(100):
                    if j == 5:
                        idx = a *100 + m 
                        dp[5][idx] += dp[4][idx]%mod
                    if j == 4:
                        idx = m //10*100 + a * 10 + m %10
                        dp[4][idx] += dp[3][idx]%mod
                    if j ==3:
                        idx = m*10 + a 
                        dp[3][idx] += dp[2][m*10]%mod
                    if j ==2 and m<10:
                        idx =m*100 + a*10 
                        dp[2][idx]  += dp[1][m*100] 
                    if j ==1 and m==0:
                        idx = a*100
                        dp[1][idx]  += dp[0][0]
        cnt =0 
        
        for i in range(1000):
            cnt += dp[5][i]
        return cnt%mod




re =Solution().countPalindromes("103301")
print(re)