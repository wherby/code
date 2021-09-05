#DSU will fast merge all edges of tree and quickly detect circile when edges added.

class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

    def getpar(self):
        return self.par

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge


if __name__=="__main__":
    s=Solution()
    edges = [[1,2], [1,3], [2,3]]
    print s.findRedundantConnection(edges)
    dsu = DSU()
    for edge in edges:
        dsu.union(edge[0],edge[1])
    dsu.union(7,8)
    print dsu.getpar()[:10]
    print dsu.rnk[:10]
    dsu.union(1,7)
    print dsu.getpar()[:10]
    print dsu.rnk[:10]