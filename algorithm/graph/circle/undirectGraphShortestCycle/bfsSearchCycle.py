# https://leetcode.cn/circle/discuss/3Cqiwp/
# https://leetcode.cn/problems/shortest-cycle-in-a-graph/
from typing import List, Tuple, Optional
from collections import deque
from math import inf

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        def bfs(start: int) -> int:
            dis = [-1] * n  # dis[i] 表示从 start 到 i 的最短路长度
            dis[start] = 0
            q = deque([(start, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:  # 第一次遇到
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:  # 第二次遇到
                        # 由于是 BFS，后面不会遇到更短的环，直接返回
                        return dis[x] + dis[y] + 1
            return inf  # 该连通分量无环

        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1


