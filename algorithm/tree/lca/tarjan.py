# ./pic/tarjan.png  tree: ./pic/tree.png
# Tarjan 的时候用dsu，不能用优化版本，因为需要得到值为1的父节点需要保持树的形状。
v =[0]*8
gf =[[1,2],[3,4],[5,6],[],[],[7],[],[]]
d = [0]*8

class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        self.p[y]= x
        # xr = self.find(x)
        # yr = self.find(y)
        # if self.rank[xr] <self.rank[yr]:
        #     xr,yr =yr,xr
        
        # self.p[yr] = xr
        # if self.rank[xr] == self.rank[yr]:
        #     self.rank[xr] += 1


dsu = DSU(8)

def tarjan(x):
    v[x] = 1
    for y in g[x]:
        if v[y]: continue
        d[y] = d[x] +1
        tarjan(y)
        dsu.union(x,y)
    for y,idx  in q[x]:
        if v[y] == 2:
            lca = dsu.find(y)
            ans[idx] = min(ans[idx],d[x]+ d[y] - 2 * d[lca])
            print(d[lca],a,d[x],d[y],lca)
    v[x] =2

#求 树上两点的距离
g = [[] for _ in range(8)]
for i in range(8):
    for a in gf[i]:
        g[i].append(a)
        g[a].append(i)
print(g)
queries = [[3,7],[4,6]]
q =[[] for i in range(8)]
ans = [100000] * len(queries)
for i in range(len(queries)):
    a,b = queries[i]
    print(i,a,b)
    q[a].append([b,i])
    q[b].append([a,i])

tarjan(0)
print(d)
print(ans)


