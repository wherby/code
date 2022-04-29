# 路径压缩，d为 奇偶性判断
# pic/questionForValuePath.png
# 也可以用扩展域解法 pic/扩展域解法.png
# d[x]记录x到已知根节点的距离，在find 时候更新根节点的父节点距离
# union(x,y,val): 表示从x到y的距离为val，在更新的时候更新d[x]为
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.d =[0]*N
    
    def find(self,x):
        if self.p[x] != x:
            fx = self.find(self.p[x])
            self.d[x] ^=self.d[self.p[x]]
            self.p[x] =fx
        return self.p[x]

    def union(self,x,y,val):
        self.p[x]=y
        self.d[x] = self.d[x] ^ self.d[y] ^ val 

dsu = DSU(100)
querys =[[1,3,1],[4,6,0],[1,6,0],[1,5,1]]  # question
n = len(querys)
for i in range(n):
    a,b,val = querys[i]
    a = a -1
    p,q  = dsu.find(a),dsu.find(b)
    if p == q:
        if dsu.d[a] ^ dsu.d[b] != val:
            print("find wrong answer :" , a+1,b,val , " at index :" ,i)
    else:
        dsu.union(a,b,val)
print("finished")
print(dsu.d)
