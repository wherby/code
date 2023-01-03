import heapq
import math
class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """
        g = [[] for _ in range(n)]
        gr = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            gr[b].append((a,c))
        def dijkstra(g,start):
            dist = [math.inf] *n 
            dist[start] =0 
            used = set()
            q = [(0,start)]

            while q :
                _,u  = heapq.heappop(q) 
                if u in used: continue
                used.add(u)

                for (v,weight) in g[u]:
                    target = dist[u] + weight
                    if target < dist[v]:
                        dist[v] = target
                        heapq.heappush(q,(dist[v],v))
            return dist
        dist1,dist2,dist3 = dijkstra(g,src1),dijkstra(g,src2),dijkstra(gr,dest)
        ans = 10**20
        #print(dist1,dist2,dist3)
        for i  in range(n):
            ans = min(ans, dist1[i]+dist2[i] + dist3[i])
        return ans if ans< 10**20 else -1

re = Solution().minimumWeight(n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5)
print(re)