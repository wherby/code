from collections import defaultdict


            
class Solution(object):
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
    
    def findAllPeople(self, n, meetings, firstPerson):
        self.p  = list(range(n))
        self.rank = [1]*n
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        dsu =self
        dsu.union(0,firstPerson)
        dic =defaultdict(list)
        for a,b,t in meetings:
            dic[t].append([a,b])
        

                
        
        for t in sorted(dic.keys()):
            ls = dic[t]
            cand = set()
            for a,b in ls:
                cand.add(a)
                cand.add(b)
                dsu.union(a,b)
            for a in cand:
                if dsu.find(a) != dsu.find(0):
                    dsu.p[a] = a 
        ret =[]
        for i in range(n):
            if dsu.find(i) == dsu.find(0):
                ret.append(i)
        return ret
    
re =Solution().findAllPeople(6,[[0,2,1],[1,3,1],[4,5,1]],1)
print(re)