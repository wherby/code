class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1

class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        dsu = DSU(n+1)
        for k in range(threshold+1,n+1):
            for j in range(1,n//k+1):
                dsu.union(k,j*k)
                #print(k,k*j)
        res =[]
        for a,b in queries:
            res.append(dsu.find(a) == dsu.find(b))
        return res

re =Solution().areConnected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]])
            