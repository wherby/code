# https://leetcode.cn/contest/biweekly-contest-131/problems/block-placement-queries/


        
class DSU:
    def __init__(self,N,rk):
        self.p  = list(range(N))
        self.rank = rk
    
    def find(self,x):
        #print(x,self.p,self.rank)
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if xr < yr:   # 这里记录了range merge之后的右坐标,rank表示merge后span大小
            xr,yr =yr,xr
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]