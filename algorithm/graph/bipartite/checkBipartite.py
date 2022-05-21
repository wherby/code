from collections import deque
class BipartiteCheck:
    def __init__(self) -> None:
        pass
    
    def check(self,g):
        n = len(g)
        is_bipartite = True
        side = [-1]*n
        dq = deque([])
        for st in range(n):
            if side[st] == -1:
                dq.append(st)
                side[st] =0
                while dq:
                    v = dq.popleft()
                    for u in g[v]:
                        if side[u] ==-1:
                            side[u] = side[v] ^1
                            dq.append(u)
                        else:
                            is_bipartite &= side[u] !=side[v]
        return is_bipartite
    
# algorithm\graph\bipartite\pic\bipartite.drawio.png
# https://app.diagrams.net/#W32d4198629faf020%2F32D4198629FAF020!3354
g =[[],[4,6],[4,5],[4],[1,3],[2],[1]]
ck = BipartiteCheck()
print(ck.check(g))
g[1].append(2)
print(ck.check(g))
        