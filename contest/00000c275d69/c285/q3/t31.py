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
        def getState(state):
            cnt = 0
            val =0
            for i in range(12):
                if (1<<i) & state:
                    cnt += lsW[i]
                    val +=i
            if cnt <= numArrows:
                return val
            return 0
        mx =0
        ans =0
        for state in range(1<<12):
            val  =getState(state)
            if val> mx:
                mx = val
                ans = state
        res = [0]*12
        for i in range(12):
            if (1<<i)& ans:
                res[i] = lsW[i]
        res[0] += numArrows -sum(res)
        return res

re =Solution().maximumBobPoints(75277,[0,1597,5395,15178,12621,6130,156,17588,2615,1832,6011,6154])
print(re)