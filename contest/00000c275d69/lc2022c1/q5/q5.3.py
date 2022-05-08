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
    
class Solution(object):
    def minimumCost(self, cost, roads):
        """
        :type cost: List[int]
        :type roads: List[List[int]]
        :rtype: int
        """
        n = len(cost)
        g = Graph(n)
        for a,b in roads:
            g.addEdge(a,b)
        ssc = g.find_cutpoints()
        print(ssc)

re = Solution().minimumCost(cost = [1,2,3,4],roads = [[0,1],[0,2],[0,3]])     
#https://cp-wiki.vercel.app/tutorial/leetcode/2022-spring-solo/#problem-e-%E5%A4%BA%E5%9B%9E%E6%8D%AE%E7%82%B9 
#re = Solution().minimumCost(cost = [1,2,3,4,5,6],roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]])