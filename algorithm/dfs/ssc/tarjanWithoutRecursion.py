## https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76db9#analysis
## contest\gcj2022\ks\rd\q4\q44.py
class Graph:
   
    def __init__(self,vertices,g =None):
        self.V= vertices #No. of vertices
        self.graph =g if g!=None else  [[] for _ in range(self.V)] # default dictionary to store graph
   
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
   
    # A function used by DFS
    def DFSUtil(self,v,visited,tmp):
        # Mark the current node as visited and print it
        st =[v]
        while st:
            a = st.pop()
            if visited[a] == False:
                visited[a] =True
                tmp.append(a)
                tp =[]
                for i in self.graph[a]:
                    if visited[i] ==False:
                        tp.append(i)
                        #st.append(i)
                st.extend(tp[::-1])
        
        # visited[v]= True
        # tmp.append(v)
        # #Recur for all the vertices adjacent to this vertex
        # for i in self.graph[v]:
        #     if visited[i]==False:
        #         self.DFSUtil(i,visited,tmp)
  
    # First do a topological sorting of the graph.
    # dfs and store the visit exiting order in stack
    def fillOrder(self,v,visited, stack):
        # # Mark the current node as visited 
        # visited[v]= True
        # #Recur for all the vertices adjacent to this vertex
        # for i in self.graph[v]:
        #     if visited[i]==False:
        #         self.fillOrder(i, visited, stack)
        # stack.append(v)
        # #print(stack)
        
        st =[v]
        while st:
            a = st.pop()
            if visited[a] != 2:
                st.append(a)
                fd =False
                ## Here need to improve using "algorithm\graph\Hieholzer" to impove
                ## for example, the a could have n child, then will have O(n2) time to process 
                ## if record the index of a, then will goes to O(n) time 
                for i in self.graph[a]:
                    if visited[i] == False:  
                        visited[i] = 1
                        st.append(i)
                        fd =True
                        break
                        #st.append(i)
                if fd==False:
                    visited[a] =2
            else:
                stack.append(a)
                
        
        # # Mark the current node as visited 
        # visited[v]= True
        # #Recur for all the vertices adjacent to this vertex
        # for i in self.graph[v]:
        #     if visited[i]==False:
        #         self.fillOrder(i, visited, stack)
        # stack = stack.append(v)
      
  
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
                if stack ==None:
                    print(i,visited,stack,"aa")
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
    
    ## Transform the origin graph using SSC information 
    def getNewGraph(self,ssc):
        n = len(ssc)
        newG = Graph(n)
        newG.w =[0]*n
        newG.sw = [-1]*n
        dic = {}
        for i,sc in enumerate(ssc):
            for a in sc:
                dic[a] =i
            newG.w[i] = len(sc)
        for i in range(self.V):
            for j in self.graph[i]:
                if dic[i] != dic[j]:
                    newG.graph[dic[i]].append(dic[j])
        newG.dic =dic
        return newG     