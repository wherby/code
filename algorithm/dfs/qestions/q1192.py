# find bridge in graph
#https://leetcode.com/problems/critical-connections-in-a-network/
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
        self.bridge=[]
        self.tin = [-1]*self.V
        self.low = [-1]* self.V
        self.timer= 0
        
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u) # For the undirect graph
    
    def dfs(self,v,p=-1):
        self.visited[v] = 1
        self.tin[v] = self.low[v] = self.timer
        self.timer +=1
        
        for to in self.g[v]:
            if to == p : continue
            if self.visited[to]:
                self.low[v] =min(self.low[v],self.tin[to])
            else:
                self.dfs(to,v)
                self.low[v] = min(self.low[v],self.low[to])
                if self.low[to] > self.tin[v]:
                    self.bridge.append([v,to])
    
    def find_bridge(self):
        self.initSetting()
        for i in range(self.V):
            if  self.visited[i] ==0:
                self.dfs(i)
        return self.bridge

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        g=Graph(n)
        for a,b in connections:
            g.addEdge(a,b)
        re = g.find_bridge()
        return re
        
        
re =Solution().criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]])
print(re)