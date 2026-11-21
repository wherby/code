# https://leetcode.cn/problems/minimum-cost-to-make-red-nodes-connected/description/
# 给你一个整数 n，表示一棵有 n 个节点的树，节点编号从 0 到 n - 1，并且树以节点 0 为 根节点。这棵树由一个长度为 n - 1 的二维数组 edges 表示，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 之间存在一条 无向 边。
# 另给你一个长度为 n 的字符串 colors，其中 colors[i] 表示节点 i 的颜色：'R' 表示红色，'B' 表示蓝色。
# 你可以 翻转 任意节点的颜色：从 'R' 变为 'B'，或从 'B' 变为 'R'。翻转节点 u 的代价等于以节点 u 为根的子树的大小。
# 你的目标是通过翻转颜色，使所有 红色 节点在树中形成 一个连通分量 。蓝色节点可以不连通。没有红色节点的配置也视为有效。
# 返回实现这一目标所需的 最小总代价 。
# 在有根树中，节点 v 的子树是由所有到根节点的路径经过 v 的节点组成的集合。
# 先弃后取，先把所有点都变蓝，然后计算当前点有一个红色区域的最大增益
class Solution:
    def minCost(self, n: int, colors: str, edges: list[list[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        base = mx = 0

        def dfs(x: int, fa: int) -> tuple[int, int]:
            nonlocal base, mx
            size = 1
            f = 0
            # 遍历 x 的子树
            for y in g[x]:
                if y != fa:
                    sz, fy = dfs(y, x)
                    size += sz
                    # 如果 fy < 0，那么子树 y 都变成蓝色是最优的，这已经算入 base 中
                    f += max(fy, 0)

            # 考虑节点 x
            if colors[x] == "R":
                base += size  # 把 x 变成蓝色的代价
                f += size  # 把 x 恢复成红色可以让 base 减少 size
            else:
                f -= size  # 把 x 变成红色会让 base 增大 size
            mx = max(mx, f)  # 最多可以让 base 减少多少

            return size, f

        dfs(0, -1)
        return base - mx


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-to-make-red-nodes-connected/solutions/4054664/shu-xing-dppythonjavacgo-by-endlesscheng-vy5z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
