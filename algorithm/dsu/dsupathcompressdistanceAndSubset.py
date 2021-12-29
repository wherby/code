# 路径压缩不加上按秩合并，这样可以确保 最后一个合并的y是最终父节点。可以用来记录每个节点到父节点的层数

class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
        self.d =[0]*N
    
    def find(self,x):
        if self.p[x] != x:
            fx = self.find(self.p[x])
            self.d[x] +=self.d[self.p[x]]
            self.p[x] =fx
        return self.p[x]

    def union(self,x,y):
        m = self.find(x)
        n = self.find(y)

        self.p[m] =n
        self.d[m] = self.rank[n]
        self.rank[n] += self.rank[m]


dsu  = DSU(100)
dsu.union(98,92)
dsu.union(92,93)
dsu.union(93,91)
#dsu.union(93,0)  # comment out the line to see behavior
print(dsu.find(93),dsu.find(94),dsu.find(98))
print(dsu.d)
for i in range(100):
    dsu.find(i)
print(dsu.d)
for i in range(100):
    dsu.find(i)
print(dsu.d)
for i in range(100):
    dsu.find(i)
print(dsu.d)
print(dsu.p)
print(dsu.rank)