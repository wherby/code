# https://codeforces.com/gym/106404/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0305/solution/cf106404h.md
# 求路径通过的最早时间也是用最短路的思维得到
# 然后用最短路计算得到最终通过时间
# 多源dijstra求得每个点的最早通过时间，单源dijkstra求得每个点的最短路径长度，比较两者得到结果
# pq = [nums[i] * n + i for i in range(n)] 这里不heapify 并不会影响结果，因为是多源的dijkstra，初始状态下每个点的距离都是独立的，所以不需要heapify，后续更新的时候会自动调整pq的顺序


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    inf = 11 * 10 ** 8
    
    for _ in range(t):
        n, m = MII()
        nums = LII()
        
        path = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v, w = MII()
            u -= 1
            v -= 1
            path[u].append(w * n + v)
            path[v].append(w * n + u)
        
        pq = [nums[i] * n + i for i in range(n)]
        
        while pq:
            d, u = divmod(heappop(pq), n)
            if nums[u] == d:
                for msk in path[u]:
                    nd, v = divmod(msk, n)
                    if nd + d < nums[v]:
                        nums[v] = nd + d
                        heappush(pq, nums[v] * n + v)
        
        dis = [inf] * n
        dis[0] = 0
        
        pq = [0]
        
        while pq:
            d, u = divmod(heappop(pq), n)
            if dis[u] == d:
                for msk in path[u]:
                    nd, v = divmod(msk, n)
                    if nd + d < dis[v] and nd + d <= nums[v]:
                        dis[v] = nd + d
                        heappush(pq, dis[v] * n + v)
        
        outs.append('YES' if dis[n - 1] < inf else 'NO')
    
    print('\n'.join(outs))

if __name__ == "__main__": 
    main()