# 如果图中所有点都是偶数的度。则可以分解为一系列的欧拉回路。
# 如果图中的点有边都互相连接，且度都是偶数。则可以得到一条完整的欧拉回路
def euler_tour(n, m, us, vs):
    m = len(us)
    path = [[] for _ in range(n)]
    for edge_id in range(m):
        u = us[edge_id]
        v = vs[edge_id]
        path[u].append(edge_id)
        path[v].append(edge_id)
    vis = [0] * m

    ans = []
    
    for node in range(n):
        if path[node]:
            stack = [node]
            circle = [node]
            circle_rev = []
            while stack:
                u = stack.pop()
                if u < 0:
                    u = ~u
                    while circle[-1] != u:
                        circle_rev.append(circle.pop())
                while len(path[u]) and vis[path[u][-1]]:
                    path[u].pop()
                if len(path[u]):
                    stack.append(~u)
                    edge_id = path[u].pop()
                    vis[edge_id] = 1
                    a, b = us[edge_id], vs[edge_id]
                    if a == u: v = b
                    else: v = a
                    stack.append(v)
                    circle.append(v)

            circle.extend(reversed(circle_rev))
            ans.append(circle)
    
    return ans