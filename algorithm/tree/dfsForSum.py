def test(n):
    count = []*n
    def dfs(s,e):
        count[s] =1
        for u in adj[s]:
            if u == e: continue
            dfs(u,s)
            count[s] += count[u]


# page 145 https://usaco.guide/CPH.pdf#page=75
