# Using Tarjan will have same issue of [maximum recursion depth exceeded in comparison]
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




    
        
def resolve(idx):
    n,m,k = tuple(list(map(lambda x: int(x),input().split())))
    g=[[] for _ in range(n)]
    for i in range(m):
        a,b =  tuple(list(map(lambda x: int(x),input().split())))
        g[b-1].append(a-1)
    if idx !=6:
        return 0
    g = Graph(n,g)
    for i in range(n):
        g.tarjan(i)
    #print(g.T)
    return 0

def op(caseidx):
    cnt =0
    #if caseidx ==6:
    cnt = resolve(caseidx)
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)