import heapq
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
        g,r = [[] for i in range(n)],[[] for _ in range(n)]
        for f,t,c in edges:
            g[f].append((t,c))
            r[t].append((f,c))
        def sssp(g,s):
            dist = [float('inf')]*n
            st =[(0,s)]
            dist[s] =0
            while st:
                c,f = heapq.heappop(st)
                if c > dist[f]: continue
                for t,c1  in g[f]:
                    if c + c1 < dist[t]:
                        heapq.heappush(st,(c+c1,t))
                        dist[t] = c+c1
            return dist
        a  = sssp(g,src1)
        b = sssp(g,src2)
        c = sssp(r,dest)
        cc =[a[i]+b[i] +c[i] for i in range(n) ]
        ans = min(cc)
        return -1 if ans >= float('inf') else ans