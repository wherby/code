class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        lsW =[0]*12
        for i,a in enumerate(aliceArrows):
            lsW[i] = a +1
        dp= [[0]*(numArrows+1) for _ in range(12)]
        record =[[-1]*(numArrows+1) for _ in range(12)]
        for i in range(12):
            for j in range(numArrows+1):
                record[i][j] = (0,j)
        for i in range(12):
            for j in range(1,numArrows+1):
                dp[i][j] = dp[i-1][j]
                record[i][j]=(0,j)
                if j>=lsW[i]:
                    if dp[i][j]<dp[i-1][j-lsW[i]] + i:
                        dp[i][j] = dp[i-1][j-lsW[i]] + i
                        #print(i,j)
                        record[i][j] = (i,j-lsW[i])
        res =[0]*12
        tp = numArrows
        for i in range(11,-1,-1):
            #print(i,tp,record[i][tp],res)
            idx,arrows = record[i][tp]
            if idx !=0:
                res[idx]=lsW[idx]
            tp = arrows
        res[0] = numArrows -sum(res)
        return res

re =Solution().maximumBobPoints(numArrows = 89, aliceArrows = [3,2,28,1,7,1,16,7,3,13,3,5])
print(re)