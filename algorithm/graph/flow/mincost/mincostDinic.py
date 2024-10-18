# https://oi-wiki.org/graph/flow/min-cost/
# Will TLE https://atcoder.jp/contests/abc373/submissions/58848394


from math import inf
from collections import defaultdict,deque
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
        self.vis[s] =True
 
        q = deque([])
        q.append(s)
        while q:
            u = q.popleft()
            self.vis[u] = False
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                
                if e.C >0 and self.dist[e.v] >self.dist[u] + e.cost:
                    self.dist[e.v] = self.dist[u] + e.cost
                    if self.vis[e.v] == False:
                        q.append(e.v)
                        self.vis[e.v] = True
 
        # If we can not reach to the sink we
        # return False else True
       #print(self.dist[t],inf,self.dist[t] == inf)
        return self.dist[t] != inf
 

    def dfs(self, u, t,flow):
        # Sink reached
        if u == t:
            return flow
        self.vis[u] =True
        ans = 0 
        for i in range(len(self.adj[u])):
            e = self.adj[u][i]
            if self.vis[e.v] == False and e.C>0 and self.dist[e.v] == self.dist[u] + e.cost:
                x = self.dfs(e.v,t,min(e.C,flow -ans))
                if x:
                    self.ret +=x * e.cost
                    e.C -= x 
                    self.adj[e.v][e.rev].C += x 
                    ans  += x 
        self.vis[u] = False
        return ans
 
    # Returns maximum flow in graph
    def DinicMaxflow(self, s, t):
 
        self.ret = 0 
        ans = 0
        while(self.spfa(s,t)):
            x = self.dfs(s,t,inf)
            if x :
                ans += x 
        return [ans,self.ret]
    

# Driver Code
if __name__ == "__main__":
    s = 0
    t = 4
 
    cap = [ [ 0, 3, 1, 0, 3 ], 
            [ 0, 0, 2, 0, 0 ], 
            [ 0, 0, 0, 1, 6 ], 
            [ 0, 0, 0, 0, 2 ],
            [ 0, 0, 0, 0, 0 ] ]
 
    cost = [ [ 0, 1, 0, 0, 2 ], 
             [ 0, 0, 0, 3, 0 ], 
             [ 0, 0, 0, 0, 0 ], 
             [ 0, 0, 0, 0, 1 ],
             [ 0, 0, 0, 0, 0 ] ]
    g = MinCost(5)
    for i in range(5):
        for j in range(5):
            g.addEdge(i,j,cap[i][j],cost[i][j])
    ret = g.DinicMaxflow(0,4)
    print(ret)
 