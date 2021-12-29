# 路径压缩不加上按秩合并，这样可以确保 最后一个合并的y是最终父节点。可以用来记录每个节点到父节点的层数

class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]

    def union(self,x,y):
        self.p[self.find(x)] =self.find(y)
