# https://leetcode.cn/contest/biweekly-contest-133/problems/count-the-number-of-inversions/description/
## 递推逆序对数目的可能值
## 然后移除不合法的状态进行转移

from typing import List, Tuple, Optional

from collections import defaultdict,deque
import math
INF  = math.inf

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10**9+7
        requirements.sort()
        rd ={}
        for a,b in requirements:
            rd[a] = b
        dp =defaultdict(int)
        mxk= 0
        dp[0] =1 
        for i in range(n):
            dp2 = defaultdict(int)
            acc=0
            for j in range(mxk + i+1):
                acc += dp[j]
                if j > i:
                    acc-= dp[j-i-1]
                dp2[j] = acc%mod
            mxk= mxk+i
            
            if i in rd:
                for k in dp2.keys():
                    if k != rd[i]:
                        dp2[k] = 0
            dp= dp2
            #print(dp,i)
        return dp[requirements[-1][1]]%mod 



re =Solution().numberOfPermutations(n = 5, requirements =[[0,0],[1,0],[4,6],[3,4]])
print(re)