# Tarjan SSC 缩点　求出的不是SSC　algorithm\dfs\qestions\lcp54.py
# https://leetcode-cn.com/contest/season/2022-spring/ranking/solo/
# https://leetcode-cn.com/contest/season/2022-spring/problems/s5kipK/
# https://leetcode-cn.com/problems/s5kipK/
from collections import defaultdict
class Graph:
    def __init__(self, vertices,g=None):
        self.V= vertices #No. of vertices
        self.g = defaultdict(list) # default dictionary to store graph
        if g != None:
            self.V = len(g)
            self.g = g
        self.initSetting()

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u) # For the undirect graph
    
    def initSetting(self):
        self.dfn = [0]*self.V
        self.low = [0]* self.V
        self.dfc= 0
        self.stk=[]
        self.cnt=self.V-1
        self.T =[[] for _ in range(self.V<<1)]
    
    def tarjan(self,u):
        self.dfc +=1
        self.dfn[u] = self.low[u] = self.dfc
        self.stk.append(u)
        
        for v in self.g[u]:
            if not self.dfn[v]:
                self.tarjan(v)
                self.low[u]= min(self.low[u],self.low[v])
                if self.low[v] >= self.dfn[u]:
                    self.cnt +=1
                    self.T[self.cnt].clear()
                    x = 0
                    while x !=v:
                        x = self.stk[-1]
                        self.T[self.cnt].append(x)
                        self.T[x].append(self.cnt)
                        self.stk.pop()
                    self.T[self.cnt].append(u)
                    self.T[u].append(self.cnt)
            else:
                self.low[u] = min(self.low[u],self.dfn[v])
                


# Create a graph given in the above diagram
# 2===1===0===3===4
#  ======
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

# Create a graph given in the above diagram
# 2===1===4===3===0
#  ======
g = Graph(5)
g.addEdge(1, 4)
g.addEdge(4, 2)
g.addEdge(2, 1)
g.addEdge(4, 3)
g.addEdge(3, 0)

for i in range(5):
    if not g.dfn[i]:
        g.tarjan(i)
print(g.T)
print(g.cnt)
                    