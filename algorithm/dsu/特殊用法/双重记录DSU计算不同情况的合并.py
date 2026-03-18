# 用两个DSU，一个记录必要边的合并，一个记录所有边的合并。必要边成环或者图不连通直接返回-1，否则剩余的边按照稳定性从大到小排序，依次合并，直到得到生成树为止。每次合并都更新答案。

from typing import List, Tuple, Optional
from math import inf

class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    # 返回是否合并成功
    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return False
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UnionFind(n)
        all_uf = UnionFind(n)
        min_s1 = inf
        for x, y, s, must in edges:
            if must:
                if not uf.merge(x, y):  # 必选边成环
                    return -1
                min_s1 = min(min_s1, s)
            all_uf.merge(x, y)

        if all_uf.cc > 1:  # 图不连通
            return -1

        left = uf.cc - 1
        if left == 0:  # 只需选必选边
            return min_s1

        # Kruskal 求最大生成树
        edges.sort(key=lambda e: -e[2])
        ans = min_s1
        for x, y, s, must in edges:
            if not must and uf.merge(x, y):
                ans = min(ans, s if left > k else s * 2)
                left -= 1
                if left == 0:  # 已经得到生成树了
                    break
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-spanning-tree-stability-with-upgrades/solutions/3711009/liang-chong-fang-fa-er-fen-da-an-kruskal-6p7a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。