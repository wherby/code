
import collections
class Solution:
    def numberOfGoodSubsets(self, nums) -> int:
        primes=[2,3,5,7,11,13,17,19,23,29]
        mod = 10**9 +7
        dp = [1] +[0] *(1 <<10)
        count = collections.Counter(nums)
        for a in count:
            if a == 1: continue
            if a %4 ==0 or a % 9 ==0 or a % 25 ==0 : continue
            mask = sum(1 <<i  for i,p in enumerate(primes) if a %p ==0)
            for i in range(1<<10):
                if i & mask : continue
                dp[i | mask] = (dp[i|mask] + count[a] * dp[i]) %mod
        return (1<< count[1]) * (sum(dp) -1) % mod




re = Solution().numberOfGoodSubsets([4,2,3,15])
print(re)
