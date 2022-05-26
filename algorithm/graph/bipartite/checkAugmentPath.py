# https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b158f8
# 用dfs检查增广路径方法来判定全匹配， 如果需要对每个路径做当前最优选择，则需要对每个点选取对应的增广路径
# 


class BipartileWithPriority:
    def __init__(self,m,n,g):
        self.used=[0]*(m+1)
        self.mt =[-1]*(n+1)
        self.g = g
    
    def dfs(self,x):
        if self.used[x]: return False
        self.used[x] = 1
        for y in self.g[x]:
            if self.mt[y] ==-1:
                self.mt[y] = x
                return True
        for y in self.g[x]:
            if self.dfs(self.mt[y]):
                self.mt[y] = x 
                return True
        return False