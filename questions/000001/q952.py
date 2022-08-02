from itertools import pairwise
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
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =len(nums)
        dsu = DSU(n)
        def get_prime(n):
            visited=[0]*(n+2)
            res =[]
            for i in range(2,n+1):
                if visited[i]: continue
                res.append(i)
                for j in range(i,n+1,i):
                    visited[j] =1
            return res
        re =get_prime(1000)
        dic = defaultdict(set)
        for i,a in enumerate(nums):
            for p in re:
                while a %p ==0:
                    dic[p].add(i)
                    a = a //p 
            if a !=1:
                dic[a].add(i)
        for k, v in dic.items():
            ls = list(v)
            for a,b in pairwise(ls):
                if dsu.find(a)!= dsu.find(b):
                    dsu.union(a,b)
        ls =[0]*n 
        #print(dic)
        for i in range(n):
            ls[dsu.find(i)] +=1
        return max(ls)
        
re = Solution().largestComponentSize([20,50,9,63])
print(re)