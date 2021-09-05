#from one point  to other points in direct graph find most value.  dijkstra using priority queue


class Solution(object):
    def networkDelayTime(self, times, N, K):
        import heapq
        pq = []
        adj = [[] for _ in range(N+1)]
        for time in times:
            adj[time[0]].append((time[1], time[2]))

        fin, res = set(), 0
        heapq.heappush(pq, (0, K))

        while len(pq) and len(fin) != N:
            cur = heapq.heappop(pq)
            print cur
            fin.add(cur[1])
            res = cur[0]
            for child, t in adj[cur[1]]:
                if child in fin: continue
                heapq.heappush(pq, (t+cur[0], child))

        return res if len(fin) == N else -1



s = Solution()
times=[[2,1,1],[2,3,1],[3,4,1]]

print s.networkDelayTime(times,4,2)
