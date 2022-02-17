from collections import defaultdict
class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        allC = 8 **k
        remains = 0
        dirs = [[2,1],[2,-1],[-2,-1],[-2,1],[1,2],[1,-2],[-1,-2],[-1,2]]
        dp0 = [[0]*n for _ in range(n)]
        dp0[row][column]  = 1
        while k >0:
            dp1 =  [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    z = dp0[i][j]
                    if z >0:
                        for d in dirs:
                            r1 = i + d[0]
                            c1 = j + d[1]
                            if r1 >=0 and r1 <n and c1 >=0 and c1 <n:
                                dp1[r1][c1] += z
            dp0 = dp1
            k -=1
        remains = sum(map(sum,dp0))
        res = remains *1.0 /allC
        
        res =format(res,'.4f')
        #print(res)
        return res

re = Solution().knightProbability(n = 1, k = 0, row = 0, column = 0) 
print(re)

            