############ ---- Input Functions ---- ############

class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        
def inp():
    return (int(input()))
def inlt():
    return (list(map(int,input().split())))
def insr():
    s = input()
    return (list(s[:len(s) ]))
def invr():
    return list((map(int,input().split())))

def resolve():
    n, = tuple(list(map(lambda x: int(x),input().split())))
    dsu= DSU(n*2)
    ls = insr()
    st =[]
    for i,a in enumerate(ls):
        if a ==("("):
            if i >0 and ls[i-1]==")":
                dsu.union(i,i-1)
            st.append(i)
        else:
            k = st.pop()
            dsu.union(i,k)
    cnt =0
    dic = {}
    for i in range(2*n):
        a = dsu.find(i)
        if a not in dic:
            dic[a] =1
            cnt +=1
    return cnt
    

def op(caseidx):
    ret= resolve()
    print(ret)
    

for i in range(int(input())):
    op(i)