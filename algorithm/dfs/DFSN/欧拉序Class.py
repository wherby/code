# Euler Tour（欧拉序）。它的核心作用是 记录每个节点的访问顺序，并 在回溯时再次记录父节点，从而构建一个 线性序列，用于后续的树查询操作（如子树查询、路径查询、LCA 等）。
class EulerTour:
    def __init__(self,  adj):
        self.n =n= len(adj)
        self.adj = adj
        self.in_time = [0] * n  
        self.out_time = [0] * n
        self.time = 0
        self.tour = [] 
        self.Fa = [-1]*n        
        

    def run(self, root):
        self._dfs(root, -1)
        return self.tour, self.in_time, self.out_time

    def _dfs(self, u, parent):
        self.in_time[u] = self.time
        self.time += 1
        self.tour.append(u)
        
        for v in self.adj[u]:
            if v != parent:
                self.Fa[v]=u
                self._dfs(v, u)
                self.tour.append(u)
                self.time += 1
        
        self.out_time[u] = self.time - 1

if __name__=="__main__":
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]
    g = [[] for _ in range(len(edges) +1)]
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    et = EulerTour(g)
    T,L,R = et.run(0)
    print(T,L,R)
    print(et.Fa)