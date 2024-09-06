# https://leetcode.cn/contest/biweekly-contest-137/ranking/
# PyIsBestLang
import heapq
from collections import deque
from math import inf
from typing import List


# from sortedcontainers import SortedList
# sys.set_int_max_str_digits(0)  # for big number in leet code


def max(a, b):
    return a if a > b else b


def min(a, b):
    return a if a < b else b


class DinicMaxflowMinCost:
    def __init__(self, n):
        self.n = n
        self.vis = [0] * (self.n + 1)
        self.point_head = [0] * (self.n + 1)
        self.edge_capacity = [0] * 2
        self.edge_cost = [0] * 2
        self.edge_to = [0] * 2
        self.edge_next = [0] * 2
        self.h = [inf] * (self.n + 1)
        self.dis = [inf] * (self.n + 1)
        self.max_flow = 0
        self.min_cost = 0
        self.edge_id = 2
        self.pre_edge = [0] * (self.n + 1)
        self.pre_point = [0] * (self.n + 1)

    def _add_single_edge(self, u, v, cap, c):
        self.edge_capacity.append(cap)
        self.edge_cost.append(c)
        self.edge_to.append(v)
        self.edge_next.append(self.point_head[u])
        self.point_head[u] = self.edge_id
        self.edge_id += 1
        return

    def add_edge(self, u, v, cap, c):
        # assert 1 <= u <= self.n
        # assert 1 <= v <= self.n
        self._add_single_edge(u, v, cap, c)
        self._add_single_edge(v, u, 0, -c)
        return

    def _spfa(self, s):
        self.h[s] = 0
        q = deque([s])
        self.vis[s] = 1
        while q:
            u = q.popleft()
            self.vis[u] = 0
            i = self.point_head[u]
            while i:
                v = self.edge_to[i]
                if self.edge_capacity[i] > 0 and self.h[v] > self.h[u] + self.edge_cost[i]:
                    self.h[v] = self.h[u] + self.edge_cost[i]
                    if not self.vis[v]:
                        q.append(v)
                        self.vis[v] = 1
                i = self.edge_next[i]
        return

    def _dijkstra(self, s, t):
        for i in range(1, self.n + 1):
            self.dis[i] = inf
            self.vis[i] = 0
        self.dis[s] = 0
        q = [(0, s)]
        while q:
            d, u = heapq.heappop(q)
            if self.vis[u]:
                continue
            self.vis[u] = 1
            i = self.point_head[u]
            while i:
                v = self.edge_to[i]
                nc = self.h[u] - self.h[v] + self.edge_cost[i]
                if self.edge_capacity[i] > 0 and self.dis[v] > self.dis[u] + nc:
                    self.dis[v] = self.dis[u] + nc
                    self.pre_edge[v] = i
                    self.pre_point[v] = u
                    if not self.vis[v]:
                        heapq.heappush(q, (self.dis[v], v))
                i = self.edge_next[i]
        return self.dis[t] < inf

    def max_flow_min_cost(self, s, t):
        self._spfa(s)
        while self._dijkstra(s, t):
            for i in range(1, self.n + 1):
                self.h[i] += self.dis[i]

            cur_flow = inf
            v = t
            while v != s:
                i = self.pre_edge[v]
                c = self.edge_capacity[i]
                cur_flow = cur_flow if cur_flow < c else c
                v = self.pre_point[v]

            v = t
            while v != s:
                i = self.pre_edge[v]
                self.edge_capacity[i] -= cur_flow
                self.edge_capacity[i ^ 1] += cur_flow
                v = self.pre_point[v]

            self.max_flow += cur_flow
            self.min_cost += cur_flow * self.h[t]

        return self.max_flow, self.min_cost



class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        flow = DinicMaxflowMinCost(m+n+4)
        for i in range(m):
            for j in range(n):
                flow.add_edge(i+1+1, m+j+1+1, 1, -board[i][j])
        for i in range(m):
            flow.add_edge(1, i+1+1, 1, 0)
        for j in range(n):
            flow.add_edge(m+j+1+1, m+n+1+1, 1, 0)

        flow.add_edge(m+n+1+2, 1, 3, 0)
        flow.add_edge(m+n+1+1, m + 1+ n + 3, 3, 0)
        ans = flow.max_flow_min_cost(m+n+1+2, m+1+n+3)
        return -ans[1]