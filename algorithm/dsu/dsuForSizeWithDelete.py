#From https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1403930/Python-Union-Find-solution-explained
#https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/submissions/


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
        self.rank[xr] += self.rank[yr]
    # https://oi-wiki.org/ds/dsu/
    def erase(self,x):
        self.rank[self.find(x)] -=1
        self.p[x] =x 
    # x need to be leaf node
    def move(self,x,y):
        fx,fy = self.find(x), self.find(y)
        if fx == fy:
            return 
        self.p[x] = fy 
        self.rank[fx] -=1
        self.rank[fy] +=1

