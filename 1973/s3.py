class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])
        if m ==1:
            return max(points[0])
        if n == 1:
            return sum(sum(x) for x in points)
        
        def left(lst):
            res = [0]*len(lst)
            res[0]= lst[0]
            for i in range(1,len(lst)):
                res[i] = max(lst[i], res[i-1] -1)
            return res
        
        def right(lst):
            res = [0]* len(lst)
            res[len(lst)-1] = lst[len(lst)-1]
            for i in  range(n-2,-1,-1):
                res[i] = max(lst[i], res[i+1]-1)
            return res

        dp= points[0]
        for i in range(1,m):
            lft = left(dp)
            rt =right(dp)
            for j in range(n):
                dp[j] = points[i][j] + max(lft[j],rt[j])
            #print(dp)
        return max(dp)

        


points = [[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]
a= Solution().maxPoints(points)
print(a)