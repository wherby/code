# https://leetcode.cn/contest/weekly-contest-318/problems/minimum-total-distance-traveled/
# https://leetcode.cn/contest/weekly-contest-318/ranking/1/   [@草莓包饭]

from typing import List
class KM:
    INF = int(1e9)

    def __init__(self, graph):
        ma = max(len(graph), len(graph[0]))
        self.graph = graph
        self.vis_x = set()
        self.vis_y = set()
        self.match = [-1] * ma
        self.lx = [max(row) for row in graph]
        self.ly = [0] * ma
        self.slack = []
        self.fa = []

        self.nx, self.ny = len(graph), len(graph[0])

    def find_path(self, x):
        self.vis_x.add(x)
        for y in range(self.ny):
            if y in self.vis_y:
                continue
            tmp_delta = self.lx[x] + self.ly[y] - self.graph[x][y]
            if tmp_delta == 0:
                self.vis_y.add(y)
                self.fa[y + self.nx] = x
                if self.match[y] == -1:
                    return y + self.nx
                self.fa[self.match[y]] = y + self.nx
                res = self.find_path(self.match[y])
                if res > 0:
                    return res
            elif self.slack[x] > tmp_delta:
                self.slack[x] = tmp_delta

        return -1

    def solve(self):
        for x in range(self.nx):
            self.slack = [KM.INF] * self.nx
            self.fa = [-1] * (self.nx + self.ny)
            self.vis_x.clear()
            self.vis_y.clear()
            fir = 1
            leaf = -1
            while True:
                if fir == 1:
                    leaf = self.find_path(x)
                    fir = 0
                else:
                    for i in range(self.nx):
                        if self.slack[i] == 0:
                            self.slack[i] = KM.INF
                            leaf = self.find_path(i)
                            if leaf > 0:
                                break
                if leaf > 0:
                    p = leaf
                    while p > 0:
                        self.match[p - self.nx] = self.fa[p]
                        p = self.fa[self.fa[p]]
                    break
                else:
                    delta = KM.INF
                    for i in range(self.nx):
                        if i in self.vis_x and delta > self.slack[i]:
                            delta = self.slack[i]
                    for i in range(self.nx):
                        if i in self.vis_x:
                            self.lx[i] -= delta
                            self.slack[i] -= delta
                    for j in range(self.ny):
                        if j in self.vis_y:
                            self.ly[j] += delta
        return self.match


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        graph = []
        ff = []
        for f, limit in factory:
            for _ in range(limit):
                ff.append(f)
        factory = ff

        for r in robot:
            tmp = []
            for f in factory:
                tmp.append(-abs(r - f))
            graph.append(tmp)

        a = KM(graph).solve()
        ans = 0
        #print(a)
        for f, r in enumerate(a):
            if r != -1:
                ans += abs(factory[f] - robot[r])
        return ans

re =Solution().minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]])
print(re)