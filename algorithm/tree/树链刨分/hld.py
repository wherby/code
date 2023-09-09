#  https://oi-wiki.org/graph/hld/
# Not verifide 

class HLD:
    def __init__(self,g):
        n = len(g) +1
        self.hson = [-1]*n 
        self.deep = [0]*n 
        self.size = [0]*n 
        self.fa =[0] *n 
        self.top = [-1] *n
        self.dfn = [-1]*n
        self.rnk = [-1]*n
        self.g = g 
        self.cnt = 0
    
    def dfs1(self,o):
        self.hson[o] = -1 
        self.size[o] = 1 
        for j in self.g[o]:
            if self.deep[j] ==0:
                self.deep[j] = self.deep[o] +1 
                self.fa[j] = o 
                self.dfs1(j)
                self.size[o] += self.size[j]
                if self.hson[o] == -1 or (self.size[j] > self.size[self.hson[o]]):
                    self.hson[o] = j 
    
    def dfs2(self,o,t):
        self.top[o] = t 
        self.cnt +=1
        self.dfn[o] = self.cnt 
        self.rnk[self.cnt] = o 
        if self.hson[o] == -1: return
        self.dfs2(self.hson[o],t)
        for j in self.g[o]:
            if j != self.hson[o] and self.fa[o] != j:
                self.dfs2(j,j)


