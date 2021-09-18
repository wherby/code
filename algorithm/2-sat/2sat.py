#https://cp-algorithms.com/graph/2SAT.html
# 切分有向图的强联通区域
N =10000
used = [False] *N
g =[[1,2],[2,3]]
gv =[[1,2],[2,3]]
order =[]
comp = [-1]*N

def dfs1(v):
    used[v] = True
    for u in g[v]:
        if not used[u]:
            dfs1(u)
    order.push(v)

def dfs2(v,c1):
    comp[v] = c1
    for u in gv:
        if comp[u] == -1:
            dfs2(u,c1)


def solve_2Sat():
    order.clear()
    used = [False] *N
    for i in range(N):
        if not used[i]:
            dfs1(i)
    
    comp =[-1] *N
    j=0
    for i in range(N):
        v= order[n-i-1]
        if comp[v] == -1:
            dfs2(v, j)
            j+=1
    