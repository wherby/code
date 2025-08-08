# 这里的DFSN,在T中叶子节点只有一个值

def getDFSOrder(g):
    depth = 0
    n = len(g)
    T = [-1] *(2*n)
    L = [-1]*n 
    R = [-1]*n 
    Fa = [-1]*n 

    def dfs0(z,fa):
        nonlocal depth
        T[depth] =z 
        depth +=1
        for d in g[z]:
            if d == fa:
                continue
            Fa[d] = z 
            dfs0(d,z)
        T[depth] = z 
        depth +=1
    dfs0(0,-1)

    for i in range(depth ):
        if L[T[i]] == -1:
            L[T[i]] = i 
        R[T[i]] = i
    return T,L,R



if __name__=="__main__":
    edges = [[0,1],[1,2],[0,3]]
    g = [[] for _ in range(4)]
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    T,L,R = getDFSOrder(g)
    print(T,L,R)
