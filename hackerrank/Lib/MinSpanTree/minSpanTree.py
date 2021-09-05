# min span tree which using multi seeds
def get(u):
    global col
    if col[u] == u:
        return u
    a = get(col[u])
    return a

def join(u,v):
    global col,rk
    u = get(u)
    v = get(v)
    if u == v:
        return False
    if rk[u] > rk[v]:
        u,v = v,u
    rk[v] = rk[u] + rk[v]
    col[u] = v
    return True

def minSpanTree(lines,n):
    global col,rk
    col = range(n)
    rk = [1]*n
    for line in lines:
        a,b = line
        print join(a,b)
    print rk,col


lines = [[0,1],[0,2],[1,2],[1,3],[2,3],[0,3]]
minSpanTree(lines,4)
lines = [[0,2],[1,2],[1,3],[2,3],[0,3]]
minSpanTree(lines,4)

col=[]
rk=[]
print rk,col