# Euler Tour（欧拉序）。它的核心作用是 记录每个节点的访问顺序，并 在回溯时再次记录父节点，从而构建一个 线性序列，用于后续的树查询操作（如子树查询、路径查询、LCA 等）。
def euler_tour(root, adj):
    n = len(adj)
    in_time = [0] * n  # 进入时间
    out_time = [0] * n  # 离开时间
    time = 0
    tour = []  # 欧拉序序列

    def dfs(u, parent):
        nonlocal time
        in_time[u] = time  # 记录进入时间
        time +=1
        tour.append(u)     # 进入节点 u
        for v in adj[u]:
            if v != parent:
                dfs(v, u)
                tour.append(u)  # 回溯时再次记录 u
                time +=1
        out_time[u] = time - 1  # 离开时间（可选，取决于需求）

    dfs(root, -1)
    return tour, in_time, out_time

if __name__=="__main__":
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]
    g = [[] for _ in range(len(edges) +1)]
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    T,L,R = euler_tour(0,g)
    print(T,L,R)