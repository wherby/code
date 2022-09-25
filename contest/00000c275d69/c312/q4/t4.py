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
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(vals)
        ret = len(vals)
        dic2 =defaultdict(list)
        for a,b in edges:
            dic2[max(vals[a],vals[b])].append([a,b])
        dir =[{} for _ in range(n)]
        dsu= DSU(n)
        keyOrd = sorted(dic2.keys())
        #print(dic2)
        for key in keyOrd:
            tmp =set()
            for a,b in dic2[key]:
                dsu.union(a,b)
                tmp.add(a)
                tmp.add(b)
            td = defaultdict(int)
            for a in tmp:
                if vals[a] ==key:
                    td[dsu.find(a)] +=1
            for k,v in td.items():
                ret += v*(v-1)//2
                #print(v,key,tmp)
        return ret
        





re =Solution().numberOfGoodPaths(vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]])
print(re)