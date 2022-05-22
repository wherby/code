#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
import os
from re import L

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



from collections import deque
from math import inf
class HopcropfKarp:
    def __init__(self,m,n,g=None) -> None:
        self.NIL = 0
        self.m = m
        self.n = n 
        self.g = g 
        if g ==None:
            self.g = [[] for _ in range(m+1)]
        
    
    def resolve(self):
        self.pairU = [self.NIL]*(self.m+1)
        self.pairV = [self.NIL]*(self.n+1)
        self.dist = [inf]*(self.m+1)
        result = 0
        while self.bfs():
            for u in range(1,self.m+1):
                if self.pairU[u] ==self.NIL and self.dfs(u):
                    result+=1
        return result
        
    
    def addEdge(self,u,v):
        self.g[u].append(v)
        
    def bfs(self):
        dq = deque([])
        for u in range(1,self.m+1):
            if self.pairU[u] == self.NIL:
                self.dist[u] =0
                dq.append(u)
            else:
                self.dist[u] = inf
            self.dist[self.NIL]  = inf
            while dq:
                u = dq.popleft()
                if self.dist[u] < self.dist[self.NIL]:
                    for v in self.g[u]:
                        if self.dist[self.pairV[v]] == inf:
                            self.dist[self.pairV[v]] = self.dist[u]+1
                            dq.append(self.pairV[v])
        return self.dist[self.NIL] !=inf
    
    def dfs(self,u):
        if u !=self.NIL:
            for v in self.g[u]:
                if self.dist[self.pairV[v]] == self.dist[u]+1:
                    if self.dfs(self.pairV[v]) ==True:
                        self.pairV[v] =u
                        self.pairU[u] =v
                        return True
            self.dist[u] = inf
            return False
        return True

def resolve():
    n = int(input())
    ch =[]
    for i in range(n):
        ls = [int(x) for x in input().split(" ")]
        x,y = ls[0],ls[1]
        ch.append((x,y))
    Jerry = [int(x) for x in input().split(" ")]
    cd= []
    for i in range(n):
        ls = [int(x) for x in input().split(" ")]
        x,y = ls[0],ls[1]
        cd.append((x,y))
    g =[[] for _ in range(n+1)]
    gg =[[] for _ in range(n+1)]
    for i in range(n):
        ch1= ch[i]
        t1 = (ch1[0] - Jerry[0])**2 + (ch1[1]-Jerry[1])**2
        for j in range(n):
            cd1 = cd[j]
            cdt = (ch1[0]-cd1[0])**2 + (ch1[1]-cd1[1])**2
            if cdt <= t1:
                gg[i+1].append((cdt, j+1))
    #print(g)
    for i in range(len(gg)):
        g1 = gg[i]
        g1.sort()
        for d,a in g1:
            g[i].append(a)
    kn = HopcropfKarp(n,n,g)
    re= kn.resolve()
    if re != n:
        return []
    else:
        return kn.pairU
    

    

def op(caseidx):
    ret= resolve()
    if len(ret) ==0:
        print("Case #"+str(caseidx+1)+": IMPOSSIBLE" )
    else:
        print("Case #"+str(caseidx+1)+": POSSIBLE" )
        for i in range(1,len(ret)):
            print(str(i)+ " " + str(ret[i]+1))
    

for i in range(int(input())):
    op(i)