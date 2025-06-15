# https://leetcode.cn/problems/find-weighted-median-node-in-tree/solutions/3700556/mo-ban-zui-jin-gong-gong-zu-xian-lcapyth-6ekj/
from typing import List, Tuple, Optional
from collections import defaultdict, deque
class LcaBinaryLifting:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        self.m = m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        depth = [0] * n
        dis = [0] * n
        pa = [[-1] * m for _ in range(n)]

        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y, w in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dis[y] = dis[x] + w
                    dfs(y, x)

        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]

        self.depth = depth
        self.dis = dis
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:
                node = self.pa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(self.m - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时往上跳 2**i 步
        return self.pa[x][0]

    # 返回 x 到 y 的距离（最短路长度）
    def get_dis(self, x: int, y: int) -> int:
        return self.dis[x] + self.dis[y] - self.dis[self.get_lca(x, y)] * 2

    # 从 x 往上跳【至多】d 距离，返回最远能到达的节点
    def upto_dis(self, x: int, d: int) -> int:
        dx = self.dis[x]
        for i in range(self.m - 1, -1, -1):
            p = self.pa[x][i]
            if p != -1 and dx - self.dis[p] <= d:  # 可以跳至多 d
                x = p
        return x


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = LcaBinaryLifting(edges)
        ans = []
        for x, y in queries:
            if x == y:
                ans.append(x)
                continue
            lca = g.get_lca(x, y)
            dis_xy = g.dis[x] + g.dis[y] - g.dis[lca] * 2
            half = (dis_xy + 1) // 2
            if g.dis[x] - g.dis[lca] >= half:  # 答案在 x-lca 路径中
                # 先往上跳至多 half-1，然后再跳一步，就是至少 half
                to = g.upto_dis(x, half - 1)
                res = g.pa[to][0]  # 再跳一步
            else:  # 答案在 y-lca 路径中
                # 从 y 出发至多 dis_xy-half，就是从 x 出发至少 half
                res = g.upto_dis(y, dis_xy - half)
            ans.append(res)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-weighted-median-node-in-tree/solutions/3700556/mo-ban-zui-jin-gong-gong-zu-xian-lcapyth-6ekj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。