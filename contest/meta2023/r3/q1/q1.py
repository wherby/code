# 
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/spooky_splits_input.txt"
#filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

FILEDEBUG=True

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f


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
        if xr == yr:
            return False
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]
        return True

def allCombination(ls,N):
    S = {tuple()}

    for x in ls:
        T = set()
        for a_tuple in S:
            a_list = list(a_tuple)
            for j in range(len(a_list)):
                b_list = list(a_list)
                b_list[j] += x 
                b_list.sort()

                if  b_list[-1]*len(b_list)<=N:
                    T.add(tuple(b_list))
            a_list.append(x)
            a_list.sort()
            if  a_list[-1]*len(a_list)<=N:
                T.add(tuple(a_list))
        S = T
    return S


def resolve():
    ret = []
    N,M= list(map(lambda x: int(x),input().split()))
    dsu =DSU(N)
    for _ in range(M):
        a,b = list(map(lambda x: int(x),input().split()))
        a,b = a-1,b-1
        dsu.union(a,b)
    visit ={}
    ls = []
    for i in range(N):
        a = dsu.find(i)
        if a not in visit:
            visit[a] = 1
            ls.append(dsu.rank[a])
    S = allCombination(ls,N)
    #print(ls,N,S)
    for i in range(1,N+1):
        if N%i == 0 and tuple([N//i] *i) in S:
            ret.append(i)

    return " ".join([str(a) for a in ret])
    

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)