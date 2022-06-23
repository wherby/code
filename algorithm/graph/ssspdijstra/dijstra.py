import heapq

def dijstra(adj, src,dest):
    dist = [float('inf')] * n
    q = [(0, src)]
    dist[src] = 0
    while q:
        du, u =heapq.heappop(q)
        if u==dest:
            return du
        if du > dist[u]:
            continue
        for v, w in adj[u]:
            dv = du + w
            if dv < dist[v]:
                heapq.heappush(q, (dv, v))
                dist[v] = dv
    return -1

n = 1000