
import heapq
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
        m = len(queries)
        qls = []
        for i,(a,b,c) in enumerate(queries):
            qls.append([c,a,b,i])
        qls.sort()
        st = []
        for a,b,c in edgeList:
            heapq.heappush(st,(c,a,b))
        ret = [False ]*m
        dsu = DSU(n)
        for i in range(m):
            c,a,b,j = qls[i]
            while st and st[0][0] < c :
                #print(st[0][0],c,st)
                c1,a1,b1 = heapq.heappop(st)
                #print(a,b,c,c1)
                dsu.union(a1,b1)
            #print(c,dsu.find(a) ,dsu.find(b),a,b)
            if dsu.find(a) == dsu.find(b):
                ret[j] = True
        return ret

re = Solution().distanceLimitedPathsExist(5,[[0,1,10],[1,2,5],[2,3,9],[3,4,13]],[[0,4,14],[1,4,13]])
print(re)