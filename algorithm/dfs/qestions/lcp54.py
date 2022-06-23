#https://leetcode-cn.com/problems/s5kipK/ 
# https://leetcode-cn.com/contest/season/2022-spring/problems/EJvmW4/
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
        for i in range(n):
            if not g.dfn[i]:
                g.tarjan(i)
        if g.cnt == n:
            return min(cost)
        ww=[10**8 for _ in range(g.cnt+1)]
        deg =[0 for _ in range(g.cnt+1)]
        for i in range(g.cnt+1):
            deg[i] = len(g.T[i])
        print(deg,g.T)
        for i in range(n):
            if deg[i] ==1:
                for a in g.T[i]:
                    ww[a] = min(ww[a],cost[i])
                    deg[a] -=1
        mx,ans =0,0
        for i in range(n,g.cnt+1):
            if deg[i]==1:
                ans += ww[i]
                mx = max(mx,ww[i])
        print(deg,ww)
        return ans-mx
                    
        
re = Solution().minimumCost(cost = [1,2,3,4],roads = [[0,1],[0,2],[0,3]])
#re = Solution().minimumCost(cost = [1,2,3,4,5,6],roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]])
print(re)