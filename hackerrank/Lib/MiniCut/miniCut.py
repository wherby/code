# Global Minimum Cut algorithm(Stoer-Wagner or Karger)
# https://www.hackerrank.com/contests/w37/challenges/two-efficient-teams/editorial

def addEdge(a,b,value):
    global g
    g[a][b] = value +g[a][b]
    g[b][a] = value +g[b][a]

def miniCut(g):
    n=len(g)
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
            #Updated the weight
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
        #print g
    return minCutValue


g = [[0, 8, 10, 0], [8, 0, 10, 10], [10, 10, 0, 10], [0, 10, 10, 0]]
print(miniCut(g))