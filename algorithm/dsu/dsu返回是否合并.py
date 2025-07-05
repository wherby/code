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
        must_uf = UnionFind(n)  # 必选边并查集
        all_uf = UnionFind(n)  # 全图并查集
        min_s, max_s = inf, 0
        for x, y, s, must in edges:
            if must and not must_uf.merge(x, y):  # 必选边成环
                return -1
            all_uf.merge(x, y)
            min_s = min(min_s, s)
            max_s = max(max_s, s)

        if all_uf.cc > 1:  # 图不连通
            return -1

        def check(low: int) -> bool:
            u = UnionFind(n)
            for x, y, s, must in edges:
                if must and s < low:  # 必选边的边权太小
                    return False
                if must or s >= low:
                    u.merge(x, y)

            left_k = k
            for x, y, s, must in edges:
                if left_k == 0 or u.cc == 1:
                    break
                if not must and s < low <= s * 2 and u.merge(x, y):
                    left_k -= 1
            return u.cc == 1

        left, right = min_s, max_s * 2 + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-spanning-tree-stability-with-upgrades/solutions/3711009/liang-chong-fang-fa-er-fen-da-an-kruskal-6p7a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。