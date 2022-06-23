from heapq import heappush, heappop
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
        def sssp(adj, src):
            dist = [float('inf')] * n
            q = [(0, src)]
            dist[src] = 0
            while q:
                du, u = heappop(q)
                if du > dist[u]:
                    continue
                for v, w in adj[u]:
                    dv = du + w
                    if dv < dist[v]:
                        heappush(q, (dv, v))
                        dist[v] = dv
            return dist

        adj = [[] for _ in range(n)]
        adjt = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adjt[v].append((u, w))
        a = sssp(adj, src1)
        b = sssp(adj, src2)
        c = sssp(adjt, dest)
        print(a,b,c)
        ans = min(a[i]+b[i]+c[i] for i in range(n))
        return ans if ans < float('inf') else -1

re =Solution().minimumWeight(8,[[4,7,24],[1,3,30],[4,0,31],[1,2,31],[1,5,18],[1,6,19],[4,6,25],[5,6,32],[0,6,50]],4,1,6)
print(re)
        