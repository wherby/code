import heapq
def sssp(adj, src):
    dist = [float('inf')] * n
    q = [(0, src)]
    dist[src] = 0
    while q:
        du, u = heapq.heappop(q)
        if du > dist[u]:
            continue
        for v, w in adj[u]:
            dv = du + w
            if dv < dist[v]:
                heapq.heappush(q, (dv, v))
                dist[v] = dv
    return dist