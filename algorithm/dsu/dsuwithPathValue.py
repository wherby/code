# ./pic/dsuwithvalue.png
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.d =[0]*N
        self.size=[1]*N
    
    def find(self,x):
        if self.p[x] != x:
            root  =self.find(self.p[x])
            self.d[x] += self.d[self.p[x]]
            self.p[x] = root
        return self.p[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        self.p[px] =py
        self.d[px] = self.size[py]
        self.size[py] += self.size[px]

dsu = DSU(8)
#0<-2<-1<-3<-4<-5<-6<-7 雖然 union(1,0) 但是2已經在0集合裏面，所以會把1放在後面形成一個鏈條
dsu.union(2,0)
dsu.union(1,0)
dsu.union(6,5)
dsu.union(7,6)
dsu.union(3,1)
dsu.union(4,1)
dsu.union(5,4)

print(dsu.d,dsu.p,dsu.size)
for i in range(8):
    dsu.find(i)
print(dsu.d,dsu.p,dsu.size)
for i in range(8):
    dsu.find(i)
print(dsu.d,dsu.p,dsu.size)
for i in range(8):
    dsu.find(i)
print(dsu.d,dsu.p,dsu.size)