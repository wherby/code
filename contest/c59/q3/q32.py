from collections import defaultdict
import heapq
import math
class Solution:
    def countPaths(self, n, roads):
        graph = defaultdict(list)
        for road in roads:
            a,b,time = road
            graph[a].append([time,b])
            graph[b].append([time,a])
        
        def dijkstra(src):
            dist = [math.inf] *n
            ways = [0] *n
            minheap = [(0,src)]
            dist[src]=0
            ways[src] =1
            while minheap:
                d,u = heapq.heappop(minheap)
                if dist[u] <d: continue
                for time, v in graph[u]:
                    if dist[v] > dist[u] + time:
                        dist[v] = dist[u] + time
                        ways[v] = ways[u]
                        heapq.heappush(minheap,(dist[v],v))
                    elif dist[v] == dist[u] + time:
                        ways[v] += ways[u]
            return ways[n-1]
        return dijkstra(0) %(10 **9 +7)
