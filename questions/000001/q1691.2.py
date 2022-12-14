# https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/
from typing import List, Tuple, Optional

from sortedcontainers import SortedDict,SortedList
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [sorted(c) for c in cuboids]
        n = len(cuboids)
        dp = [0]*n
        cuboids.sort()
        for i in range(n):
            dp[i] = cuboids[i][2]
            a = cuboids[i]
            for j in range(i):
                b = cuboids[j]
                if a[0]>=b[0] and a[1] >=b[1] and a[2]>=b[2]:
                    dp[i] = max(dp[i],dp[j]+a[2],dp[j])
        return max(dp)
            
        
re = Solution().maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]])
print(re)
            