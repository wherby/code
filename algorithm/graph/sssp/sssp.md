# single source shortest path
https://leetcode-cn.com/contest/weekly-contest-284/problems/minimum-weighted-subgraph-with-the-required-paths/
多源路徑的最小值就是從源和目的地求到各點和的最小值

def sssp(adj, src):
    dist = [float('inf')] * n
    q = [(0, src)]
    dist[src] = 0
    while q:
        du, u = heappop(q)
        if du > dist[u]:
            continue
        for v, w in adj[u]:
            dv = du + w
            if dv < dist[v]:
                heappush(q, (dv, v))
                dist[v] = dv
    return dist