# https://leetcode.cn/contest/weekly-contest-318/ranking/1/   @草莓奶昔
from typing import List, Tuple, Optional
from collections import defaultdict, Counter, deque
from sortedcontainers import SortedList

MOD = int(1e9 + 7)
INF = int(1e18)

# X 轴上有一些机器人和工厂。给你一个整数数组 robot ，其中 robot[i] 是第 i 个机器人的位置。再给你一个二维整数数组 factory ，其中 factory[j] = [positionj, limitj] ，表示第 j 个工厂的位置在 positionj ，且第 j 个工厂最多可以修理 limitj 个机器人。

# 每个机器人所在的位置 互不相同 。每个工厂所在的位置也 互不相同 。注意一个机器人可能一开始跟一个工厂在 相同的位置 。

# 所有机器人一开始都是坏的，他们会沿着设定的方向一直移动。设定的方向要么是 X 轴的正方向，要么是 X 轴的负方向。当一个机器人经过一个没达到上限的工厂时，这个工厂会维修这个机器人，且机器人停止移动。

# 任何时刻，你都可以设置 部分 机器人的移动方向。你的目标是最小化所有机器人总的移动距离。

# 请你返回所有机器人移动的最小总距离。测试数据保证所有机器人都可以被维修。

# 注意：

# 所有机器人移动速度相同。
# 如果两个机器人移动方向相同，它们永远不会碰撞。
# 如果两个机器人迎面相遇，它们也不会碰撞，它们彼此之间会擦肩而过。
# 如果一个机器人经过了一个已经达到上限的工厂，机器人会当作工厂不存在，继续移动。
# 机器人从位置 x 到位置 y 的移动距离为 |y - x| 。


class Edge:
    __slots__ = ("fromV", "toV", "cap", "cost", "flow")

    def __init__(self, fromV: int, toV: int, cap: int, cost: int, flow: int) -> None:
        self.fromV = fromV
        self.toV = toV
        self.cap = cap
        self.cost = cost
        self.flow = flow


class MinCostMaxFlow:
    """最小费用流的连续最短路算法复杂度为流量*最短路算法复杂度"""

    __slots__ = ("_n", "_start", "_end", "_edges", "_reGraph", "_dist", "_visited", "_curEdges")

    def __init__(self, n: int, start: int, end: int):
        """
        Args:
            n (int): 包含虚拟点在内的总点数
            start (int): (虚拟)源点
            end (int): (虚拟)汇点
        """
        assert 0 <= start < n and 0 <= end < n
        self._n = n
        self._start = start
        self._end = end
        self._edges: List["Edge"] = []
        self._reGraph: List[List[int]] = [[] for _ in range(n + 10)]  # 残量图存储的是边的下标

        self._dist = [INF] * (n + 10)
        self._visited = [False] * (n + 10)
        self._curEdges = [0] * (n + 10)

    def addEdge(self, fromV: int, toV: int, cap: int, cost: int) -> None:
        """原边索引为i 反向边索引为i^1"""
        self._edges.append(Edge(fromV, toV, cap, cost, 0))
        self._edges.append(Edge(toV, fromV, 0, -cost, 0))
        len_ = len(self._edges)
        self._reGraph[fromV].append(len_ - 2)
        self._reGraph[toV].append(len_ - 1)

    def work(self) -> Tuple[int, int]:
        """
        Returns:
            Tuple[int, int]: [最大流,最小费用]
        """
        maxFlow, minCost = 0, 0
        while self._spfa():
            # !如果流量限定为1，那么一次dfs只会找到一条费用最小的增广流
            # !如果流量限定为INF，那么一次dfs不只会找到一条费用最小的增广流
            flow = self._dfs(self._start, self._end, INF)
            maxFlow += flow
            minCost += flow * self._dist[self._end]
        return maxFlow, minCost

    def slope(self) -> List[Tuple[int, int]]:
        """
        Returns:
            List[Tuple[int, int]]: 流量为a时,最小费用是b
        """
        res = [(0, 0)]
        flow, cost = 0, 0
        while self._spfa():
            deltaFlow = self._dfs(self._start, self._end, INF)
            flow += deltaFlow
            cost += deltaFlow * self._dist[self._end]
            res.append((flow, cost))  # type: ignore
        return res

    def _spfa(self) -> bool:
        """spfa沿着最短路寻找增广路径  有负cost的边不能用dijkstra"""
        n, start, end, edges, reGraph, visited = (
            self._n,
            self._start,
            self._end,
            self._edges,
            self._reGraph,
            self._visited,
        )

        self._curEdges = [0] * n
        self._dist = dist = [INF] * n
        dist[start] = 0
        queue = deque([start])

        while queue:
            cur = queue.popleft()
            visited[cur] = False
            for edgeIndex in reGraph[cur]:
                edge = edges[edgeIndex]
                cost, remain, next = edge.cost, edge.cap - edge.flow, edge.toV
                if remain > 0 and dist[cur] + cost < dist[next]:
                    dist[next] = dist[cur] + cost
                    if not visited[next]:
                        visited[next] = True
                        if queue and dist[queue[0]] > dist[next]:
                            queue.appendleft(next)
                        else:
                            queue.append(next)

        return dist[end] != INF

    def _dfs(self, cur: int, end: int, flow: int) -> int:
        if cur == end:
            return flow

        visited, reGraph, curEdges, edges, dist = (
            self._visited,
            self._reGraph,
            self._curEdges,
            self._edges,
            self._dist,
        )

        visited[cur] = True
        res = flow
        index = curEdges[cur]
        while res and index < len(reGraph[cur]):
            edgeIndex = reGraph[cur][index]
            next, remain = edges[edgeIndex].toV, edges[edgeIndex].cap - edges[edgeIndex].flow
            if remain > 0 and not visited[next] and dist[next] == dist[cur] + edges[edgeIndex].cost:
                delta = self._dfs(next, end, remain if remain < res else res)
                res -= delta
                edges[edgeIndex].flow += delta
                edges[edgeIndex ^ 1].flow -= delta
            curEdges[cur] += 1
            index = curEdges[cur]

        visited[cur] = False
        return flow - res


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        STRAT, END = n + m + 3, n + m + 4
        mcmf = MinCostMaxFlow(n + m + 10, STRAT, END)
        # 源点到机器人
        for i in range(n):
            mcmf.addEdge(STRAT, i, 1, 0)
        # 机器人到工厂
        for i in range(n):
            for j in range(m):
                mcmf.addEdge(i, n + j, 1, abs(robot[i] - factory[j][0]))
        # 工厂到汇点
        for i in range(m):
            mcmf.addEdge(n + i, END, factory[i][1], 0)
        return mcmf.work()[1]