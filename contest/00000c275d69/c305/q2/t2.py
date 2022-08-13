class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        res = set(restricted)
        g = [[] for _ in range(n)]
        for a,b in edges:
            if a not in res and b not in res:
                g[a].append(b)
                g[b].append(a)
        visit =[0]*n
        def dfs(a):
            if visit[a] != 0 :
                return 0
            acc =1
            visit[a] =1 
            for x in g[a]:
                acc += dfs(x)
            return acc
        
        return dfs(0)





re =Solution().reachableNodes(n = 10, edges =[[8,2],[2,5],[5,0],[2,7],[1,7],[3,8],[0,4],[3,9],[1,6]], restricted = [9,8,4,5,3,1])
print(re)