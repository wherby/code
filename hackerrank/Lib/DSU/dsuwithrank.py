class DSU:
    def __init__(self, N):
        self.par = range(N)
        self.rank = [0]*N
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        rkx = self.rank[x]
        rky = self.rank[y]
        px = self.find(x)
        py = self.find(y)
        if rkx == rky:
            self.rank[x] = self.rank[x] +1
            self.par[px] =py
        elif rkx >rky:
            self.par[py] = px
        else:
            self.par[px] = py


dsu =DSU(10)
pairs = [(0,1),(2,3),(4,6),(1,3)]
for pair in pairs:
    a,b = pair
    dsu.union(a,b)
print dsu.par, dsu.rank
for i in range(10):
    print dsu.find(i)