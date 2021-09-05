filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


n,m = map(int , ins[0].strip().split())
g=[]
for i in range(n):
    g.append([0]*n)


def addEdge(a,b,value):
    global g
    g[a][b] = value +g[a][b]
    g[b][a] = value +g[b][a]

def miniCut(g):
    global n
    used =[0] *n
    dist = [0] *n
    vertices = []
    MAXV = 100000000000
    for i in range(n):
        vertices.append(i)
    minCutValue = MAXV
    while len(vertices) >1:
        u = vertices[0]
        for v in vertices:
            used[v] = False
            dist[v] = g[u][v]
        used[u] = True
        for i in range(len(vertices) -2):
            for  v in vertices:
                if used[v] == False:
                    if used[u] == True or dist[v] > dist[u]:
                        u =v
            used[u] = True
            for v in vertices:
                if used[v] == False:
                    dist[v] = dist[v] + g[u][v]
        t = -1
        for v in vertices:
            if used[v] != True:
                t = v
        minCutValue = min(minCutValue, dist[t])
        vertices.remove(t)
        for v in vertices:
            addEdge(u,v, g[v][t])
    return minCutValue




index=1
total = 0
for i in range(m):
    ls1= list(map(int , ins[index+i*2].strip().split()))
    ls2= list(map(int , ins[index+i*2 +1].strip().split()))
    total = total + ls1[1] *2
    if ls1[0] ==2:
        a = ls2[0] -1
        b = ls2[1] -1
        addEdge( a, b, ls1[1]*2)
    else:
        a = ls2[0] -1
        b = ls2[1] -1
        c = ls2[2] -1
        value = ls1[1]
        addEdge( a,b, value)
        addEdge(a,c, value)
        addEdge(b,c, value)
print(g)
minCutValue = miniCut(g)
print( int(total- minCutValue)//2)
