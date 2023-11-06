class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        n= len(plants)
        dp= [1]*n
        res =capacity -plants[0]
        for i in range(1,n):
            if res >= plants[i]:
                res -=plants[i]
                #print(dp,dp[i],dp[i-1],1)
                dp[i]=dp[i-1] +1
                #print(dp,dp[i-1])
            else:
                dp[i]+=i*2+ dp[i-1]
                #dp[i]+=1
                res =capacity- plants[i]
            #print(dp)
        #print(dp)
        return dp[-1]

re = Solution().wateringPlants(plants = [2,2,3,3], capacity = 5)