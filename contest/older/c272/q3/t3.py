class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        cnt =n
        state =0
        for i in range(1,n):
            if prices[i] == prices[i-1]-1:
                state +=1
            else:
                state = 0
            cnt +=state
        return cnt

re =Solution().getDescentPeriods(prices = [8,6,7,7])
print(re)