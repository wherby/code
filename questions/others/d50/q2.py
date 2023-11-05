class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        N= 503
        lls = [[] for _ in range(N+1)]
        for x,y in points:
            lls[x].append(y)
        res =[]
        for x,y,r in queries:
            m = max(x-r,0)
            mx = min(x+r,N)
            cnt =0
            for i in range(m,mx+1):
                for b in lls[i]:
                    if (x-i)**2 + (b-y)**2 <= r**2:
                        cnt+=1
            res.append(cnt)
        return res

re = Solution().countPoints(points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]])
print(re)