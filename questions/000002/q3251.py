from typing import List, Tuple, Optional

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mx = max(nums)
        N = mx +1
        dp = [0]*N
        for i in range(nums[0] +1):
            dp[i] =1 
        
        for i,a in enumerate(nums[1:],1):
            tmp =[0]*N
            pre = [0]
            for x in range(a+1):
                
                pre.append(pre[-1] + dp[x])
                y = a -x
                x1= nums[i-1]-y
                #print(x1,x,pre)
                if x1 >=0:
                    tmp[x] = pre[min(x1,x)+1]
            dp = tmp 

        mod = 10**9+7 
        return sum(dp)%mod 

re = Solution().countOfPairs([1,17])
print(re)

        