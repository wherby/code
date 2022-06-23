# Not verified
from collections import defaultdict, deque
class LCA:
    def __init__(self,root,g,edges={}):
        self.n = len(g)
        self.d =[0]*self.n
        self.g=g
        self.t = 10 # the 2**t layer depth of tree 
        self.f=[[0]*self.t for _ in range(self.n)]
        self.dist=defaultdict(int)
        self.edges =edges
        self.bfs(root)
        

    def bfs(self,root):
        st=deque([root])
        self.d[root] =1
        while st:
            x = st.popleft()
            for a in self.g[x]:
                if self.d[a]: continue
                self.d[a] = self.d[x] +1
                self.dist[a] = self.dist[x] + self.edges.get((x,a),1)
                self.f[a][0] = x
                for j in range(1,self.t):
                    self.f[a][j] = self.f[self.f[a][j-1]][j-1]
                st.append(a)
    
    def lca(self,x,y):
        if self.d[x]> self.d[y]:
            x,y = y,x
        for i in range(self.t-1,-1,-1):
            if self.d[self.f[y][i]] >=self.d[x]:
                y = self.f[y][i]
        if x == y:
            return x
        for i in range(self.t-1,-1,-1):
            if self.f[x][i] != self.f[y][i]:
                x = self.f[x][i]
                y = self.f[y][i]
        return self.f[x][0]
    
# algorithm\tree\lca\pic\tree.png tree graph
gf =[[1,2],[3,4],[5,6],[],[],[7],[],[]]
lca = LCA(0,gf)
print(lca.lca(3,4))
print(lca.lca(3,6))
print(lca.lca(3,7))
print(lca.lca(6,7))
print(lca.dist)