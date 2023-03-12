# https://leetcode.cn/contest/weekly-contest-335/problems/number-of-ways-to-earn-points/

from typing import List, Tuple, Optional

from collections import defaultdict


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:

        dp = [0]*(target+1)
        dp[0] =1
        #res[0]=1
        mod=10**9+7
        for count,marks in types:
            for j in range(target,-1,-1):
                for k in range(1,min(count,j//marks) +1):
                    dp[j] += dp[j-marks*k]
                dp[j] %=mod
        return dp[-1]




types=[[6,1],[49,2],[33,3],[26,4],[28,5],[45,6],[4,7],[23,8],[46,9],[39,10],[12,11],[28,12],[37,13],[18,14],[10,15],[27,16],[26,17],[10,18],[34,19],[11,20],[35,21],[5,22],[47,23],[19,24],[15,25],[27,26],[50,27],[3,28],[24,29],[18,30],[49,31],[32,32],[18,33],[5,34],[34,35]]
re =Solution().waysToReachTarget(target = 500, types =types)
print(re)