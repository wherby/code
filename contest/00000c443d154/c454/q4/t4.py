# https://leetcode.cn/contest/weekly-contest-454/problems/find-weighted-median-node-in-tree/description/
from typing import List, Tuple, Optional
from collections import defaultdict, deque
class LCA:
    def __init__(self,root,g,edges={}):
        self.n = len(g)
        self.d =[0]*self.n
        self.g=g
        self.t = 20 # the 2**t layer depth of tree 
        self.f=[[0]*self.t for _ in range(self.n)]  # node number ==0 is for vitual node link
        self.dist=defaultdict(int)
        self.edges =edges
        self.bfs(root)
        

    def bfs(self,root):
        st=deque([root])
        self.d[root] =1
        while st:
            x = st.popleft()
            for a in self.g[x]:
                if self.d[a]: continue
                self.d[a] = self.d[x] +1
                self.dist[a] = self.dist[x] + self.edges.get((x,a),1)
                self.f[a][0] = x
                for j in range(1,self.t):
                    self.f[a][j] = self.f[self.f[a][j-1]][j-1]
                st.append(a)
    
    def lca(self,x,y):
        if self.d[x]> self.d[y]:
            x,y = y,x
        for i in range(self.t-1,-1,-1):
            if self.d[self.f[y][i]] >=self.d[x]:
                y = self.f[y][i]
        if x == y:
            return x
        for i in range(self.t-1,-1,-1):
            if self.f[x][i] != self.f[y][i]:
                x = self.f[x][i]
                y = self.f[y][i]
        return self.f[x][0]
    
    def goUp(self,x,wayToGo):
        for i in range(self.t-1,-1,-1):
            if self.dist[x] - self.dist[self.f[x][i]] < wayToGo and self.f[x][i] != x:
                return self.goUp(self.f[x][i],wayToGo -(self.dist[x] - self.dist[self.f[x][i]]))
        return x


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        gedg = {}
        for a,b,c in edges:
            g[a].append(b)
            g[b].append(a)
            gedg[(a,b)] = c 
            gedg[(b,a)] =c 
        lca = LCA(0,g,gedg)
        ret = []
        for a,b in queries:
            if a ==b:
                ret.append(a)
                continue
            c = lca.lca(a,b)
            s1 = lca.dist[a] - lca.dist[c]
            s2 = lca.dist[b] - lca.dist[c]
            #print(s1,s2)
            if s1*2 >= s1+s2:
                t = lca.goUp(a,(s1+s2+1)//2)
                ret.append(lca.f[t][0])
            else:
                #print("a",b,(s1+s2)//2+1)
                t = lca.goUp(b,(s1+s2)//2+1)
                ret.append(t)
        return ret