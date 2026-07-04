# https://leetcode.cn/problems/minimum-time-to-reach-target-with-limited-power/description/

from math import inf
from heapq import heappop,heappush 

class Solution:
    def minTimeMaxPower(self, n: int, edges: list[list[int]], power: int, cost: list[int], source: int, target: int) -> list[int]:
        g = [[] for _ in range(n)]
        for x, y, t in edges:
            g[x].append((y, t))

        dis = [[inf] * (power + 1) for _ in range(n)]
        dis[source][power] = 0
        h = [(0, -power, source)]  # (最短路长度, -剩余电量, 节点编号)

        while h:
            d, rem, x = heappop(h)
            rem = -rem
            if x == target:
                return [d, rem]
            if d > dis[x][rem] or rem < cost[x]:
                continue
            rem -= cost[x]
            for y, t in g[x]:
                new_dis = d + t
                if new_dis < dis[y][rem]:
                    dis[y][rem] = new_dis
                    heappush(h, (new_dis, -rem, y))

        return [-1, -1]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-time-to-reach-target-with-limited-power/solutions/3988936/dijkstra-suan-fa-fen-ceng-tu-zui-duan-lu-t9yx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。