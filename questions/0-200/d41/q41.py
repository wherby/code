class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        boxes=[[-1,0]]+ boxes
        n =len(boxes)
        dp =[10**10]*(n+1)
        dp[0] =0
        j =0
        lastJ =0
        tp =0
        weight =0
        for i in range(1,n):
            while j+1<n and j+1-i+1 <= maxBoxes and weight + boxes[j+1][1] <= maxWeight:
                j +=1
                weight += boxes[j][1]
                if boxes[j][0] != boxes[j-1][0]:
                    tp +=1
                    lastJ =j
                # if boxes[j][0] != lastPort:
                #     lastPort = boxes[j][0]
                #     lastJ = j
            dp[j] = min(dp[j], dp[i-1] + tp  +1)
            if j+1 <n and boxes[j][0] == boxes[j+1][0]:
                dp[lastJ-1] = min(dp[lastJ-1],dp[i-1]+ tp)
            weight -= boxes[i][1]
            tp -= (i+1 <n and boxes[i][0] != boxes[i+1][0])
        #print(dp[-30:])
        return dp[n-1]  

re = Solution().boxDelivering(boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6)
print(re)