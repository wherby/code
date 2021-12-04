class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        valueSet = [[0]*1024 for _ in range(k)]
        totalCount = [0]*k
        for i,a in enumerate(nums):
            valueSet[i%k][a]+=1
            totalCount[i%k] +=1
        dp = [[0]*1024 for i in range(2001)]
        n = len(nums)
        
        for d in range(1024):
            dp[0][d] = totalCount[0] -valueSet[0][d]
        for i in range(1,k):
            minCost = 1000000
            x =-1
            for d in range(1024):
                if dp[i-1][d] < minCost:
                    minCost  = dp[i-1][d]
                    x =d
            #print(minCost,x)
            for d in range(1024):
                # if x not in value exists # totalCount[i] - valueSet[i][v] <==cost function if choose v as value at index i
                v = d^ x
                dp[i][d] = minCost + totalCount[i] - valueSet[i][v]

                for j in range(i,n,k):
                    v = nums[j]
                    dp[i][d] = min(dp[i][d],dp[i-1][v^d] + totalCount[i] - valueSet[i][v])
        #print(dp[k-1][:30],dp[0][:30],dp[1][:30])
        return dp[k-1][0]
            
re = Solution().minChanges(nums = [1,2,4,1,2,5,1,2,6], k = 3)
print(re)