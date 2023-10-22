#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/ready_go_part_2_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



from collections import defaultdict,deque
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
        self.rank[xr] += self.rank[yr]


def resolve():
    m,n = tuple(map(lambda x: int(x),input().split()))
    g = []
    for i in range(m):
        g.append(input())
    visit ={}
    def dfs(i,j):
        seeds=set()
        cand =[(i,j)]
        while cand:
            tmp = []
            #print(cand)
            for a,b in cand:
                if (a,b) not in visit:
                    visit[(a,b)] =1
                    for x,y in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                        if 0<=x<m and 0<=y<n:
                            if g[x][y]== "." :
                                seeds.add((x,y))
                            elif g[x][y] == "W" and dsu.find(x*n+y) != dsu.find(i*n+j):
                                tmp.append((x,y))
                                dsu.union(x*n+y,i*n+j)
                            else:
                                pass
            cand=tmp
        return seeds
    
    dsu =DSU(m*n)
    mx =0
    dic2 = defaultdict(int)
    for i in range(m):
        for j in range(n):
            if (i,j) not in visit and g[i][j] =="W":
                re= dfs(i,j)
                #print(re)
                if len(re) == 1:
                    #print(tuple(re))
                    #print(i,j,dsu.rank[dsu.find(i*n+j)],dsu.find(i*n+j))
                    dic2[tuple(re)] += dsu.rank[dsu.find(i*n+j)]
    #print(dic2.values())
    if len(dic2)>0:
        mx = max(dic2.values())
    return mx

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)