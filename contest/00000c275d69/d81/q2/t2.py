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
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dsu = DSU(n)
        for a,b in edges:
            dsu.union(a,b)
        cnt = 0
        ls = [0]*n
        for i in range(n):
            ls[dsu.find(i)]+=1
        for i in range(n):
            if ls[i] !=0:
                cnt +=(n-ls[i])*ls[i]
        
        return cnt//2
        
        
re = Solution().countPairs(n = 12, edges = [])

print(re)