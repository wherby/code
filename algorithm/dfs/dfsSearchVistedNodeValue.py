# https://leetcode-cn.com/contest/weekly-contest-266/problems/maximum-path-quality-of-a-graph/
#SPM dfs search visited node value. use visted number to calulate only once of dfs visited.

class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        n =len(values)
        g=[[] for i in range(n)]
        for e in edges:
            a,b,c= tuple(e)
            g[a].append([b,c])
            g[b].append([a,c])
        vist =[0]*n
        mxv =[0]
        def dfs(at,price,cost):
            if cost > maxTime:
                return
            vist[at] +=1
            if vist[at] == 1:
                price += values[at]
            if at == 0:
                mxv[0] = max(mxv[0],price)
            for i in  g[at]:
                dfs(i[0], price,cost +i[1])
            vist[at] -=1
        dfs(0,0,0)
        return mxv[0]