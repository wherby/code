# https://leetcode.cn/contest/weekly-contest-410/problems/find-the-count-of-monotonic-pairs-ii/description/

from typing import List, Tuple, Optional

import sys
sys.setrecursionlimit(10000000)

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        
        dp = [[0]*1001 for _ in range(n)]
        for i in range(nums[0]+1):
            dp[0][i] = 1
        #print(dp[0][:6])
        for i in range(1,n):
            pre = [0]
            for j in range(1001):
                pre.append(pre[-1] + dp[i-1][j])
            for j in range(nums[i]+1):
                d = nums[i] - nums[i-1]
                if d <=0:
                    dp[i][j] = pre[j+1] 
                else:
                    dp[i][j] =pre[j-d+1] if j-d+1 >=0 else 0
            #print(dp[i][:6],i,pre[:6])
        return sum(dp[-1]) %mod



ls = [1000]*2000
re =Solution().countOfPairs( ls)
print(re)