import heapq

def verify(sor,edges):
    g = [[] for _ in range(n)]
    for a,b,c in edges:
        g[a].append((b,c))
        g[b].append((a,c))
    st = [(0,sor)]
    visit = {}
    while st:
        c,d = heapq.heappop(st)
        if d in visit:continue
        visit[d] =c
        #if c > target: continue
        for b,c1 in g[d]:
            if b not in visit:
                heapq.heappush(st,(c+c1,b))
    return visit 