# https://cp-algorithms.com/graph/cutpoints.html

from collections import defaultdict
class Graph:
    def __init__(self, vertices,g=None):
        self.V= vertices #No. of vertices
        self.g = defaultdict(list) # default dictionary to store graph
        if g != None:
            self.V = len(g)
            self.g = g
        self.initSetting()
    
    def initSetting(self):
        self.visited=[0]*self.V
        self.acticulationPoint=[]
        self.tin = [-1]*self.V
        self.low = [-1]* self.V
        self.timer= 0
        
    # function to add an edge to graph 
    def addEdge(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u)# For the undirect graph
    
    def dfs(self,v,p=-1):
        self.visited[v] = 1
        self.tin[v] = self.low[v] = self.timer
        self.timer +=1
        children =0
        
        for to in self.g[v]:
            if to == p : continue
            if self.visited[to]:
                self.low[v] =min(self.low[v],self.tin[to])
            else:
                self.dfs(to,v)
                self.low[v] = min(self.low[v],self.low[to])
                if self.low[to] >= self.tin[v] and p !=-1:
                    self.acticulationPoint.append(v)
                children +=1
        if p ==-1 and children >1:
            self.acticulationPoint.append(v)
    
    def find_cutpoints(self):
        self.initSetting()
        for i in range(self.V):
            if  self.visited[i] ==0:
                self.dfs(i)
        return self.acticulationPoint

# Create a graph given in the above diagram
# 2===1===0===3===4
#  ======
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

points = g.find_cutpoints()
print(points)
   
# Create a graph given in the above diagram
# 2===1===4===3===0
#  ======
g = Graph(5)
g.addEdge(1, 4)
g.addEdge(4, 2)
g.addEdge(2, 1)
g.addEdge(4, 3)
g.addEdge(3, 0)

points = g.find_cutpoints()
print(points)