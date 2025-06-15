# 求和的时候可以用这种解法， 求最大最小值则不可以
from typing import List, Tuple, Optional

class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)  # 使用下标 1 到 n

    # a[i] 增加 val
    # 1 <= i <= n
    def update(self, i: int, val: int) -> None:
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    # 计算前缀和 a[1] + ... + a[i]
    # 1 <= i <= n
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n + 1)]
        for x, y, _ in edges:
            g[x].append(y)
            g[y].append(x)

        in_ = [0] * (n + 1)
        out = [0] * (n + 1)
        clock = 0
        def dfs(x: int, fa: int) -> None:
            nonlocal clock
            clock += 1
            in_[x] = clock  # 进来的时间
            for y in g[x]:
                if y != fa:
                    dfs(y, x)
            out[x] = clock  # 离开的时间
        dfs(1, 0)

        weight = [0] * (n + 1)
        diff = FenwickTree(n)
        def update(x: int, y: int, w: int) -> None:
            # 保证 y 是 x 的儿子
            if in_[x] > in_[y]:
                y = x
            d = w - weight[y]  # 边权的增量
            weight[y] = w
            # 把子树 y 中的最短路长度都增加 d（用差分树状数组维护）
            diff.update(in_[y], d)
            diff.update(out[y] + 1, -d)

        for e in edges:
            update(*e)

        ans = []
        for q in queries:
            if q[0] == 1:
                update(*q[1:])
            else:
                ans.append(diff.pre(in_[q[1]]))
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/shortest-path-in-a-weighted-tree/solutions/3649372/dfs-shi-jian-chuo-chai-fen-shu-zhuang-sh-h8q3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。