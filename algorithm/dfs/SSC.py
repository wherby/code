from collections import defaultdict
#https://cp-algorithms.com/graph/strongly-connected-components.html 
#This class represents a directed graph using adjacency list representation
class Graph:
   
    def __init__(self,vertices,g =None):
        self.V= vertices #No. of vertices
        self.graph =g if g!=None else  [[] for _ in range(self.V)] # default dictionary to store graph
   
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
   
    # A function used by DFS
    # Will [maximum recursion depth exceeded in comparison] when recursive call 
    # https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76db9#problem
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
        for i in range(self.V):
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
                

# Create a graph given in the above diagram
# 2===1===0===3===4
#  ======
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
  
   
print ("Following are strongly connected components " +
                           "in given graph")
re =g.getSSC()
print(re)
#This code is contributed by Neelam Yadav