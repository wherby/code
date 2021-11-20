class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        N=401
        g = [[] for _ in range(N)]
        mx =[[0] *N for _ in range(N)]
        deg = [0]*N

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            mx[a][b] = 1
            mx[b][a] =1
            deg[a] +=1
            deg[b] +=1
        mn = 10**9
        for i in range(1,n+1):
            ls = g[i]
            m = len(ls)
            for l in range(m):
                for r in range(l+1,m):
                    a,b= ls[l],ls[r]
                    if mx[a][b] ==1:
                        mn = min( mn, deg[i] + deg[a] + deg[b] -6)
        return -1 if mn ==10**9 else mn

