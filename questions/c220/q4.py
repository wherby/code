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
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        eg =[]
        for a,b,c in edgeList:
            eg.append((c,a,b))
        n1 = len(eg)
        eg.sort()
        q =[]
        for i,(a,b,c) in enumerate(queries):
            q.append((c,a,b,i))
        q.sort()
        m = len(q)
        res = [0]*m
        dsu = DSU(n)
        idx =0
        for i in range(m):
            c,a,b,i2 =q[i]
            while idx < n1 and eg[idx][0]<c:
                _,a1,b1 = eg[idx]
                idx+=1
                dsu.union(a1,b1)
            if dsu.find(a) != dsu.find(b):
                res[i2]=False
            else:
                res[i2] = True
        return res




re = Solution().distanceLimitedPathsExist(n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]])
print(re)