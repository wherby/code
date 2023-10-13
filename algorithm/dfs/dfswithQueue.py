#  https://cp-algorithms.com/graph/search-for-connected-components.html

def dfs(v,g):
    sst =[]
    sst.append(v)
    visit = {}
    while sst:
        curr = sst.pop()
        if curr not in visit:
            visit[curr] = True
            for b in g[v]:
                sst.append(b)

