
from collections import Counter
class Solution:
    def numberOfGoodSubsets(self, nums) -> int:
        pms =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        ct = Counter(nums)
        dp=[0]*2000
        dp[0]=1
        for a in ct:
            if a ==1: continue
            if a %4 ==0 or a %9==0 or a %25 ==0: continue
            msk = sum([1<<i for i,p in enumerate(pms) if a%p ==0])
            for i in range(1<<10):
                if i &msk ==msk:
                    #print(i,msk)
                    dp[i] = dp[i] + dp[i-msk] *ct[a]
        #print(dp[:10])
        mod = 10**9+7
        return (1<<ct[1]) * (sum(dp)-1)%mod
            
            


re = Solution().numberOfGoodSubsets([1,2,3,4])
print(re)
