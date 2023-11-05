import heapq
import math
class Dijstra(object):
    
    def __init__(self,n,graph):
        self.n = n 
        self.g = graph
        self.distance = [0]*n

    def traverse(self,node):
        distance = [math.inf]*self.n
        hp = [(0,node)]
        distance[node] = 0
        while hp:
            c, node=heapq.heappop(hp)
            if c > distance[node]: continue # The cost  is not the minimum cost. which means the node is visited
            self.distance[node] =distance[node]
            for a,acost in self.g[node]:
                newCost = acost + c
                if distance[a] > newCost:
                    distance[a] = newCost
                    heapq.heappush(hp,(newCost, a))
        
        



class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        mod = 10**9+7
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            a,b = a-1,b-1
            g[a].append([b,c])
            g[b].append([a,c])
        dj = Dijstra(n,g)
        dj.traverse(n-1)
        dist = dj.distance
        pathNum = [-1] *n
        def dfs(cur):
            if cur == n-1: return 1
            if pathNum[cur] != -1: return pathNum[cur]
            sm =0
            for next,c in g[cur]:
                if dist[next] >= dist[cur] : continue
                sm += dfs(next)
                sm %=mod
            pathNum[cur] = sm
            return sm
        return dfs(0)




re =Solution().countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])
print(re)