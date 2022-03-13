# single source shortest path
https://leetcode-cn.com/contest/weekly-contest-284/problems/minimum-weighted-subgraph-with-the-required-paths/
多源路徑的最小值就是從源和目的地求到各點和的最小值
https://github.com/wherby/code/blob/master/contest/00000c275d69/c284/q4/t42.py

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

## dijstra

dijstra 就是單源的sssp

