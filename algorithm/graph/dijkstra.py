# https://leetcode.cn/problems/minimum-weighted-subgraph-with-the-required-paths/solution/de-dao-yao-qiu-lu-jing-de-zui-xiao-dai-q-mj2c/
# questions/000001/q2203.py
import math
import heapq

def dijkstra(g,start):
    dist = [math.inf] *n 
    dist[start] =0 
    used = set()
    q = [(0,start)]

    while q :
        u,_  = heapq.heappop(q) 
        if u in used: continue
        used.add(u)

        for (v,weight) in g[u]:
            target = dist[u] + weight
            if target < dist[v]:
                dist[v] = target
                heapq.heappush(q,(dist[v],v))
    return dist

n = 1000
g = []