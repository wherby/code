class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        n = len(values)
        g = [[] for _ in range(n)]
        for a,b,v in edges:
            g[a].append((b,v))
            g[b].append((a,v))
        mx =0
        visited = [0]*n
        visited[0] = 1
        def dfs(p,acc,time):
            nonlocal mx
            if p ==0:
                mx = max(mx,acc)
            for b,c in g[p]:
                if visited[b] == 0 and c <=time:
                    visited[b] =1
                    #print(b,acc +values[b],acc,time-c)
                    dfs(b,acc + values[b],time -c)
                    visited[b] =0
                elif c <= time:
                    dfs(b,acc,time-c)
        dfs(0,values[0],maxTime)
        return mx

        


re =Solution().maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50)
print(re)