# https://atcoder.jp/contests/abc373/submissions/58853021
# TLE

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin






from math import inf
from collections import defaultdict,deque
from heapq import heapify,heappop,heappush 
class Edge:
    def __init__(self, v, C, rev,cost):
        self.v = v
        self.C = C
        self.rev = rev
        self.cost = cost
 
    def __repr__(self) -> str:
        return "{ v: "+ str(self.v) + " cap: " +str( self.C) + " rev: " +str(self.rev) +" cost:  " + str(self.cost) +" } "
# Residual Graph
 
 
class MinCost:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]
        self.V = V
        self.dist = [inf for i in range(V)]
        self.vis = [False for _ in range(V)]
        self.ret =0
        self.dad = [(i,-1) for i in range(V)]
 
    # add edge to the graph
    def addEdge(self, u, v, C,cost):
 
        # Forward edge : 0 flow and C capacity
        a = Edge(v, C, len(self.adj[v]),cost)
 
        # Back edge : 0 flow and 0 capacity
        b = Edge(u,0, len(self.adj[u]),-cost)
        self.adj[u].append(a)
        self.adj[v].append(b)
 

    def spfa(self, s, t):
        for i in range(self.V):
            self.dist[i] = inf
        self.dist[s] = 0
        q = [(0,s)]
        visit ={}
        while q:
            c,u = heappop(q)
            if u in visit:
                continue
            visit[u] =1
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                if e.C >0 and self.dist[e.v] >self.dist[u] + e.cost :
                    self.dist[e.v] = self.dist[u] + e.cost
                    self.dad[e.v] = (u,i)
                    if e.v in visit:
                        del visit[e.v]  # Dijstr 在增广路径的时候有负边，需要更新visit
                    heappush(q,(self.dist[e.v],e.v))
        # If we can not reach to the sink we
        # return False else True
       #print(self.dist[t],inf,self.dist[t] == inf)
        return self.dist[t] != inf
 

    def dfs(self, s, t,flow):
        # Sink reached
        x = t 
        while x != s:
            flow = min(flow, self.adj[self.dad[x][0]][self.dad[x][1]].C)
            x = self.dad[x][0]
        x = t
        while x != s:
            ue = self.adj[self.dad[x][0]][self.dad[x][1]]
            ue.C -=flow
            self.ret += ue.cost * flow 
            self.adj[ue.v][ue.rev].C += flow
            x = self.dad[x][0]
        
        return flow
 
    # Returns maximum flow in graph
    def DinicMaxflow(self, s, t):
 
        self.ret = 0 
        ans = 0
        while(self.spfa(s,t)):
            x = self.dfs(s,t,inf)
            if x :
                ans += x 
        return [ans,self.ret]




N = int(input())
als,bls= [],[]
for _ in range(N):
    als.append(list(map(lambda x: int(x),input().split())))
for _ in range(N):
    bls.append(list(map(lambda x: int(x),input().split())))
ncg = MinCost(N*2 +2)
s = N*2
t = 2*N+1
C = 1.5*(10**12)
for i in range(N):
    ncg.addEdge(s,i,1,0)
    ncg.addEdge(i+N,t,1,0)
    for j in range(N):
        x1= ( (als[i][0] - bls[j][0]) **2 + (als[i][1]-bls[j][1])**2)**(1/2) 
        ncg.addEdge(i,j+N, 1, C*x1+0.5)
f,c = ncg.DinicMaxflow(s,t)
ret = [0]*N
for i in range(N):
    for e in ncg.adj[i]:
        if  N<=e.v <2*N and e.C ==0:
            ret[i] = e.v-N+1
print(" ".join([str(a) for a in ret]))  

