# https://wherby.github.io/code/graph/depth-first-search.html
class DFSWithOrder:
    def __init__(self,n,edges) -> None:
        self.color=[0]*n 
        self.timeIn=[0]*n
        self.timeOut =[0]*n
        self.timer =0
        self.adj=[[] for _ in range(n)]
        for a,b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        
    def dfs(self,v):
        self.color[v] = 1
        self.timeIn[v] = self.timer
        self.timer +=1
        for u in self.adj[v]:
            if self.color[u] ==0:
                self.dfs(u)
        self.color[v] = 2
        self.timeOut[v] = self.timer
        self.timer +=1
    
    def isSubChild(self,u,v):
        return self.timeIn[u] <self.timeIn[v] and self.timeOut[v] < self.timeOut[u]
    