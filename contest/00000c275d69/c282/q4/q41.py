
class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        oneMin =10**9
        for f,r in tires:
            if r ==1:
                oneMin = min(oneMin,f)
        dp= [10**9]*20
        for f,r in tires:
            if r >1:
                sm = 0
                for i in range(1,20):
                    sm += f*(r**(i-1))
                    dp[i] =min(dp[i],sm)
        #print(dp)
        dp[0] =0
        cost = [10**15]*(numLaps+1)
        cost[0] =0
        for i in range(1,numLaps+1):
            for j in range(min(i,19)+1):
                cost[i] = min(cost[i],cost[i-j]+ changeTime +dp[j])
        #print(cost)
        return cost[numLaps]-changeTime


re = Solution().minimumFinishTime(tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4)
print(re)

