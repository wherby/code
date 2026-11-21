# https://leetcode.cn/problems/minimum-cost-to-make-red-nodes-connected/description/
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
