from collections import defaultdict


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
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        dsu  = DSU(n)
        dsu.union(0,firstPerson)
        dic =defaultdict(list)
        for a,b,t in meetings:
            dic[t].append([a,b])
        

                
        
        for t in sorted(dic.keys()):
            ls = dic[t]
            g = defaultdict(set)
            visit =[0]*n
            for a,b in ls:
                g[a].add(b)
                g[b].add(a)
            cand = []
            for a in g.keys():
                if dsu.find(a) ==dsu.find(0):
                    cand.append(a)
            visit ={}
            while cand:
                tmp =[]
                for a in cand:
                    if a not in visit:
                        visit[a] =1
                        for b in g[a]:
                            if dsu.find(b) != dsu.find(a):
                                tmp.append(b)
                                dsu.union(a,b)
                cand = tmp
        ret =[]
        for i in range(n):
            if dsu.find(i) == dsu.find(0):
                ret.append(i)
        return ret
    
re =Solution().findAllPeople(6,[[0,2,1],[1,3,1],[4,5,1]],1)
print(re)