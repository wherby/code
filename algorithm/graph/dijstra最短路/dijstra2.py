#TDK dijstra  enqueue many time , may have time issue.
import heapq

class Dijstra(object):
    
    def __init__(self,n,graph):
        self.n = n 
        self.g = graph
        self.distance = [0]*n

    def traverse(self,node):
        visited = [0] *self.n
        
        hp = [(0,node)]
        while hp:
            c, node=heapq.heappop(hp)
            print(c,node)
            if visited[node]: continue
            self.distance[node] =c
            visited[node] =1
            for a,acost in self.g[node]:
                print(a,acost)
                if visited[a]: continue
                heapq.heappush(hp,(acost +c, a))  # This way will enqueue same node multiple time 

class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            a,b = a-1,b-1
            g[a].append([b,c])
            g[b].append([a,c])
        dj = Dijstra(n,g)
        dj.traverse(n-1)
        print(dj.distance)




re =Solution().countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])