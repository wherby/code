from collections import defaultdict
#https://cp-algorithms.com/graph/strongly-connected-components.html 
#This class represents a directed graph using adjacency list representation
#This type of SSC will not work for undirected graph.. So can't be used
class Graph:
   
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
   
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        #self.graph[v].append(u)
   
    # A function used by DFS
    def DFSUtil(self,v,visited,tmp):
        # Mark the current node as visited and print it
        visited[v]= True
        tmp.append(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited,tmp)
  
    # First do a topological sorting of the graph.
    # dfs and store the visit exiting order in stack
    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited 
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
      
  
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
  
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
  
   
   
    # The main function that finds and prints all strongly
    # connected components
    def getSSC(self):
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
  
        # Create a reversed graph
        gr = self.getTranspose()
           
         # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)

        ssc =[]
         # Now process all vertices in order defined by Stack
        while stack:
             i = stack.pop()
             if visited[i]==False:
                tmp=[]
                gr.DFSUtil(i, visited,tmp)
                ssc.append(tmp)
        return ssc

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
        ssc = g.getSSC()
        print(ssc)
        
re = Solution().minimumCost(cost = [1,2,3,4,5,6],roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]])