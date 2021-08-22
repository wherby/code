class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        leftLow =[1000000]*n
        rightHigh = [0]*n
        for i in range(n):
            if i ==0:
                leftLow[i] = prices[i]
                rightHigh[n-1-i] =prices[n-1-i]
            else:
                leftLow[i]  = min(prices[i],leftLow[i-1])
                rightHigh[n-1-i]= max(prices[n-1-i],rightHigh[n-i])
        fromLeft = [0]*n
        fromRight= [0]*n 
        for i in range(1,n):
            fromLeft[i] =max(prices[i]-leftLow[i],fromLeft[i-1])
            fromRight[n-1-i]= max(rightHigh[n-1-i]-prices[n-i-1],fromRight[n-i])
        mxV = [0]*n
        for i in range(0,n):
            mxV[i] = fromLeft[i] + fromRight[i]
        print(leftLow)
        print(rightHigh)
        print(fromLeft)
        print(fromRight)
        return max (mxV)

print(Solution().maxProfit([1,2]))