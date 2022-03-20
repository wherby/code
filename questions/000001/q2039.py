from collections import deque

class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        n = len(patience)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        dist = [float("inf")] * n
        visit =[0]*n
        q = deque()
        q.append(0)
        dist[0] = 0
        visit[0] =1
        while q :
            head = q.popleft()
            for x in g[head]:
                if visit[x] ==0:
                    visit[x] =1
                    dist[x] = dist[head] +1
                    q.append(x)
        for i in range(n):
            dist[i] *=2
        patience[0] =1
        ret = [dist[i] + 1 if (dist[i]-1) // patience[i] ==0 else (dist[i]-1)//patience[i] * patience[i] + dist[i] +1 for i in range(n)]
        return max(ret)