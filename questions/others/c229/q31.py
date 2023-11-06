import functools
from math import inf
class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        m = len(multipliers)
        n = len(nums)
        dp =[[0]*(m+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[0][i] =dp[0][i-1] + nums[n-i]*multipliers[i-1]
            dp[i][0] = dp[i-1][0]   + nums[i-1] *multipliers[i-1]
        for l in range(1,m+1):
            for r in range(1,m+1):
                midx = l+r-1
                if midx < m:
                    dp[l][r] = max(dp[l-1][r] + nums[l-1]*multipliers[midx] ,
                     dp[l][r-1] + nums[n-r]*multipliers[midx])
        mx = -inf
        for i in range(m+1):
            j =m-i
            mx = max(mx, dp[i][j])
        return mx

nums = [-854,-941,10,299,995,-346,294,-393,351,-76,210,897,-651,920,624,969,-629,985,-695,236,637,-901,-817,546,-69,192,-377,251,542,-316,-879,-764,-560,927,629,877,42,381,367,-549,602,139,-312,-281,105,690,-376,-705,-906,85,-608,639,752,770,-139,-601,341,61,969,276,176,-715,-545,471,-170,-126,596,-737,130]
multipliers =[83,315,-442,-714,461,920,-737,-93,-818,-760,558,-584,-358,-228,-220]
re =Solution().maximumScore(nums , multipliers )
print(re)

