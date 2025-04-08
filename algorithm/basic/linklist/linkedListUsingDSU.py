
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
        if xr == yr:
            return
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]

    def next(self,x):
        xp = self.find(x)
        return xp + self.rank[xp] 

dsu =DSU(1000)
dsu.union(1,2)
print(dsu.next(1))
print(dsu.next(2))