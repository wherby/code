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
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        dsu = DSU(n)

        res =[]
        for a,b in requests:
            ap = dsu.find(a)
            bp = dsu.find(b)
            
            dic={ap:1,bp:1}
            isGood = True
            for x,y in restrictions:
                if dsu.find(x) == dsu.find(y) or (dsu.find(x) in dic and  dsu.find(y) in dic):
                    isGood =False
                    break
            if isGood == True:
                dsu.union(a,b)
            res.append(isGood)
        return res        