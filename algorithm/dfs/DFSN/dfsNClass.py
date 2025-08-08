
class DFSTraverser:
    """
    一个用于执行深度优先搜索并记录欧拉环游路径的类。
    """
    def __init__(self, adjacency_list):
        self.n = len(adjacency_list)
        self.Vec = adjacency_list
        self.Fa = {} # 存储父节点
        self.T = [] # 存储遍历序列
        self.depth = 0
        self.L = [-1]*self.n 
        self.R = [-1]*self.n
        self.compute()
    
    def compute(self):
        self.dfs(0,-1)
        for i in range(self.depth ):
            
            if self.L[self.T[i]] == -1:
                self.L[self.T[i]] = i 
            self.R[self.T[i]] = i

    def dfs(self, z, fa):
        """
        递归执行深度优先搜索。
        :param z: 当前节点
        :param fa: 当前节点的父节点
        """
        
        self.T.append(z)
        self.depth += 1
        # 遍历当前节点的所有邻居
        for d in self.Vec[z]:
            if d == fa:
                continue
            
            self.Fa[d] = z
            self.dfs(d, z)
        self.T.append(z)
        self.depth += 1

if __name__=="__main__":
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]
    g = [[] for _ in range(len(edges) +1)]
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    dft = DFSTraverser(g)
    print(dft.T,dft.L,dft.R)