# 这里是用了DFS树上路径DP。其实可以用更简单的结论，只检测长度为1 或者2 的路径， 但是这里的DFS是树上路径的基础做法，维护两个不同特性的值的最大值

from math import inf


class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        g = [[] for _ in values]
        for x, y, c in edges:
            g[x].append((y, c))
            g[y].append((x, c))

        # p_ones 为根到 x 的路径异或和的二进制中的 1 的个数的奇偶性
        # 返回从 x 到其后代的最小开销和（按照 p_ones 的奇偶性分别计算）
        def dfs(x: int, fa: int, p_ones: int) -> list[int]:
            nonlocal ans
            p_val = values[x].bit_count() % 2
            p_ones ^= p_val
            min_sum = [inf, inf]
            min_sum[p_ones] = 0  # x 作为路径的端点

            for y, c in g[x]:
                if y == fa:
                    continue
                mn = dfs(y, x, p_ones)
                mn[0] += c
                mn[1] += c
                # 现在 mn 是从 x 到子树 y 中节点的最小开销和
                # 拼接从 x 到两棵子树中的路径（拼接后，路径在 x 拐弯）
                ans = min(ans, min_sum[0] + mn[p_val], min_sum[1] + mn[p_val ^ 1])
                min_sum[0] = min(min_sum[0], mn[0])
                min_sum[1] = min(min_sum[1], mn[1])

            return min_sum

        ans = inf
        dfs(0, -1, 0)
        return ans if ans < inf else -1


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-path-with-even-xor-parity/solutions/4051727/wei-yun-suan-heng-deng-shi-pin-jie-lu-ji-i2he/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
