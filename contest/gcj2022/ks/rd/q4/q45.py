#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/ts1_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

#import sys
#sys.setrecursionlimit(5000)

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
                for i in self.graph[a]:
                    if visited[i] ==False:
                        st.append(i)
        
        # visited[v]= True
        # tmp.append(v)
        # #Recur for all the vertices adjacent to this vertex
        # for i in self.graph[v]:
        #     if visited[i]==False:
        #         self.DFSUtil(i,visited,tmp)
  
    # First do a topological sorting of the graph.
    # dfs and store the visit exiting order in stack
    def fillOrder(self,v,visited, stack):
        st =[v]
        inOd={}
        rg ={}
        while st:
            a = st.pop()
            if visited[a] !=2:
                visited[a] =2
                cnt =0
                for i in self.graph[a]:
                    if visited[i] ==False:
                        visited[i] =1
                        cnt +=1
                        st.append(i)
                        rg[i] = a
                inOd[a] =cnt 
                while a in rg and inOd[a]==0 :
                    stack.append(a)
                    b = rg[a]
                    if b in inOd:
                        inOd[b] -=1
                    a=b
                
        
        # # Mark the current node as visited 
        # visited[v]= True
        # #Recur for all the vertices adjacent to this vertex
        # for i in self.graph[v]:
        #     if visited[i]==False:
        #         self.fillOrder(i, visited, stack)
        # stack.append(v)
        # print(stack)
  
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
    
    def getNewGraph(self,ssc):
        if len(ssc) ==0:
            dic ={}
            for i in range(self.V):
                dic[i] =i
            self.dic = dic
            self.w =[1]*self.V
            self.sw = [-1]*self.V
            return self
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



def dfs(x,newG):
    if newG.sw[x] != -1:
        return newG.sw[x]
    acc = newG.w[x]
    for a in newG.graph[x]:
        acc += dfs(a,newG)
    newG.sw[x] = acc
    return acc
    
        
def resolve(idx):
    n,m,k = tuple(list(map(lambda x: int(x),input().split())))
    g=[[] for _ in range(n)]
    for i in range(m):
        a,b =  tuple(list(map(lambda x: int(x),input().split())))
        g[b-1].append(a-1)
    g = Graph(n,g)
    newG = g.getNewGraph(g.getSSC())
    cnt = 0 
    if idx ==6:
        print(g.graph)
        print(g.getSSC())
    for i in range(n):
        p = newG.dic[i]
        a  = dfs(p,newG)
        if a >k :
            cnt +=1
    return cnt 

def op(caseidx):
    cnt =0
    #if caseidx ==6:
    cnt = resolve(caseidx)
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)